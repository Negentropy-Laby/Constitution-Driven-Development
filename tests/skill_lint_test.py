"""CLI regression tests for skill package Markdown discovery."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
LINTER = REPO_ROOT / "scripts" / "skill_lint.py"
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import skill_lint as sl  # noqa: E402


class SkillLintDirectoryTests(unittest.TestCase):
    def _run(self, path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(LINTER), "--strict", str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

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
                    result = self._run(directory)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertIn("markdown heading missing a space after #", result.stdout)
                    self.assertIn(f"{expected_count} file(s) checked", result.stdout)

    def test_unrelated_directory_ignores_ordinary_markdown_but_explicit_file_keeps_frontmatter_check(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            ordinary = directory / "README.md"
            ordinary.write_text("#Broken heading\n", encoding="utf-8")
            package = directory / "example"
            package.mkdir()
            (package / "SKILL.md").write_text(
                "---\nname: example\ndescription: Example\nargument-hint: none\n"
                "user-invocable: true\nallowed-tools: Read\n---\n# Example\n",
                encoding="utf-8",
            )
            result = self._run(directory)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("1 file(s) checked", result.stdout)
            self.assertNotIn("README.md", result.stdout)

            explicit = self._run(ordinary)
            self.assertEqual(explicit.returncode, 1, explicit.stdout)
            self.assertIn("missing or unterminated YAML frontmatter", explicit.stdout)

    def test_nested_skill_md_is_not_treated_as_package_entrypoint(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            package = Path(temp) / "example"
            reference = package / "references" / "SKILL.md"
            reference.parent.mkdir(parents=True)
            (package / "SKILL.md").write_text("# Package\n", encoding="utf-8")
            reference.write_text("# Nested reference\n", encoding="utf-8")
            result = self._run(reference)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertNotIn("frontmatter", result.stdout)

    def test_canonical_case_variant_entrypoint_reports_name_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skills = Path(temp) / "skills"
            wrong = skills / "example" / "skill.md"
            wrong.parent.mkdir(parents=True)
            wrong.write_text("# Wrong case\n", encoding="utf-8")
            output = StringIO()
            with mock.patch.object(sl, "SKILLS_DIR", skills), redirect_stdout(output):
                result = sl.main(["--strict", str(skills)])
            self.assertEqual(result, 1)
            self.assertIn("skill entrypoint must be named exactly SKILL.md", output.getvalue())


if __name__ == "__main__":
    unittest.main()
