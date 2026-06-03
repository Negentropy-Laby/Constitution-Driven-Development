#!/usr/bin/env python3
"""Non-blocking lint for CDD skill markdown files.

Default mode reports findings and exits 0 so it can be used as an advisory check.
Use --strict to return exit 1 when errors are found.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
TEMPLATES_DIR = REPO_ROOT / ".claude" / "docs" / "templates"

REQUIRED_FRONTMATTER = {
    "name",
    "description",
    "argument-hint",
    "user-invocable",
    "allowed-tools",
}
BROKEN_TERMS = ("or" + "eate", "oon" + "firmation", "If " + "o")
BROKEN_WORDS = re.compile(r"\b(" + "|".join(re.escape(term) for term in BROKEN_TERMS) + r")\b", re.IGNORECASE)
COMMAND_REF = re.compile(r"(?<![\w.:-])/[a-z][a-z0-9-]*\b")
HEADING = re.compile(r"^(#{1,6})(\s+)(.+?)\s*$")
BAD_HEADING = re.compile(r"^(#{1,6})(?!#)(?!\s|$)")
PATH_IN_BACKTICKS = re.compile(r"`([^`\n]+\.(?:md|yaml|yml|json|txt|py|sh|gd|cs|ts|tsx|rs|go|toml|cfg|ini))`")

KNOWN_GENERATED_ROOTS = (
    "design/",
    "docs/architecture/",
    "docs/reference/",
    "docs/engine-reference/",
    "memory_bank/",
    "production/",
    "prototypes/",
    "src/",
    "tests/",
)


@dataclass
class Finding:
    severity: str
    path: Path
    line: int
    message: str


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def parse_frontmatter(text: str) -> tuple[dict[str, str], int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 0

    fm_lines: list[str] = []
    for index, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            fields: dict[str, str] = {}
            for fm_line in fm_lines:
                if ":" in fm_line and not fm_line.startswith((" ", "\t", "-")):
                    key, value = fm_line.split(":", 1)
                    fields[key.strip()] = value.strip()
            return fields, index
        fm_lines.append(line)

    return {}, 0


def collect_known_commands() -> set[str]:
    commands: set[str] = set()
    if not SKILLS_DIR.exists():
        return commands

    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        commands.add("/" + skill_file.parent.name)
        fields, _ = parse_frontmatter(skill_file.read_text(encoding="utf-8", errors="replace"))
        if "name" in fields and fields["name"]:
            commands.add("/" + fields["name"].strip().strip('"').strip("'"))
    return commands


def line_number(lines: list[str], offset: int) -> int:
    count = 0
    total = 0
    for line in lines:
        total += len(line) + 1
        count += 1
        if total > offset:
            return count
    return max(1, count)


def template_exists_for(path_text: str) -> bool:
    if not TEMPLATES_DIR.exists():
        return False
    name = Path(path_text).name
    stem = Path(path_text).stem
    return any(candidate.name == name or candidate.stem == stem for candidate in TEMPLATES_DIR.rglob("*"))


def lint_file(path: Path, known_commands: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    fields, fm_end = parse_frontmatter(text)
    if not fields:
        findings.append(Finding("ERROR", path, 1, "missing or unterminated YAML frontmatter"))
    else:
        missing = sorted(REQUIRED_FRONTMATTER - set(fields))
        if missing:
            findings.append(Finding("ERROR", path, 1, "missing required frontmatter fields: " + ", ".join(missing)))
        if fm_end < 2:
            findings.append(Finding("ERROR", path, 1, "frontmatter closing marker not found"))

    for match in BROKEN_WORDS.finditer(text):
        findings.append(Finding("ERROR", path, line_number(lines, match.start()), f"broken word found: {match.group(0)}"))

    fence_count = sum(1 for line in lines if line.strip().startswith("```"))
    if fence_count % 2 != 0:
        findings.append(Finding("ERROR", path, len(lines), "unbalanced markdown code fences"))

    heading_count = 0
    for idx, line in enumerate(lines, start=1):
        if BAD_HEADING.match(line):
            findings.append(Finding("ERROR", path, idx, "markdown heading missing a space after #"))
        if HEADING.match(line):
            heading_count += 1
    if heading_count == 0:
        findings.append(Finding("WARN", path, 1, "no markdown headings found after frontmatter"))

    ignored = {"/api", "/docs", "/src", "/tests", "/tmp"}
    for match in COMMAND_REF.finditer(text):
        command = match.group(0)
        if command in ignored:
            continue
        if command not in known_commands:
            findings.append(Finding("ERROR", path, line_number(lines, match.start()), f"unknown slash command reference: {command}"))

    for match in PATH_IN_BACKTICKS.finditer(text):
        path_text = match.group(1)
        if " " in path_text or path_text.startswith(("http://", "https://")):
            continue
        normalized = path_text.replace("\\", "/")
        if normalized.startswith(("./", "../", "/")):
            continue
        if not (
            normalized.startswith(".claude/")
            or normalized.startswith(".github/")
            or normalized.startswith("CDD Skill Testing Framework/")
            or normalized.startswith(KNOWN_GENERATED_ROOTS)
        ):
            continue
        if (REPO_ROOT / normalized).exists() or template_exists_for(normalized):
            continue
        findings.append(
            Finding(
                "WARN",
                path,
                line_number(lines, match.start()),
                f"artifact path has no existing file or same-name template: {normalized}",
            )
        )

    return findings


def write_bad_skill(directory: Path) -> Path:
    skill_dir = directory / "broken"
    skill_dir.mkdir()
    bad_file = skill_dir / "SKILL.md"
    bad_file.write_text(
        """---
