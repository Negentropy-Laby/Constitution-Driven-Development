#!/usr/bin/env python3
"""Gate 6 tests for scripts/workflow_consistency.py.

These tests are read-only against the real repository: they do not mutate any
tracked file. They cover the canonical-root semantic flip and the new
adapter-freshness check added in Gate 6:

  * collect_known_commands() reads the canonical skills/ root.
  * _freshness_findings() maps sync_adapters CheckReport drifts/diagnostics
    into ERROR Findings (using synthetic report objects, no repo mutation).
  * check_generated_adapters_fresh() is clean on a freshly-synced repo.
"""

from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"

# Import workflow_consistency and sync_adapters via sys.path on scripts/.
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import sync_adapters as sa  # noqa: E402
import workflow_consistency as wc  # noqa: E402


class CollectKnownCommandsTest(unittest.TestCase):
    """collect_known_commands() must read the canonical skills/ root."""

    def test_collect_known_commands_reads_canonical(self) -> None:
        commands = wc.collect_known_commands()
        # The catalog is non-empty on a real repo.
        self.assertTrue(commands, "collect_known_commands() should not be empty")
        # gate-check is a core installed skill command.
        self.assertIn("/gate-check", commands)
        # Size must equal the number of canonical skills/*/SKILL.md files.
        expected = {
            "/" + path.parent.name
            for path in (wc.SKILLS_SOURCE.glob("*/SKILL.md"))
            if path.is_file()
        }
        self.assertEqual(commands, expected)


class CodexHookCommandContractTest(unittest.TestCase):
    """Codex hook commands must remain safe when a session starts below root."""

    def test_git_root_resolved_command_is_accepted(self) -> None:
        self.assertTrue(
            wc.is_git_root_resolved_codex_hook_command(
                'bash "$(git rev-parse --show-toplevel)/.codex/hooks/validate-assets.sh"'
            )
        )

    def test_relative_and_embedded_forms_are_rejected(self) -> None:
        for command in (
            "bash .codex/hooks/validate-assets.sh",
            'echo "$(git rev-parse --show-toplevel)/.codex/hooks/validate-assets.sh"',
            'bash "$(git rev-parse --show-toplevel)/.codex/hooks/not-a-script.txt"',
        ):
            with self.subTest(command=command):
                self.assertFalse(wc.is_git_root_resolved_codex_hook_command(command))


class FreshnessMappingTest(unittest.TestCase):
    """_freshness_findings() maps drifts/diagnostics per severity."""

    def test_freshness_mapping(self) -> None:
        # Build a synthetic CheckReport with one drift of each status and one
        # diagnostic of each severity. This does not touch the repository.
        report = sa.CheckReport(
            drifts=[
                sa.Drift(status="OK", path="ok/path"),
                sa.Drift(status="STALE", path="a/stale"),
                sa.Drift(status="MISSING", path="a/missing"),
                sa.Drift(status="EXTRA", path="a/extra"),
                sa.Drift(status="INVALID", path="a/invalid"),
            ],
            diagnostics=[
                sa.Diagnostic(severity="ERROR", path="d/error", message="boom"),
                sa.Diagnostic(severity="WARN", path="d/warn", message="watch out"),
            ],
        )

        findings = wc._freshness_findings(report)

        # Every finding is an ERROR.
        for finding in findings:
            self.assertEqual(finding.severity, "ERROR")

        # OK drift produces nothing; WARN diagnostic produces nothing.
        messages = [finding.message for finding in findings]
        self.assertEqual(len(messages), 5)  # 4 non-OK drifts + 1 ERROR diagnostic

        # Each non-OK drift status is surfaced with the regenerate hint.
        for status_lower in ("stale", "missing", "extra", "invalid"):
            matched = [m for m in messages if m.startswith(f"a/{status_lower} is {status_lower};")]
            self.assertEqual(len(matched), 1, f"expected one {status_lower} drift finding")
            self.assertIn("run python scripts/sync_adapters.py --write", matched[0])

        # The ERROR diagnostic is surfaced as an adapter-generation error.
        error_diag_msgs = [m for m in messages if m.startswith("adapter generation:")]
        self.assertEqual(len(error_diag_msgs), 1)
        self.assertIn("d/error", error_diag_msgs[0])
        self.assertIn("boom", error_diag_msgs[0])

        # WARN diagnostic must NOT appear.
        self.assertFalse(any("watch out" in m for m in messages))
        # OK drift must NOT appear.
        self.assertFalse(any("ok/path" in m for m in messages))

    def test_freshness_mapping_dedups_same_path_error_and_invalid(self) -> None:
        # Regression: sync_adapters.check_plan appends an INVALID drift for a
        # preflight-failed path that ALSO carries an ERROR diagnostic. The
        # consistency layer must surface that path ONCE (the diagnostic, which
        # carries the root-cause message), not twice.
        report = sa.CheckReport(
            drifts=[sa.Drift(status="INVALID", path="p/broken")],
            diagnostics=[
                sa.Diagnostic(
                    severity="ERROR", path="p/broken", message="preflight failed"
                )
            ],
        )
        findings = wc._freshness_findings(report)
        self.assertEqual(len(findings), 1, "same path must surface once, not twice")
        self.assertIn("adapter generation:", findings[0].message)
        self.assertIn("p/broken", findings[0].message)
        self.assertIn("preflight failed", findings[0].message)
        self.assertNotIn("is invalid", findings[0].message)


