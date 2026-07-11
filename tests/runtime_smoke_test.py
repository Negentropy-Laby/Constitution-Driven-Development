#!/usr/bin/env python3
"""Credential-free tests for runtime smoke fixture and result contracts."""

from __future__ import annotations

import json
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


class RuntimeResultTests(unittest.TestCase):
    def test_runtime_result_direct_and_claude_wrapper_are_accepted(self) -> None:
        result = {
            "command": "help",
            "skill_loaded": True,
            "write_attempted": False,
            "summary": "Catalog next step reported.",
            "evidence": ["workflow/workflow-catalog.yaml"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, value in (
                ("direct.json", result),
                ("wrapped.json", {"structured_output": result}),
                ("string.json", {"result": json.dumps(result)}),
            ):
                with self.subTest(name=name):
                    path = root / name
                    path.write_text(json.dumps(value), encoding="utf-8")
                    self.assertEqual(rs.validate_result(path, "help"), [])

    def test_runtime_result_write_or_wrong_command_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.json"
            path.write_text(
                json.dumps(
                    {
                        "command": "constitute",
                        "skill_loaded": True,
                        "write_attempted": True,
                        "summary": "bad",
                        "evidence": ["x"],
                    }
                ),
                encoding="utf-8",
            )
            errors = rs.validate_result(path, "help")
            self.assertTrue(any("expected command" in error for error in errors))
            self.assertTrue(any("write" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