name: broken
description: Broken test skill
---
#Broken

Run /missing-command after you """ + "or" + """eate the file.
```
unterminated
""",
        encoding="utf-8",
    )
    return bad_file


def run_self_test() -> int:
    with TemporaryDirectory() as temp:
        bad_file = write_bad_skill(Path(temp))
        findings = lint_file(bad_file, known_commands={"/broken"})
    messages = "\n".join(f.message for f in findings)
    expected = [
        "missing required frontmatter fields",
        "broken word found",
        "unknown slash command reference: /missing-command",
        "unbalanced markdown code fences",
        "markdown heading missing a space after #",
    ]
    missing = [item for item in expected if item not in messages]
    if missing:
        print("SELF-TEST FAILED: missing detections: " + ", ".join(missing), file=sys.stderr)
        return 1
    print("SELF-TEST PASSED: broken frontmatter, command refs, bad words, headings, and code fences detected.")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Lint CDD skill markdown files.")
    parser.add_argument("paths", nargs="*", help="Skill files or directories. Defaults to .claude/skills/*/SKILL.md")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on ERROR findings")
    parser.add_argument("--self-test", action="store_true", help="Run internal detection self-test")
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()

    known_commands = collect_known_commands()
    targets: list[Path] = []
    if args.paths:
        for raw in args.paths:
            candidate = (REPO_ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw)
            if candidate.is_dir():
                targets.extend(candidate.glob("*/SKILL.md"))
                if candidate.name != "skills":
                    targets.extend(candidate.rglob("SKILL.md"))
            else:
                targets.append(candidate)
    else:
        targets = sorted(SKILLS_DIR.glob("*/SKILL.md"))

    all_findings: list[Finding] = []
    for target in sorted(set(targets)):
        if target.exists():
            all_findings.extend(lint_file(target, known_commands))
        else:
            all_findings.append(Finding("ERROR", target, 1, "target file does not exist"))

    for finding in all_findings:
        print(f"{finding.severity}: {rel(finding.path)}:{finding.line}: {finding.message}")

    errors = sum(1 for finding in all_findings if finding.severity == "ERROR")
    warnings = sum(1 for finding in all_findings if finding.severity == "WARN")
    print(f"skill-lint summary: {errors} error(s), {warnings} warning(s), {len(targets)} file(s) checked")

    if args.strict and errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