class FreshnessCheckCleanTest(unittest.TestCase):
    """check_generated_adapters_fresh() must be clean on a fresh repo."""

    def setUp(self) -> None:
        # Ensure the shared manifest context reflects the real repo (another
        # test may have reset or re-pointed it).
        wc.REPO_ROOT = REPO_ROOT
        wc.MANIFEST_PATH = REPO_ROOT / "cdd-manifest.toml"
        wc.reset_manifest_context()

    def test_freshness_check_clean_on_fresh_repo(self) -> None:
        findings = wc.check_generated_adapters_fresh()
        errors = [f for f in findings if f.severity == "ERROR"]
        self.assertEqual(
            errors,
            [],
            f"expected no ERROR findings on a fresh repo, got: {[f.message for f in errors]}",
        )


class ManifestContextTest(unittest.TestCase):
    """The manifest is the single source of truth for canonical roots (ADR-0001)."""

    def setUp(self) -> None:
        self.original_repo_root = wc.REPO_ROOT
        self.original_manifest_path = wc.MANIFEST_PATH
        wc.REPO_ROOT = REPO_ROOT
        wc.MANIFEST_PATH = REPO_ROOT / "cdd-manifest.toml"
        wc.reset_manifest_context()

    def tearDown(self) -> None:
        wc.REPO_ROOT = self.original_repo_root
        wc.MANIFEST_PATH = self.original_manifest_path
        wc.reset_manifest_context()
        wc.get_manifest_context()

    def test_manifest_context_cached_single_load(self) -> None:
        # Multiple consumers share one manifest parse per cache lifetime.
        with mock.patch.object(sa, "load_manifest", wraps=sa.load_manifest) as load:
            ctx1 = wc.get_manifest_context()
            ctx2 = wc.get_manifest_context()
            commands = wc.collect_known_commands()
            findings = wc.check_generated_adapters_fresh()

        self.assertIs(ctx1, ctx2)
        self.assertTrue(commands)
        self.assertEqual(findings, [])
        self.assertEqual(load.call_count, 1)

    def test_roots_derived_from_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            temp_root = Path(td)
            manifest_text = (REPO_ROOT / "cdd-manifest.toml").read_text(
                encoding="utf-8"
            )
            self.assertIn('root = "skills"', manifest_text)
            manifest_text = manifest_text.replace(
                'root = "skills"', 'root = "alternate-skills"', 1
            )
            manifest_path = temp_root / "cdd-manifest.toml"
            manifest_path.write_bytes(manifest_text.encode("utf-8"))
            sample = temp_root / "alternate-skills" / "sample" / "SKILL.md"
            sample.parent.mkdir(parents=True)
            sample.write_bytes(b"---\nname: sample\ndescription: sample\n---\n")

            wc.REPO_ROOT = temp_root
            wc.MANIFEST_PATH = manifest_path
            wc.reset_manifest_context()
            ctx = wc.get_manifest_context()

            self.assertEqual(ctx.repo_root, temp_root)
            self.assertEqual(ctx.roots["skills"], temp_root / "alternate-skills")
            self.assertEqual(
                ctx.roots["root-instructions"], temp_root / "INSTRUCTIONS.md"
            )
            self.assertEqual(wc.SKILLS_SOURCE, ctx.roots["skills"])
            self.assertEqual(wc.AGENTS_SOURCE, ctx.roots["agents"])
            self.assertEqual(wc.HOOKS_SOURCE, ctx.roots["hooks"])
            self.assertEqual(wc.ROOT_INSTRUCTIONS, ctx.roots["root-instructions"])
            self.assertEqual(
                wc.GATE_CHECK, ctx.roots["skills"] / "gate-check" / "SKILL.md"
            )
            self.assertEqual(wc.collect_known_commands(), {"/sample"})

    def test_invalid_manifest_reports_one_error_no_traceback(self) -> None:
        # main() must gate every dependent check behind one clean manifest error.
        with tempfile.TemporaryDirectory() as td:
            bogus = Path(td) / "cdd-manifest.toml"
            bogus.write_bytes(b"this is = = not valid toml [[[\n")
            wc.MANIFEST_PATH = bogus
            wc.reset_manifest_context()
            stdout = io.StringIO()
            with mock.patch.object(sys, "argv", ["workflow_consistency.py"]):
                with contextlib.redirect_stdout(stdout):
                    exit_code = wc.main()

        output = stdout.getvalue()
        self.assertEqual(exit_code, 1)
        self.assertEqual(output.count("ERROR:"), 1, output)
        self.assertIn("manifest load failed; canonical-root checks skipped", output)
        self.assertIn("workflow-consistency summary: 1 error(s), 0 warning(s)", output)
        self.assertNotIn("Traceback", output)


