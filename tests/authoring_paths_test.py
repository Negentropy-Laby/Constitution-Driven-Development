#!/usr/bin/env python3
"""Gate 5 tests: authoring/consumer boundary points at canonical roots.

Part 1 asserts the rewritten canonical skill/agent sources direct authoring at
canonical roots and adapter regeneration (and do not direct writes at generated
paths). Part 2 executes hooks/validate-generated-adapter-change.sh with representative JSON
and asserts it classifies canonical vs generated paths correctly. These tests
read the real canonical sources; they do not mutate the repository.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def read_canonical(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


def frontmatter_value(text: str, key: str) -> str:
    for line in text.splitlines():
        if line.startswith(key + ":"):
            return line.split(":", 1)[1].strip()
    return ""


def iter_hook_commands(value: object):
    """Yield command strings from a runtime hook configuration subtree."""
    if isinstance(value, dict):
        command = value.get("command")
        if isinstance(command, str):
            yield command
        for child in value.values():
            yield from iter_hook_commands(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_hook_commands(child)


def _resolve_git_bash() -> str | None:
    """Find a Bash interpreter able to run the hook.

    On Windows, ``shutil.which("bash")`` can return
    ``C:\\Windows\\System32\\bash.exe`` (the WSL launcher), which cannot execute
    this hook. Prefer Git Bash by checking the bash co-located with ``git`` and
    the common Git install locations, and reject any candidate whose resolved
    path is under ``\\Windows\\System32`` (the WSL launcher lives there). On
    other platforms ``shutil.which("bash")`` is reliable. Returns the
    interpreter path, or None if no suitable Bash is found.
    """
    if os.name != "nt":
        return shutil.which("bash")

    candidates: list[Path] = []
    git_exe = shutil.which("git")
    if git_exe:
        git_root = Path(git_exe).resolve().parent.parent
        candidates.append(git_root / "bin" / "bash.exe")
        candidates.append(git_root / "usr" / "bin" / "bash.exe")
    for env_var in ("ProgramFiles", "ProgramFiles(x86)"):
        base = os.environ.get(env_var)
        if base:
            candidates.append(Path(base) / "Git" / "bin" / "bash.exe")
            candidates.append(Path(base) / "Git" / "usr" / "bin" / "bash.exe")
    local_appdata = os.environ.get("LOCALAPPDATA")
    if local_appdata:
        candidates.append(Path(local_appdata) / "Programs" / "Git" / "bin" / "bash.exe")
        candidates.append(Path(local_appdata) / "Programs" / "Git" / "usr" / "bin" / "bash.exe")
    which_bash = shutil.which("bash")
    if which_bash:
        candidates.append(Path(which_bash))

    system32 = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32"
    seen: set[str] = set()
    for cand in candidates:
        try:
            resolved = cand.resolve()
        except OSError:
            continue
        key = str(resolved).lower()
        if key in seen or not resolved.is_file():
            continue
        seen.add(key)
        try:
            resolved.relative_to(system32)
            continue  # under System32 -> WSL launcher, not usable
        except ValueError:
            pass
        return str(resolved)
    return None


def _env_with_strict_jq_shim(directory: Path) -> dict[str, str]:
    """Return an environment whose jq shim rejects non-raw output input.

    The hook first uses jq to parse its JSON payload, then uses raw-slurp mode to
    wrap multi-line advisory text in one JSON document. The shim implements only
    those contracts and deliberately fails if the output call omits ``-R`` or
    ``-s``.
    """
    shim = directory / "jq"
    script = r'''#!/usr/bin/env python
import json
import sys

args = sys.argv[1:]
expression = args[-1] if args else ""
raw = sys.stdin.read()
raw_slurp = any(arg.startswith("-") and "R" in arg and "s" in arg for arg in args)

if raw_slurp:
    if 'decision:"block"' in expression:
        payload = {
            "decision": "block",
            "reason": raw,
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": raw,
            },
        }
    else:
        payload = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": raw,
            }
        }
    print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    raise SystemExit(0)

if "-r" in args:
    payload = json.loads(raw)
    tool_input = payload.get("tool_input", {})
    if "file_path" in expression:
        print(tool_input.get("file_path") or "")
    elif "command" in expression:
        print(tool_input.get("command") or "")
    raise SystemExit(0)

print("strict jq shim: expected JSON parse mode or -Rsc", file=sys.stderr)
raise SystemExit(64)
'''
    shim.write_bytes(script.encode("utf-8"))
    shim.chmod(0o755)
    env = os.environ.copy()
    env["PATH"] = str(directory) + os.pathsep + env.get("PATH", "")
    return env


class AuthoringPathTests(unittest.TestCase):
    def test_skill_improve_targets_canonical_and_regenerates(self) -> None:
        text = read_canonical("skills/skill-improve/SKILL.md")
        # Authoring/revert target is the canonical root, not the generated trees.
        self.assertIn("skills/[name]/SKILL.md", text)
        self.assertIn("sync_adapters.py --write --class skills", text)
        # Snapshot rollback preserves the exact invocation baseline regardless
        # of Git/index state; it must not depend on git checkout.
        self.assertIn("snapshot", text.lower())
        self.assertNotIn("git checkout -- .claude/skills", text)
        # No remaining authoring pointer at the generated trees.
        self.assertNotIn("write the improved skill to `.claude/skills", text)
        self.assertNotIn("write the improved skill to `.agents/skills", text)

    def test_skill_test_enumerates_canonical_skills(self) -> None:
        text = read_canonical("skills/skill-test/SKILL.md")
        self.assertIn("Glob `skills/*/SKILL.md`", text)
        self.assertIn("Find skill at `skills/[name]/SKILL.md`.", text)
        # Audit still sources the agent list from the catalog, not a directory glob.
        self.assertIn("skill_testing/catalog.yaml", text)
        self.assertNotIn("Glob `.claude/skills", text)
        self.assertNotIn("not found in `.claude/skills/`", text)

    def test_setup_engine_authors_instructions_and_regenerates(self) -> None:
        text = read_canonical("skills/setup-engine/SKILL.md")
        # Root-instruction authoring target is the canonical INSTRUCTIONS.md.
        self.assertIn("write these settings to `INSTRUCTIONS.md`", text)
        self.assertNotIn("write these settings to `CLAUDE.md`", text)
        # Regeneration is wired and Bash is permitted so the command can run.
        self.assertIn("sync_adapters.py --write --class root-instructions", text)
        allowed = frontmatter_value(text, "allowed-tools")
        self.assertIn("Bash", allowed)

    def test_godot_specialist_references_instructions(self) -> None:
        text = read_canonical("agents/godot-specialist.md")
        self.assertIn("Document every autoload's purpose in INSTRUCTIONS.md", text)
        self.assertNotIn("purpose in CLAUDE.md", text)

    def test_runtime_hook_configs_reference_existing_scripts(self) -> None:
        configs = {
            ".claude/settings.json": ".claude",
            ".codex/hooks.json": ".codex",
        }
        all_commands: list[str] = []
        for config_path, runtime_root in configs.items():
            data = json.loads(read_canonical(config_path))
            commands = list(iter_hook_commands(data["hooks"]))
            self.assertTrue(commands, config_path)
            all_commands.extend(commands)
            for command in commands:
                matches = re.findall(
                    rf"{re.escape(runtime_root)}/hooks/([A-Za-z0-9._-]+\.sh)",
                    command,
                )
                self.assertEqual(len(matches), 1, f"{config_path}: {command}")
                target = REPO_ROOT / runtime_root / "hooks" / matches[0]
                self.assertTrue(target.is_file(), f"missing hook target: {target}")

        self.assertNotIn("validate-skill-change.sh", "\n".join(all_commands))
        codex = json.loads(read_canonical(".codex/hooks.json"))
        for command in iter_hook_commands(codex["hooks"]):
            self.assertIn(
                "$(git rev-parse --show-toplevel)/.codex/hooks/",
                command,
            )


class ValidateGeneratedAdapterChangeHookTests(unittest.TestCase):
    """Executes hooks/validate-generated-adapter-change.sh (requires bash)."""

    def setUp(self) -> None:
        # Find a Bash that can actually run the hook. On Windows this must be
        # Git Bash; a bare shutil.which("bash") may otherwise resolve to the WSL
        # launcher (C:\Windows\System32\bash.exe), which cannot execute this
        # script and causes the hook tests to fail or hang.
        self.bash = _resolve_git_bash()
        if self.bash is None:
            self.skipTest(
                "no suitable Bash available "
                "(Windows: Git Bash not found, only the WSL launcher present)"
            )
        self.hook = REPO_ROOT / "hooks" / "validate-generated-adapter-change.sh"

    def _run(
        self,
        file_path: str | None,
        payload: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if payload is None:
            payload = json.dumps(
                {"tool_name": "Write", "tool_input": {"file_path": file_path}}
            )
        return subprocess.run(
            [self.bash, self.hook.as_posix()],
            input=payload,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
        )

    def _run_codex(
        self,
        command: str,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        """Run the hook with a Codex apply_patch payload (tool_input.command)."""
        payload = json.dumps(
            {"tool_name": "apply_patch", "tool_input": {"command": command}}
        )
        return self._run(None, payload=payload, env=env)

    def test_canonical_skill_advises_lint_and_regeneration(self) -> None:
        proc = self._run("skills/foo/SKILL.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Canonical Skill Modified: foo", proc.stderr)
        self.assertIn("skill_lint.py skills/foo/SKILL.md", proc.stderr)
        self.assertIn("sync_adapters.py --write --class skills", proc.stderr)

    def test_generated_claude_skill_is_warned(self) -> None:
        proc = self._run("repo/.claude/skills/foo/SKILL.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Generated Adapter Edited: foo", proc.stderr)
        self.assertIn("GENERATED", proc.stderr)
        self.assertIn("skills/foo/SKILL.md", proc.stderr)  # points to canonical source

    def test_generated_codex_skill_is_warned(self) -> None:
        proc = self._run(".agents/skills/foo/SKILL.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Generated Adapter Edited: foo", proc.stderr)
        self.assertIn("GENERATED", proc.stderr)

    def test_unrelated_path_is_silent(self) -> None:
        proc = self._run("README.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stderr, "")
        self.assertEqual(proc.stdout, "")

    def test_backslash_path_is_normalized_to_canonical(self) -> None:
        proc = self._run("skills\\foo\\SKILL.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Canonical Skill Modified: foo", proc.stderr)

    def test_invalid_json_exits_clean(self) -> None:
        # Malformed JSON must not crash the hook (advisory; exit 0 always).
        proc = self._run(None, payload="{not valid json")
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_empty_input_exits_clean(self) -> None:
        # Empty stdin must not crash the hook (advisory; exit 0 always).
        proc = self._run(None, payload="")
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_grep_fallback_classifies_when_jq_absent(self) -> None:
        # Force jq off PATH so the hook's grep fallback is exercised. If jq
        # cannot be fully removed (multiple installs), skip rather than
        # false-pass on the jq code path.
        env = os.environ.copy()
        jq_exe = shutil.which("jq")
        if jq_exe:
            jq_dirs = {str(Path(jq_exe).resolve().parent).lower()}
            env["PATH"] = os.pathsep.join(
                p for p in env["PATH"].split(os.pathsep)
                if p and str(Path(p).resolve()).lower() not in jq_dirs
            )
        check = subprocess.run(
            [self.bash, "-c", "command -v jq >/dev/null 2>&1 && echo found || echo gone"],
            capture_output=True,
            text=True,
            env=env,
        )
        if check.stdout.strip() != "gone":
            self.skipTest("could not remove jq from PATH; grep fallback not exercisable")
        proc = self._run("skills/foo/SKILL.md", env=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Canonical Skill Modified: foo", proc.stderr)

    def test_generated_agents_warned(self) -> None:
        proc = self._run(".claude/agents/writer.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Generated Adapter Edited: agents", proc.stderr)
        self.assertIn("--class agents", proc.stderr)

    def test_generated_rules_warned(self) -> None:
        proc = self._run(".claude/rules/engine-code.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Generated Adapter Edited: rules", proc.stderr)

    def test_nested_generated_instruction_warned(self) -> None:
        proc = self._run("docs/CLAUDE.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Generated Adapter Edited: nested-docs", proc.stderr)

    def test_root_generated_instruction_warned(self) -> None:
        proc = self._run("AGENTS.md")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Generated Adapter Edited: root-instructions", proc.stderr)

    def test_codex_native_rules_not_flagged(self) -> None:
        proc = self._run(".codex/rules/default.rules")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stdout, "")
        self.assertEqual(proc.stderr, "")

    def test_codex_apply_patch_generated_agents_emits_json(self) -> None:
        proc = self._run_codex("*** Update File: .codex/agents/writer.toml\n--- a/x\n+++ b/x\n")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["hookSpecificOutput"]["hookEventName"], "PostToolUse")
        ctx = data["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Generated Adapter Edited: agents", ctx)
        self.assertIn("--class agents", ctx)

    def test_jq_present_branch_emits_one_codex_json_document(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env = _env_with_strict_jq_shim(Path(tmp))
            proc = self._run_codex(
                "*** Update File: .codex/agents/writer.toml\n",
                env=env,
            )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn(
            "Generated Adapter Edited: agents",
            data["hookSpecificOutput"]["additionalContext"],
        )

    def test_codex_apply_patch_multi_file(self) -> None:
        command = "*** Add File: .claude/skills/foo/SKILL.md\n*** Update File: src/AGENTS.md\n"
        proc = self._run_codex(command)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ctx = json.loads(proc.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Generated Adapter Edited: foo", ctx)
        self.assertIn("Generated Adapter Edited: nested-src", ctx)

    def test_codex_apply_patch_delete_generated_file_warns(self) -> None:
        proc = self._run_codex("*** Delete File: AGENTS.md\n")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ctx = json.loads(proc.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Generated Adapter Edited: root-instructions", ctx)

    def test_codex_apply_patch_move_target_generated_file_warns(self) -> None:
        proc = self._run_codex(
            "*** Update File: scratch.md\n"
            "*** Move to: .codex/agents/writer.toml\n"
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ctx = json.loads(proc.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Generated Adapter Edited: agents", ctx)

    def test_codex_overlapping_paths_are_deduplicated_exactly(self) -> None:
        proc = self._run_codex(
            "*** Update File: src/AGENTS.md\n"
            "*** Update File: AGENTS.md\n"
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ctx = json.loads(proc.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Generated Adapter Edited: nested-src", ctx)
        self.assertIn("Generated Adapter Edited: root-instructions", ctx)

    def test_absolute_path_instruction_not_silent(self) -> None:
        # Absolute path to a generated instruction must not be silent (plan §570).
        proc = self._run(str(REPO_ROOT / "AGENTS.md"))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Generated Adapter Edited", proc.stderr + proc.stdout)


class ValidateAssetsHookTests(unittest.TestCase):
    """Executes hooks/validate-assets.sh for Claude and Codex payloads."""

    def setUp(self) -> None:
        self.bash = _resolve_git_bash()
        if self.bash is None:
            self.skipTest(
                "no suitable Bash available "
                "(Windows: Git Bash not found, only the WSL launcher present)"
            )
        self.hook = REPO_ROOT / "hooks" / "validate-assets.sh"

    def _run(
        self,
        payload: str,
        env: dict[str, str] | None = None,
        cwd: Path | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [self.bash, self.hook.as_posix()],
            input=payload,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
            cwd=cwd,
        )

    def _run_claude(
        self,
        file_path: str,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return self._run(
            json.dumps({"tool_name": "Write", "tool_input": {"file_path": file_path}}),
            env=env,
        )

    def _run_codex(
        self,
        command: str,
        env: dict[str, str] | None = None,
        cwd: Path | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return self._run(
            json.dumps({"tool_name": "apply_patch", "tool_input": {"command": command}}),
            env=env,
            cwd=cwd,
        )

    def test_claude_file_path_warns_on_bad_asset_name(self) -> None:
        proc = self._run_claude("assets/data/Bad-Name.json")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Asset Validation: Warnings", proc.stderr)
        self.assertIn("Bad-Name.json", proc.stderr)
        self.assertEqual(proc.stdout, "")

    def test_codex_multi_file_apply_patch_emits_json(self) -> None:
        proc = self._run_codex(
            "*** Update File: README.md\n"
            "*** Add File: assets/Bad File.PNG\n"
            "*** Update File: assets/data/also-Bad.json\n"
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["hookSpecificOutput"]["hookEventName"], "PostToolUse")
        context = data["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Bad File.PNG", context)
        self.assertIn("also-Bad.json", context)
        self.assertNotIn("README.md", context)

    def test_codex_overlapping_asset_paths_are_deduplicated_exactly(self) -> None:
        proc = self._run_codex(
            "*** Update File: archive/assets/Bad.png\n"
            "*** Update File: assets/Bad.png\n"
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        context = json.loads(proc.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("archive/assets/Bad.png", context)
        self.assertIn("  NAMING: assets/Bad.png", context)

    def test_codex_apply_patch_move_target_asset_is_validated(self) -> None:
        proc = self._run_codex(
            "*** Update File: README.md\n"
            "*** Move to: assets/Bad-Name.json\n"
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        context = json.loads(proc.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("NAMING: assets/Bad-Name.json", context)

    def test_malformed_and_empty_input_exit_cleanly(self) -> None:
        for payload in ("", "{not valid json"):
            with self.subTest(payload=payload):
                proc = self._run(payload)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertEqual(proc.stdout, "")

    def test_grep_fallback_parses_codex_payload_without_jq(self) -> None:
        env = os.environ.copy()
        jq_exe = shutil.which("jq")
        if jq_exe:
            jq_dirs = {str(Path(jq_exe).resolve().parent).lower()}
            env["PATH"] = os.pathsep.join(
                p for p in env["PATH"].split(os.pathsep)
                if p and str(Path(p).resolve()).lower() not in jq_dirs
            )
        check = subprocess.run(
            [self.bash, "-c", "command -v jq >/dev/null 2>&1 && echo found || echo gone"],
            capture_output=True,
            text=True,
            env=env,
        )
        if check.stdout.strip() != "gone":
            self.skipTest("could not remove jq from PATH; grep fallback not exercisable")

        proc = self._run_codex(
            "*** Update File: assets/data/Bad-Name.json\n",
            env=env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn("Bad-Name.json", data["hookSpecificOutput"]["additionalContext"])

    def test_invalid_json_is_reported_for_both_payloads(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            asset = Path(tmp) / "assets" / "data" / "broken.json"
            asset.parent.mkdir(parents=True)
            asset.write_text("{broken", encoding="utf-8")

            claude = self._run_claude(str(asset))
            self.assertEqual(claude.returncode, 1)
            self.assertIn("FORMAT:", claude.stderr)

            codex = self._run_codex(f"*** Update File: {asset}\n")
            self.assertEqual(codex.returncode, 0, codex.stderr)
            data = json.loads(codex.stdout)
            self.assertEqual(data["decision"], "block")
            self.assertIn("FORMAT:", data["reason"])
            self.assertIn("FORMAT:", data["hookSpecificOutput"]["additionalContext"])

    def test_jq_present_branch_emits_one_codex_block_document(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            asset = root / "assets" / "data" / "broken.json"
            asset.parent.mkdir(parents=True)
            asset.write_text("{broken", encoding="utf-8")
            env = _env_with_strict_jq_shim(root)

            proc = self._run_codex(f"*** Update File: {asset}\n", env=env)

        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["decision"], "block")
        self.assertIn("FORMAT:", data["reason"])

    def test_codex_relative_json_path_resolves_from_git_root_when_cwd_is_nested(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            asset = root / "assets" / "data" / "broken.json"
            asset.parent.mkdir(parents=True)
            asset.write_text("{broken", encoding="utf-8")
            nested = root / "nested"
            nested.mkdir()
            subprocess.run(
                ["git", "init", "--quiet"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            )

            proc = self._run_codex(
                "*** Update File: assets/data/broken.json\n",
                cwd=nested,
            )

            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(proc.stdout)
            self.assertEqual(data["decision"], "block")
            self.assertIn("FORMAT: assets/data/broken.json", data["reason"])


if __name__ == "__main__":
    unittest.main()
