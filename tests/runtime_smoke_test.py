#!/usr/bin/env python3
"""Credential-free tests for runtime discovery and CLI contracts."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import runtime_smoke as rs  # noqa: E402
import sync_adapters as sa  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]


class RuntimeFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = sa.load_manifest(REPO_ROOT / "cdd-manifest.toml")

    def test_runtime_fixture_each_runtime_has_discovery_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for runtime in rs.RUNTIMES:
                with self.subTest(runtime=runtime):
                    fixture = Path(tmp) / runtime
                    rs.prepare_fixture(REPO_ROOT, fixture, runtime)
                    self.assertEqual(rs.validate_fixture(fixture, runtime, self.manifest), [])
                    self.assertFalse((fixture / ".claude" / "settings.json").exists())
                    self.assertFalse((fixture / ".codex" / "hooks.json").exists())

    def test_runtime_fixture_missing_key_skill_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "codex"
            rs.prepare_fixture(REPO_ROOT, fixture, "codex")
            (fixture / ".agents" / "skills" / "help" / "SKILL.md").unlink()
            errors = rs.validate_fixture(fixture, "codex", self.manifest)
            self.assertTrue(any("missing key skill help" in error for error in errors))

    def test_runtime_structural_smoke_is_clean(self) -> None:
        self.assertEqual(rs.structural_errors(REPO_ROOT), [])


class RuntimeCliContractTests(unittest.TestCase):
    def test_runtime_cli_help_with_required_options_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for runtime, required in rs.CLI_HELP_REQUIREMENTS.items():
                with self.subTest(runtime=runtime):
                    path = Path(tmp) / f"{runtime}-help.txt"
                    path.write_text("\n".join(required), encoding="utf-8")
                    self.assertEqual(rs.validate_cli_help(path, runtime), [])

    def test_runtime_cli_help_missing_option_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "claude-help.txt"
            path.write_text("--print\n", encoding="utf-8")
            errors = rs.validate_cli_help(path, "claude")
            self.assertTrue(any("--json-schema" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