class InitialPushWhitespaceGuardTest(unittest.TestCase):
    """The all-zero-before branch checks a root commit against Git's empty tree."""

    def test_root_commit_trailing_whitespace_is_rejected(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/template-consistency.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn('empty_tree="$(git hash-object -t tree /dev/null)"', workflow)
        self.assertIn('git diff --check "$empty_tree..HEAD"', workflow)
        self.assertNotIn("root commit; nothing to diff", workflow)

        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)

            def git(
                *args: str, input_text: str | None = None
            ) -> subprocess.CompletedProcess[str]:
                return subprocess.run(
                    ["git", "-C", str(repo), *args],
                    input=input_text,
                    capture_output=True,
                    text=True,
                    check=False,
                )

            self.assertEqual(git("init", "--quiet").returncode, 0)
            self.assertEqual(git("config", "user.name", "Whitespace Test").returncode, 0)
            self.assertEqual(
                git("config", "user.email", "whitespace@example.invalid").returncode,
                0,
            )
            (repo / "bad.txt").write_bytes(b"trailing spaces   \n")
            self.assertEqual(git("add", "bad.txt").returncode, 0)
            commit = git("commit", "--quiet", "-m", "root")
            self.assertEqual(commit.returncode, 0, commit.stderr)

            empty_tree = git("hash-object", "-t", "tree", "--stdin", input_text="")
            self.assertEqual(empty_tree.returncode, 0, empty_tree.stderr)
            result = git("diff", "--check", f"{empty_tree.stdout.strip()}..HEAD")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("trailing whitespace", (result.stdout + result.stderr).lower())


if __name__ == "__main__":
    unittest.main()
