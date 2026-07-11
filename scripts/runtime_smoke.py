#!/usr/bin/env python3
"""Validate credential-free Claude/Codex structure and CLI contracts."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import tomllib
from pathlib import Path

import sync_adapters as sa

REPO_ROOT = Path(__file__).resolve().parents[1]
KEY_SKILLS = ("constitute", "help", "cdd-status")
NESTED_DIRS = ("src", "design", "docs")
RUNTIMES = ("claude", "codex")
CLI_HELP_REQUIREMENTS = {
    "claude": (
        "--print",
        "--json-schema",
        "--no-session-persistence",
        "--permission-mode",
        "--setting-sources",
        "--tools",
    ),
    "codex": (
        "exec",
        "--ask-for-approval",
        "--sandbox",
        "--cd",
        "--ephemeral",
        "--ignore-user-config",
        "--output-schema",
        "--output-last-message",
    ),
}


def _copy_tree(source: Path, destination: Path) -> None:
    if source.is_dir():
        shutil.copytree(source, destination, copy_function=shutil.copy2)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def prepare_fixture(repo_root: Path, destination: Path, runtime: str) -> None:
    """Create one minimal fresh-project fixture without runtime hook settings."""

    if runtime not in RUNTIMES:
        raise ValueError(f"runtime must be one of {RUNTIMES}, got {runtime!r}")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError(f"fixture destination must be absent or empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)

    for common in ("workflow", "templates", "standards", "skill_testing"):
        _copy_tree(repo_root / common, destination / common)

    if runtime == "claude":
        _copy_tree(repo_root / "CLAUDE.md", destination / "CLAUDE.md")
        _copy_tree(repo_root / ".claude" / "skills", destination / ".claude" / "skills")
        _copy_tree(repo_root / ".claude" / "agents", destination / ".claude" / "agents")
        _copy_tree(repo_root / ".claude" / "hooks", destination / ".claude" / "hooks")
        nested_name = "CLAUDE.md"
    else:
        _copy_tree(repo_root / "AGENTS.md", destination / "AGENTS.md")
        _copy_tree(repo_root / ".agents" / "skills", destination / ".agents" / "skills")
        _copy_tree(repo_root / ".codex" / "agents", destination / ".codex" / "agents")
        _copy_tree(repo_root / ".codex" / "hooks", destination / ".codex" / "hooks")
        nested_name = "AGENTS.md"

    for directory in NESTED_DIRS:
        _copy_tree(
            repo_root / directory / nested_name,
            destination / directory / nested_name,
        )


def _frontmatter_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return ""
    for line in text.splitlines()[1:]:
        if line == "---":
            break
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip('"')
    return ""


def validate_fixture(
    fixture: Path,
    runtime: str,
    manifest: sa.Manifest,
) -> list[str]:
    """Return structural discovery errors for one prepared runtime fixture."""

    errors: list[str] = []
    if runtime == "claude":
        root_instructions = fixture / "CLAUDE.md"
        skills_root = fixture / ".claude" / "skills"
        agents_root = fixture / ".claude" / "agents"
        hooks_root = fixture / ".claude" / "hooks"
        nested_name = "CLAUDE.md"
        forbidden_config = fixture / ".claude" / "settings.json"
    else:
        root_instructions = fixture / "AGENTS.md"
        skills_root = fixture / ".agents" / "skills"
        agents_root = fixture / ".codex" / "agents"
        hooks_root = fixture / ".codex" / "hooks"
        nested_name = "AGENTS.md"
        forbidden_config = fixture / ".codex" / "hooks.json"

    if not root_instructions.is_file():
        errors.append(f"{runtime}: missing root instructions: {root_instructions}")
    if forbidden_config.exists():
        errors.append(f"{runtime}: live fixture must omit write-capable hook config: {forbidden_config}")

    expected_skills = manifest.sources["skills"].expected_count
    skill_files = sorted(skills_root.glob("*/SKILL.md"))
    if len(skill_files) != expected_skills:
        errors.append(f"{runtime}: expected {expected_skills} discoverable skills, found {len(skill_files)}")
    for skill in KEY_SKILLS:
        path = skills_root / skill / "SKILL.md"
        if not path.is_file():
            errors.append(f"{runtime}: missing key skill {skill}: {path}")
        elif _frontmatter_name(path) != skill:
            errors.append(f"{runtime}: key skill frontmatter mismatch: {path}")

    expected_agents = manifest.sources["agents"].expected_count
    if runtime == "claude":
        agent_files = sorted(agents_root.glob("*.md"))
        for path in agent_files:
            if not _frontmatter_name(path):
                errors.append(f"claude: invalid agent frontmatter: {path}")
    else:
        agent_files = sorted(agents_root.glob("*.toml"))
        for path in agent_files:
            try:
                values = tomllib.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, tomllib.TOMLDecodeError) as exc:
                errors.append(f"codex: invalid agent TOML {path}: {exc}")
                continue
            if set(values) != {"name", "description", "developer_instructions"}:
                errors.append(f"codex: unexpected agent fields: {path}")
    if len(agent_files) != expected_agents:
        errors.append(f"{runtime}: expected {expected_agents} agents, found {len(agent_files)}")

    expected_hooks = manifest.sources["hooks"].expected_count
    hook_files = sorted(hooks_root.glob("*.sh"))
    if len(hook_files) != expected_hooks:
        errors.append(f"{runtime}: expected {expected_hooks} hooks, found {len(hook_files)}")

    for directory in NESTED_DIRS:
        path = fixture / directory / nested_name
        if not path.is_file():
            errors.append(f"{runtime}: missing nested instructions: {path}")
    return errors


def _iter_commands(value: object):
    if isinstance(value, dict):
        command = value.get("command")
        if isinstance(command, str):
            yield command
        for child in value.values():
            yield from _iter_commands(child)
    elif isinstance(value, list):
        for child in value:
            yield from _iter_commands(child)


def _hook_config_errors(repo_root: Path) -> list[str]:
    errors: list[str] = []
    configs = (
        (repo_root / ".claude" / "settings.json", ".claude/hooks/"),
        (repo_root / ".codex" / "hooks.json", ".codex/hooks/"),
    )
    for config_path, prefix in configs:
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid runtime hook config {config_path}: {exc}")
            continue
        referenced = set()
        for command in _iter_commands(config):
            referenced.update(re.findall(re.escape(prefix) + r"([a-z0-9-]+\.sh)", command))
        if not referenced:
            errors.append(f"runtime hook config has no generated hook references: {config_path}")
        for name in sorted(referenced):
            if not (repo_root / prefix / name).is_file():
                errors.append(f"runtime hook config references missing script: {prefix}{name}")
    return errors


def structural_errors(repo_root: Path = REPO_ROOT) -> list[str]:
    """Validate the committed adapter graph and two disposable discovery fixtures."""

    errors: list[str] = []
    manifest_path = repo_root / "cdd-manifest.toml"
    try:
        manifest = sa.load_manifest(manifest_path)
        report = sa.check_plan(sa.build_sync_plan(manifest, repo_root))
    except (OSError, UnicodeError, ValueError, tomllib.TOMLDecodeError) as exc:
        return [f"adapter manifest/check failed: {exc}"]
    if not report.ok:
        errors.extend(f"adapter {drift.status.lower()}: {drift.path}" for drift in report.drifts if drift.status != sa.OK)
        errors.extend(
            f"adapter {diagnostic.severity.lower()}: {diagnostic.path}: {diagnostic.message}"
            for diagnostic in report.diagnostics
        )
    errors.extend(_hook_config_errors(repo_root))

    with tempfile.TemporaryDirectory(prefix="cdd-runtime-smoke-") as tmp:
        temp_root = Path(tmp)
        for runtime in RUNTIMES:
            fixture = temp_root / runtime
            prepare_fixture(repo_root, fixture, runtime)
            errors.extend(validate_fixture(fixture, runtime, manifest))
    return errors


def validate_cli_help(path: Path, runtime: str) -> list[str]:
    """Validate the pinned CLI exposes every release-contract option."""

    try:
        help_text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"cannot read {runtime} CLI help evidence {path}: {exc}"]
    return [
        f"{runtime} CLI help omits required option: {token}"
        for token in CLI_HELP_REQUIREMENTS[runtime]
        if token not in help_text
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Claude/Codex structure and CLI contracts.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--structural", action="store_true", help="Run credential-free structural smoke checks.")
    mode.add_argument("--prepare-fixture", type=Path, metavar="DIR", help="Create a minimal discovery fixture.")
    mode.add_argument("--validate-cli-help", type=Path, metavar="FILE", help="Validate pinned CLI help evidence.")
    parser.add_argument("--runtime", choices=RUNTIMES, help="Runtime for fixture or CLI validation.")
    args = parser.parse_args(argv)

    if args.prepare_fixture is not None and args.runtime is None:
        parser.error("--prepare-fixture requires --runtime")
    if args.validate_cli_help is not None and args.runtime is None:
        parser.error("--validate-cli-help requires --runtime")

    try:
        if args.structural:
            errors = structural_errors()
        elif args.prepare_fixture is not None:
            prepare_fixture(REPO_ROOT, args.prepare_fixture, args.runtime)
            manifest = sa.load_manifest(REPO_ROOT / "cdd-manifest.toml")
            errors = validate_fixture(args.prepare_fixture, args.runtime, manifest)
        else:
            errors = validate_cli_help(args.validate_cli_help, args.runtime)
    except (OSError, UnicodeError, ValueError, tomllib.TOMLDecodeError) as exc:
        errors = [str(exc)]

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"runtime-smoke summary: FAIL ({len(errors)} error(s))")
        return 1
    print("runtime-smoke summary: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
