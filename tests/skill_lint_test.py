"""CLI regression tests for skill package Markdown discovery."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINTER = REPO_ROOT / "scripts" / "skill_lint.py"


class SkillLintDirectoryTests(unittest.TestCase):
    def test_skill_package_directory_with_broken_reference_fails_strict_lint(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            package = Path(temp) / "example"
            references = package / "references"
            references.mkdir(parents=True)
            (package / "SKILL.md").write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "argument-hint: none\n"
                "user-invocable: true\n"
                "allowed-tools: Read\n"
                "---\n"
                "# Example\n",
                encoding="utf-8",
            )
            (references / "details.md").write_text("#Broken heading\n", encoding="utf-8")

            for directory, expected_count in ((package, 2), (references, 1)):
                with self.subTest(directory=directory):
                    result = subprocess.run(
                        [sys.executable, str(LINTER), "--strict", str(directory)],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        check=False,
                    )
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertIn("markdown heading missing a space after #", result.stdout)
                    self.assertIn(f"{expected_count} file(s) checked", result.stdout)


if __name__ == "__main__":
    unittest.main()
