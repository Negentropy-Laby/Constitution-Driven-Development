#!/usr/bin/env python3
"""Gate 5 tests: authoring/consumer boundary points at canonical roots.

Part 1 asserts the rewritten canonical skill/agent sources direct authoring at
canonical roots and adapter regeneration (and do not direct writes at generated
paths). Part 2 executes hooks/validate-skill-change.sh with representative JSON
and asserts it classifies canonical vs generated paths correctly. These tests
read the real canonical sources; they do not mutate the repository.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
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


class ValidateSkillChangeHookTests(unittest.TestCase):
    """Executes hooks/validate-skill-change.sh (requires bash)."""

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
        self.hook = REPO_ROOT / "hooks" / "validate-skill-change.sh"

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
            env=env,
        )

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


if __name__ == "__main__":
    unittest.main()
