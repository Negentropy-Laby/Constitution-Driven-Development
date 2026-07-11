#!/usr/bin/env python3
"""Tests for scripts/sync_adapters.py.

State-independent unit tests build temporary repositories under TemporaryDirectory
and never mutate tracked repository files. Repository-integration tests are
read-only and require the permanent byte-fresh post-Gate-4 state.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import sync_adapters as sa  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]


# ---------------------------------------------------------------------------
# Manifest loading and validation
# ---------------------------------------------------------------------------


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _agent_document(
    name: str = "writer",
    description: str = "The Writer writes.",
    body: str = "You are a Writer.\nDo good work.",
    **fields: str,
) -> str:
    """Return a canonical agent source with one structural trailing LF."""
    frontmatter = {
        "name": name,
        "description": json.dumps(description, ensure_ascii=False),
        "tools": "Read, Write",
        "model": "sonnet",
        "maxTurns": "20",
        "memory": "project",
        "skills": "[a, b]",
        "disallowedTools": "Bash",
        "isolation": "worktree",
    }
    frontmatter.update(fields)
    lines = "\n".join(f"{key}: {value}" for key, value in frontmatter.items())
    return f"---\n{lines}\n---\n{body}\n"


def _context(stem: str = "writer") -> "sa.RenderContext":
    """Build the mandatory transform context used by agent_md_to_toml."""
    return sa.RenderContext(
        source_path=f"agents/{stem}.md",
        relative=f"{stem}.md",
        name=f"{stem}.md",
        stem=stem,
    )


def _valid_manifest_data() -> dict:
    """A complete v2 manifest dict suitable for targeted schema mutations."""
    sources = {
        "skills": {"root": "skills", "include": "*/SKILL.md", "expected_count": 1},
        "agents": {"root": "agents", "include": "*.md", "expected_count": 1},
        "hooks": {"root": "hooks", "include": "*.sh", "expected_count": 1},
        "root-instructions": {"file": "INSTRUCTIONS.md", "expected_count": 1},
    }
    outputs = [
        {"source": "skills", "runtime": "claude", "dest_root": ".claude/skills",
         "dest_pattern": "{relative}", "transforms": [], "owns_tree": True},
        {"source": "skills", "runtime": "codex", "dest_root": ".agents/skills",
         "dest_pattern": "{relative}", "transforms": ["runtime_substitute"], "owns_tree": True},
        {"source": "agents", "runtime": "claude", "dest_root": ".claude/agents",
         "dest_pattern": "{name}", "transforms": [], "owns_tree": True},
        {"source": "agents", "runtime": "codex", "dest_root": ".codex/agents",
         "dest_pattern": "{stem}.toml", "transforms": ["runtime_substitute", "agent_md_to_toml"],
         "owns_tree": True},
        {"source": "hooks", "runtime": "claude", "dest_root": ".claude/hooks",
         "dest_pattern": "{name}", "transforms": [], "owns_tree": True},
        {"source": "hooks", "runtime": "codex", "dest_root": ".codex/hooks",
         "dest_pattern": "{name}", "transforms": [], "owns_tree": True},
        {"source": "root-instructions", "runtime": "claude", "dest_file": "CLAUDE.md",
         "transforms": [], "owns_tree": False},
        {"source": "root-instructions", "runtime": "codex", "dest_file": "AGENTS.md",
         "transforms": ["runtime_substitute"], "owns_tree": False},
    ]
    return {
        "version": 2,
        "runtimes": {"claude": {"label": "Claude Code"}, "codex": {"label": "Codex"}},
        "sources": sources,
        "transforms": {
            "runtime_substitute": {
                "replacements": [["CLAUDE.md", "AGENTS.md"], ["CLAUDE", "Codex"], ["Claude", "Codex"]],
                "forbidden_literals": [".claude/", "CLAUDE", "Claude"],
            }
        },
        "outputs": outputs,
    }


class ManifestTests(unittest.TestCase):
    def test_valid_manifest_loads(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            m = sa.load_manifest(_manifest(root, skills_count=1))
            self.assertEqual(m.version, 2)
            self.assertEqual(m.sources["skills"].expected_count, 1)
            self.assertEqual(len(m.outputs), 8)
            self.assertEqual(len(m.replacements), 3)  # the helper manifest's rule set

    def test_unknown_top_key_rejected(self) -> None:
        with self.assertRaises(ValueError):
            sa._coerce_manifest({"version": 2, "bogus": {}})

    def test_unsupported_version_rejected(self) -> None:
        for bad in (0, 3, "2", 1.0, 2.0, True):
            with self.subTest(version=bad), self.assertRaises(ValueError):
                sa._coerce_manifest({"version": bad})

    def test_v1_manifest_rejected_with_actionable_error(self) -> None:
        with self.assertRaisesRegex(ValueError, r"version 1 is unsupported.*UPGRADING"):
            sa._coerce_manifest({"version": 1})

    def test_source_id_must_match_pattern(self) -> None:
        data = _valid_manifest_data()
        data["sources"]["Bad_Source"] = data["sources"].pop("hooks")
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_source_id_all_is_reserved_for_cli_selector(self) -> None:
        data = _valid_manifest_data()
        data["sources"]["all"] = data["sources"].pop("hooks")
        for output in data["outputs"]:
            if output["source"] == "hooks":
                output["source"] = "all"
        with self.assertRaisesRegex(ValueError, "reserved"):
            sa._coerce_manifest(data)

    def test_requires_one_output_per_declared_source_target(self) -> None:
        data = _valid_manifest_data()
        data["outputs"].pop()
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_runtimes_required_and_validated(self) -> None:
        # No runtimes -> rejected.
        data = _valid_manifest_data()
        data.pop("runtimes")
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)
        # Bad runtime id -> rejected.
        data = _valid_manifest_data()
        data["runtimes"]["BadRuntime"] = data["runtimes"].pop("codex")
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_asymmetric_targets_supported(self) -> None:
        # A source may target a subset of runtimes; outputs must match exactly.
        data = _valid_manifest_data()
        data["sources"]["hooks"]["targets"] = ["claude"]
        # Remove the codex hooks output to match the declared target.
        data["outputs"] = [o for o in data["outputs"] if not (o["source"] == "hooks" and o["runtime"] == "codex")]
        m = sa._coerce_manifest(data)  # should not raise
        self.assertEqual(m.sources["hooks"].targets, ("claude",))

    def test_output_must_declare_exactly_one_dest_form(self) -> None:
        data = _valid_manifest_data()
        data["outputs"][0]["dest_file"] = "x"
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_file_output_rejects_dest_pattern_even_when_ignored_by_shape(self) -> None:
        data = _valid_manifest_data()
        root_output = next(
            output for output in data["outputs"]
            if output["source"] == "root-instructions" and output["runtime"] == "claude"
        )
        root_output["dest_pattern"] = "../../ignored"
        with self.assertRaisesRegex(ValueError, "must not declare dest_pattern"):
            sa._coerce_manifest(data)

    def test_expected_count_must_be_positive_non_bool_int(self) -> None:
        for bad in (0, -1, True, 1.5, "1"):
            data = _valid_manifest_data()
            data["sources"]["skills"]["expected_count"] = bad
            with self.subTest(value=bad), self.assertRaises(ValueError):
                sa._coerce_manifest(data)

    def test_single_file_source_count_must_equal_one(self) -> None:
        data = _valid_manifest_data()
        data["sources"]["root-instructions"]["expected_count"] = 2
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_owns_tree_must_be_real_bool(self) -> None:
        for bad in (0, 1, "true", None, []):
            data = _valid_manifest_data()
            data["outputs"][0]["owns_tree"] = bad
            with self.subTest(value=bad), self.assertRaises(ValueError):
                sa._coerce_manifest(data)

    def test_all_path_and_pattern_fields_must_be_strings(self) -> None:
        mutations = (
            ("skills", "root", 7),
            ("skills", "include", ["*/SKILL.md"]),
            ("root-instructions", "file", 7),
        )
        for source, key, bad in mutations:
            data = _valid_manifest_data()
            data["sources"][source][key] = bad
            with self.subTest(source=source, field=key), self.assertRaises(ValueError):
                sa._coerce_manifest(data)

    def test_unknown_nested_keys_and_bad_transform_types_rejected(self) -> None:
        mutations = []
        data = _valid_manifest_data()
        data["sources"]["skills"]["bogus"] = True
        mutations.append(data)
        data = _valid_manifest_data()
        data["outputs"][0]["bogus"] = True
        mutations.append(data)
        data = _valid_manifest_data()
        data["outputs"][0]["transforms"] = "runtime_substitute"
        mutations.append(data)
        data = _valid_manifest_data()
        data["outputs"][0]["transforms"] = [7]
        mutations.append(data)
        data = _valid_manifest_data()
        data["outputs"][0]["source"] = 7
        mutations.append(data)
        data = _valid_manifest_data()
        data["outputs"][0]["runtime"] = 7
        mutations.append(data)
        data = _valid_manifest_data()
        data["transforms"]["runtime_substitute"]["replacements"] = [["one"]]
        mutations.append(data)
        data = _valid_manifest_data()
        data["transforms"]["runtime_substitute"]["replacements"] = [["one", 7]]
        mutations.append(data)
        data = _valid_manifest_data()
        data["transforms"]["runtime_substitute"]["forbidden_literals"] = "Claude"
        mutations.append(data)
        data = _valid_manifest_data()
        data["transforms"]["runtime_substitute"]["forbidden_literals"] = [7]
        mutations.append(data)
        for index, invalid in enumerate(mutations):
            with self.subTest(index=index), self.assertRaises(ValueError):
                sa._coerce_manifest(invalid)
        for key in ("dest_root", "dest_pattern"):
            data = _valid_manifest_data()
            data["outputs"][0][key] = 7
            with self.subTest(field=key), self.assertRaises(ValueError):
                sa._coerce_manifest(data)
        data = _valid_manifest_data()
        data["outputs"][6]["dest_file"] = 7
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_source_destination_exact_or_ancestor_overlap_rejected(self) -> None:
        for source_root in (".claude/skills", ".claude", ".claude/skills/nested"):
            data = _valid_manifest_data()
            data["sources"]["skills"]["root"] = source_root
            with self.subTest(root=source_root), self.assertRaises(ValueError):
                sa._coerce_manifest(data)

    def test_source_destination_casefold_overlap_rejected(self) -> None:
        data = _valid_manifest_data()
        data["sources"]["skills"]["root"] = ".CLAUDE/SKILLS"
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_overlapping_managed_roots_rejected(self) -> None:
        data = _valid_manifest_data()
        data["outputs"][2]["dest_root"] = ".claude/skills/nested"
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)

    def test_casefold_destination_collision_rejected(self) -> None:
        data = _valid_manifest_data()
        data["outputs"][2]["dest_root"] = ".CLAUDE/SKILLS"
        with self.assertRaises(ValueError):
            sa._coerce_manifest(data)


class PathSafetyTests(unittest.TestCase):
    def test_platform_independent_unsafe_paths_rejected(self) -> None:
        bad_paths = (
            "", ".", "..", "../x", "x/../y", "./x", "x/./y", "x//y",
            "/abs/path", "//server/share", "C:/drive/path", "C:\\drive\\path",
            "a\\b", "a\x00b", "writer.toml:payload",
        )
        for bad in bad_paths:
            with self.subTest(path=bad), self.assertRaises(ValueError):
                sa._validate_posix_rel(bad, "x")

    def test_safe_glob_is_accepted_but_escaping_glob_is_rejected(self) -> None:
        data = _valid_manifest_data()
        data["sources"]["skills"]["include"] = "**/SKILL*.md"
        sa._coerce_manifest(data)
        for bad in ("../*.md", "a/../../*.md", "/abs/*.md", "C:/*.md", "a\\*.md", "a//*.md"):
            data = _valid_manifest_data()
            data["sources"]["skills"]["include"] = bad
            with self.subTest(pattern=bad), self.assertRaises(ValueError):
                sa._coerce_manifest(data)

    def test_dest_pattern_placeholder_and_traversal_validation(self) -> None:
        for bad in (
            "../{name}", "x/{bogus}", "x/{name", "x/name}", "/{name}",
            "C:/{name}", "x\\{name}", "{name!r}", "{name:>10}",
        ):
            data = _valid_manifest_data()
            data["outputs"][0]["dest_pattern"] = bad
            with self.subTest(pattern=bad), self.assertRaises(ValueError):
                sa._coerce_manifest(data)

    def test_rendered_exact_collision_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "skills" / "b" / "SKILL.md", "---\nname: b\n---\n# B\n")
            path = _manifest(root, skills_count=2)
            data = sa.tomllib.loads(path.read_text(encoding="utf-8"))
            for output in data["outputs"]:
                if output["source"] == "skills":
                    output["dest_pattern"] = "same/SKILL.md"
            manifest = sa._coerce_manifest(data)
            plan = sa.build_sync_plan(manifest, root, "skills")
            collisions = [
                d for d in plan.diagnostics
                if d.severity == sa.ERROR and "rendered destination collides" in d.message
            ]
            self.assertEqual(len(collisions), 2)
            report = sa.check_plan(plan)
            self.assertFalse(report.ok)
            self.assertGreater(report.counts()[sa.INVALID], 0)
            self.assertFalse((root / ".claude").exists())
            self.assertFalse((root / ".agents").exists())

    def test_windows_reparse_attribute_is_linklike_without_following(self) -> None:
        fake_stat = mock.Mock(st_mode=0, st_file_attributes=sa.FILE_ATTRIBUTE_REPARSE_POINT)
        self.assertTrue(sa._is_linklike_stat(fake_stat))

    def test_rendered_casefold_and_file_ancestor_collisions_rejected(self) -> None:
        manifest = sa._coerce_manifest(_valid_manifest_data())
        collision_sets = (
            ("generated/Foo.toml", "generated/foo.toml"),
            ("generated/agent", "generated/agent/child.toml"),
        )
        for left, right in collision_sets:
            with self.subTest(left=left, right=right), tempfile.TemporaryDirectory() as tmp:
                plan = sa.SyncPlan(manifest, Path(tmp), "agents")
                plan.rendered = [
                    sa.RenderedOutput(left, b"left\n", True),
                    sa.RenderedOutput(right, b"right\n", True),
                ]
                sa._validate_rendered_graph(plan)
                self.assertTrue(any(d.severity == sa.ERROR and "collid" in d.message
                                    for d in plan.diagnostics))


# ---------------------------------------------------------------------------
# Transforms
# ---------------------------------------------------------------------------


class SubstitutionTests(unittest.TestCase):
    def setUp(self) -> None:
        # Real manifest replacements + forbidden literals.
        self.reps = (
            (".claude/skills/", ".agents/skills/"),
            (".claude/agents/", ".codex/agents/"),
            ("Claude Code", "Codex"),
            ("CLAUDE.md", "AGENTS.md"),
            ("CLAUDE", "Codex"),
            ("Claude", "Codex"),
        )
        self.forb = (".claude/", ".claude\\", "CLAUDE", "Claude")

    def test_ordering_claude_md_before_bare_claude(self) -> None:
        out = sa._runtime_substitute("Read CLAUDE.md and the CLAUDE/version.", self.reps, self.forb)
        self.assertEqual(out, "Read AGENTS.md and the Codex/version.")

    def test_ordering_claude_code_before_bare_claude(self) -> None:
        out = sa._runtime_substitute("Use Claude Code, not plain Claude.", self.reps, self.forb)
        self.assertEqual(out, "Use Codex, not plain Codex.")

    def test_path_substitution(self) -> None:
        out = sa._runtime_substitute("See .claude/skills/help/ and .claude/agents/x.md", self.reps, self.forb)
        self.assertEqual(out, "See .agents/skills/help/ and .codex/agents/x.md")

    def test_all_six_rules_apply_in_declared_order(self) -> None:
        source = (
            ".claude/skills/a .claude/agents/b.md Claude Code CLAUDE.md "
            "CLAUDE/version Claude"
        )
        expected = (
            ".agents/skills/a .codex/agents/b.md Codex AGENTS.md "
            "Codex/version Codex"
        )
        self.assertEqual(sa._runtime_substitute(source, self.reps, self.forb), expected)

    def test_forbidden_residual_is_error(self) -> None:
        # Bare "Claude" survives if replacements do not cover it.
        with self.assertRaises(sa.SubstitutionError):
            sa._runtime_substitute("Claude", (), self.forb)

    def test_real_setup_engine_prose_collapses_and_is_rejected(self) -> None:
        # Regression for the original P0 bug: the exact canonical sentence from
        # skills/setup-engine/SKILL.md, run through the real pipeline, must raise.
        canonical = (
            "regenerates the runtime root-instruction files "
            "(`CLAUDE.md` and `AGENTS.md`)"
        )
        with self.assertRaises(sa.SubstitutionError) as ctx:
            sa._runtime_substitute(canonical, self.reps, self.forb)
        self.assertIn("collapse", str(ctx.exception))

    def test_real_skill_improve_prose_collapses_and_is_rejected(self) -> None:
        canonical = (
            "regenerates the runtime adapters "
            "(`.claude/skills/[name]/SKILL.md` and "
            "`.agents/skills/[name]/SKILL.md`)"
        )
        with self.assertRaises(sa.SubstitutionError):
            sa._runtime_substitute(canonical, self.reps, self.forb)

    def test_runtime_name_doubling_is_rejected(self) -> None:
        # "Claude Code and Claude Code" -> "Codex and Codex" through the real
        # pipeline; the doubled "Codex" target token is flagged.
        with self.assertRaises(sa.SubstitutionError):
            sa._runtime_substitute("use Claude Code and Claude Code here", self.reps, self.forb)

    def test_connector_variants_are_rejected(self) -> None:
        for connector in ("and", "or", ","):
            with self.subTest(connector=connector):
                with self.assertRaises(sa.SubstitutionError):
                    sa._runtime_substitute(
                        f"see `CLAUDE.md` {connector} `CLAUDE.md`", self.reps, self.forb
                    )

    def test_pre_existing_non_target_repetition_passes(self) -> None:
        # Repeating a path that is NOT a substitution target is not a collapse the
        # transform could introduce, so it must be allowed (regression for the
        # legitimate same-path-twice prose in skills such as gate-check).
        out = sa._runtime_substitute(
            "update memory_bank/t3_archive/gate_runs/ and "
            "memory_bank/t3_archive/gate_runs/ if needed",
            self.reps,
            self.forb,
        )
        self.assertIn("memory_bank", out)

    def test_pre_existing_target_repetition_passes(self) -> None:
        out = sa._runtime_substitute(
            "Compare Codex and Codex behavior.",
            self.reps,
            self.forb,
        )
        self.assertEqual(out, "Compare Codex and Codex behavior.")

    def test_parenthesized_distinct_tokens_collapse_is_rejected(self) -> None:
        with self.assertRaises(sa.SubstitutionError):
            sa._runtime_substitute(
                "Compare (CLAUDE.md) and (AGENTS.md).",
                self.reps,
                self.forb,
            )

    def test_comma_conjunction_distinct_tokens_collapse_is_rejected(self) -> None:
        for connector in (", and", ", or"):
            with self.subTest(connector=connector), self.assertRaises(sa.SubstitutionError):
                sa._runtime_substitute(
                    f"Compare CLAUDE.md{connector} AGENTS.md.",
                    self.reps,
                    self.forb,
                )

    def test_legitimate_non_adjacent_repetition_passes(self) -> None:
        out = sa._runtime_substitute(
            "Read AGENTS.md first. Later, read AGENTS.md again.", self.reps, self.forb
        )
        self.assertIn("AGENTS.md", out)

    def test_distinct_adjacent_filenames_pass(self) -> None:
        # Different tokens across a connector are fine; only substitution-made
        # identical tokens collapse.
        out = sa._runtime_substitute(
            "regenerates (`CLAUDE.md` and `different.md`)", self.reps, self.forb
        )
        self.assertIn("AGENTS.md", out)

    def test_second_token_with_target_prefix_passes(self) -> None:
        out = sa._runtime_substitute(
            "Use Claude Code and Claude Code-generated output.",
            self.reps,
            self.forb,
        )
        self.assertEqual(out, "Use Codex and Codex-generated output.")

    def test_transform_cannot_introduce_bom_or_cr_into_rendered_output(self) -> None:
        for label, replacement in (("bom", "\ufeffCodex"), ("cr", "Codex\r")):
            with self.subTest(label=label), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write(root / "skills" / "a" / "SKILL.md", "Claude\n")
                data = _valid_manifest_data()
                data["transforms"]["runtime_substitute"] = {
                    "replacements": [["Claude", replacement]],
                    "forbidden_literals": [],
                }
                manifest = sa._coerce_manifest(data)
                plan = sa.build_sync_plan(manifest, root, "skills")
                self.assertTrue(
                    any(d.severity == sa.ERROR and "transform failed" in d.message
                        for d in plan.diagnostics),
                    plan.diagnostics,
                )
                report = sa.apply_plan(plan)
                self.assertFalse(report.ok)
                self.assertGreater(report.counts()[sa.INVALID], 0)
                self.assertFalse((root / ".claude").exists())
                self.assertFalse((root / ".agents").exists())


class AgentTransformTests(unittest.TestCase):
    def test_drops_known_operational_fields(self) -> None:
        toml = sa._agent_md_to_toml(_agent_document(), _context())
        parsed = sa.tomllib.loads(toml)
        self.assertEqual(set(parsed), {"name", "description", "developer_instructions"})
        self.assertEqual(parsed["name"], "writer")

    def test_unknown_field_fails(self) -> None:
        with self.assertRaises(ValueError):
            sa._agent_md_to_toml(_agent_document(newFutureField="oops"), _context())

    def test_name_must_match_source_stem(self) -> None:
        with self.assertRaises(ValueError):
            sa._agent_md_to_toml(_agent_document(name="other"), _context("writer"))

    def test_bad_name_pattern_fails(self) -> None:
        with self.assertRaises(ValueError):
            sa._agent_md_to_toml(_agent_document(name="Bad_Name"), _context("Bad_Name"))

    def test_quoted_description_round_trips(self) -> None:
        toml = sa._agent_md_to_toml(_agent_document(description='She said "hi"'), _context())
        parsed = sa.tomllib.loads(toml)
        self.assertEqual(parsed["description"], 'She said "hi"')

    def test_empty_description_fails(self) -> None:
        with self.assertRaises(ValueError):
            sa._agent_md_to_toml(_agent_document(description=""), _context())

    def test_body_boundary_single_trailing_lf_removed(self) -> None:
        toml = sa._agent_md_to_toml(_agent_document(), _context())
        parsed = sa.tomllib.loads(toml)
        # Body had exactly one terminating LF; value has no trailing newline.
        self.assertEqual(parsed["developer_instructions"], "You are a Writer.\nDo good work.")

    def test_body_extra_trailing_lf_preserved_as_semantic(self) -> None:
        # Two trailing LFs: one file terminator (removed), one semantic (kept).
        agent = "---\nname: writer\ndescription: \"d\"\n---\nBody line\n\n"
        parsed = sa.tomllib.loads(sa._agent_md_to_toml(agent, _context()))
        self.assertEqual(parsed["developer_instructions"], "Body line\n")

    def test_unterminated_frontmatter_fails(self) -> None:
        with self.assertRaises(ValueError):
            sa._agent_md_to_toml("---\nname: writer\n", _context())

    def test_duplicate_field_fails(self) -> None:
        with self.assertRaises(ValueError):
            sa._agent_md_to_toml(
                "---\nname: writer\nname: writer\ndescription: \"d\"\n---\nbody\n",
                _context(),
            )

    def test_backslash_in_body_escaped_and_round_trips(self) -> None:
        # Body contains a literal backslash-n (two chars); it must survive TOML encoding.
        agent = "---\nname: writer\ndescription: \"d\"\n---\nUse \\n for newline.\n"
        parsed = sa.tomllib.loads(sa._agent_md_to_toml(agent, _context()))
        self.assertEqual(parsed["developer_instructions"], "Use \\n for newline.")

    def test_toml_corpus_round_trips_exact_values(self) -> None:
        bodies = (
            "plain",
            'She said """hello""" and then """" four quotes',
            r"Windows-like C:\\temp\\file and literal \\n",
            "tabs\tbackspace\bformfeed\fcontrols:\x01\x1f",
            "中文、emoji 😀、combining e\u0301",
            "no structural boundary ambiguity",
            "semantic trailing LF\n",
            "line one\nline two\nline three",
        )
        descriptions = (
            "normal",
            'quotes: "hi" and backslash: \\',
            "中文 😀 tab:\t control:\u0001",
        )
        for index, body in enumerate(bodies):
            description = descriptions[index % len(descriptions)]
            with self.subTest(index=index):
                source = _agent_document(description=description, body=body)
                rendered = sa._agent_md_to_toml(source, _context())
                parsed = sa.tomllib.loads(rendered)
                self.assertEqual(parsed["name"], "writer")
                self.assertEqual(parsed["description"], description)
                self.assertEqual(parsed["developer_instructions"], body)

    def test_optional_structural_leading_lf_is_removed(self) -> None:
        source = "---\nname: writer\ndescription: \"d\"\n---\n\nBody\n"
        parsed = sa.tomllib.loads(sa._agent_md_to_toml(source, _context()))
        self.assertEqual(parsed["developer_instructions"], "Body")


# ---------------------------------------------------------------------------
# Freshness + write mechanics (temp repositories)
# ---------------------------------------------------------------------------


def _manifest(
    root: Path,
    skills_count: int = 1,
    agents_count: int = 1,
    hooks_count: int = 1,
) -> Path:
    """Write a minimal but realistic manifest covering all four classes."""
    path = root / "cdd-manifest.toml"
    write(path, (
        "version = 2\n"
        '[runtimes.claude]\nlabel = "Claude Code"\n'
        '[runtimes.codex]\nlabel = "Codex"\n'
        f'[sources.skills]\nroot = "skills"\ninclude = "*/SKILL.md"\nexpected_count = {skills_count}\n'
        f'[sources.agents]\nroot = "agents"\ninclude = "*.md"\nexpected_count = {agents_count}\n'
        f'[sources.hooks]\nroot = "hooks"\ninclude = "*.sh"\nexpected_count = {hooks_count}\n'
        '[sources.root-instructions]\nfile = "INSTRUCTIONS.md"\nexpected_count = 1\n'
        '[transforms.runtime_substitute]\nreplacements = [["CLAUDE.md", "AGENTS.md"], ["CLAUDE", "AGENTS"], ["Claude", "Codex"]]\n'
        'forbidden_literals = [".claude/", "CLAUDE", "Claude"]\n'
        '[[outputs]]\nsource = "skills"\nruntime = "claude"\ndest_root = ".claude/skills"\ndest_pattern = "{relative}"\ntransforms = []\nowns_tree = true\n'
        '[[outputs]]\nsource = "skills"\nruntime = "codex"\ndest_root = ".agents/skills"\ndest_pattern = "{relative}"\ntransforms = ["runtime_substitute"]\nowns_tree = true\n'
        '[[outputs]]\nsource = "agents"\nruntime = "claude"\ndest_root = ".claude/agents"\ndest_pattern = "{name}"\ntransforms = []\nowns_tree = true\n'
        '[[outputs]]\nsource = "agents"\nruntime = "codex"\ndest_root = ".codex/agents"\ndest_pattern = "{stem}.toml"\ntransforms = ["runtime_substitute", "agent_md_to_toml"]\nowns_tree = true\n'
        '[[outputs]]\nsource = "hooks"\nruntime = "claude"\ndest_root = ".claude/hooks"\ndest_pattern = "{name}"\ntransforms = []\nowns_tree = true\n'
        '[[outputs]]\nsource = "hooks"\nruntime = "codex"\ndest_root = ".codex/hooks"\ndest_pattern = "{name}"\ntransforms = []\nowns_tree = true\n'
        '[[outputs]]\nsource = "root-instructions"\nruntime = "claude"\ndest_file = "CLAUDE.md"\ntransforms = []\nowns_tree = false\n'
        '[[outputs]]\nsource = "root-instructions"\nruntime = "codex"\ndest_file = "AGENTS.md"\ntransforms = []\nowns_tree = false\n'
    ))
    # Seed unrelated source classes so an all-class plan remains valid. Tests
    # that target count/discovery behavior create their target class explicitly.
    (root / "agents").mkdir(exist_ok=True)
    (root / "hooks").mkdir(exist_ok=True)
    if agents_count == 1 and not any((root / "agents").glob("*.md")):
        write(root / "agents" / "writer.md", _agent_document())
    if hooks_count == 1 and not any((root / "hooks").glob("*.sh")):
        write(root / "hooks" / "validate.sh", "#!/usr/bin/env bash\nexit 0\n")
    if not (root / "INSTRUCTIONS.md").exists():
        write(root / "INSTRUCTIONS.md", "# Root\n")
    return path


class FreshnessTests(unittest.TestCase):
    def test_check_is_read_only_and_reports_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "INSTRUCTIONS.md", "# Root\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root)
            report = sa.check_plan(plan)
            self.assertFalse(report.ok)
            statuses = {d.path: d.status for d in report.drifts}
            self.assertEqual(statuses[".claude/skills/a/SKILL.md"], sa.MISSING)
            self.assertEqual(statuses["CLAUDE.md"], sa.MISSING)

    def test_write_then_check_ok(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "INSTRUCTIONS.md", "# Root\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root)
            self.assertTrue(sa.apply_plan(plan).ok)
            self.assertTrue(sa.check_plan(plan).ok)

    def test_extra_orphan_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "INSTRUCTIONS.md", "# Root\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root)
            sa.apply_plan(plan)
            write(root / ".claude" / "skills" / "orphan" / "SKILL.md", "stale\n")
            report = sa.check_plan(plan)
            statuses = {d.path: d.status for d in report.drifts}
            self.assertEqual(statuses[".claude/skills/orphan/SKILL.md"], sa.EXTRA)
            self.assertTrue(sa.apply_plan(plan).ok)
            self.assertFalse((root / ".claude" / "skills" / "orphan").exists())

    def test_empty_orphan_directory_detected_and_pruned(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertTrue(sa.apply_plan(plan).ok)
            orphan = root / ".claude" / "skills" / "empty-orphan"
            orphan.mkdir()
            report = sa.check_plan(plan)
            self.assertTrue(any(d.status == sa.EXTRA and "empty-orphan" in d.path for d in report.drifts))
            self.assertTrue(sa.apply_plan(plan).ok)
            self.assertFalse(orphan.exists())

    def test_stale_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "INSTRUCTIONS.md", "# Root\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root)
            sa.apply_plan(plan)
            # Corrupt the generated output; the plan's expected (from the source) is unchanged.
            write(root / ".claude" / "skills" / "a" / "SKILL.md", "tampered\n")
            report = sa.check_plan(plan)
            statuses = {d.path: d.status for d in report.drifts}
            self.assertEqual(statuses[".claude/skills/a/SKILL.md"], sa.STALE)

    def test_count_mismatch_blocks_and_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            # expected_count = 2 but only 1 exists -> blocking preflight.
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=2)), root)
            report = sa.check_plan(plan)
            self.assertTrue(any(d.severity == sa.ERROR for d in report.diagnostics))
            # apply must not write anything when preflight fails
            applied = sa.apply_plan(plan)
            self.assertFalse(applied.ok)
            self.assertFalse((root / ".claude").exists())
            self.assertFalse((root / ".agents").exists())

    def test_zero_source_match_is_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills").mkdir()
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root, "skills")
            report = sa.check_plan(plan)
            self.assertFalse(report.ok)
            self.assertTrue(any(d.severity == sa.ERROR for d in report.diagnostics))
            sa.apply_plan(plan)
            self.assertFalse((root / ".claude").exists())

    def test_rename_source_without_count_update_is_missing_and_extra(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "INSTRUCTIONS.md", "# Root\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root)
            sa.apply_plan(plan)
            # Rename the canonical skill but keep expected_count=1: old output orphan, new missing.
            (root / "skills" / "a" / "SKILL.md").unlink()
            (root / "skills" / "a").rmdir()
            write(root / "skills" / "b" / "SKILL.md", "---\nname: b\n---\n# B\n")
            report = sa.check_plan(sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root))
            statuses = {d.path: d.status for d in report.drifts}
            self.assertEqual(statuses[".claude/skills/b/SKILL.md"], sa.MISSING)
            self.assertEqual(statuses[".claude/skills/a/SKILL.md"], sa.EXTRA)
            self.assertTrue(sa.apply_plan(
                sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root, "skills")
            ).ok)
            self.assertFalse((root / ".claude" / "skills" / "a").exists())

    def test_generated_crlf_bom_and_invalid_utf8_are_repairable_stale(self) -> None:
        variants = {
            "crlf": b"---\r\nname: a\r\n---\r\n# A\r\n",
            "bom": b"\xef\xbb\xbf---\nname: a\n---\n# A\n",
            "invalid-utf8": b"\xff\xfe",
        }
        for label, bad_bytes in variants.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                canonical = b"---\nname: a\n---\n# A\n"
                (root / "skills" / "a").mkdir(parents=True)
                (root / "skills" / "a" / "SKILL.md").write_bytes(canonical)
                plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
                self.assertTrue(sa.apply_plan(plan).ok)
                target = root / ".claude" / "skills" / "a" / "SKILL.md"
                target.write_bytes(bad_bytes)
                report = sa.check_plan(plan)
                drift = next(d for d in report.drifts if d.path == ".claude/skills/a/SKILL.md")
                self.assertEqual(drift.status, sa.STALE)
                self.assertTrue(sa.apply_plan(plan).ok)
                self.assertEqual(target.read_bytes(), canonical)

    def test_expected_path_directory_is_invalid_and_blocks_all_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            bad = root / ".claude" / "skills" / "a" / "SKILL.md"
            write(bad / "sentinel.txt", "keep\n")
            report = sa.check_plan(plan)
            self.assertTrue(any(d.status == sa.INVALID and d.path.endswith("SKILL.md") for d in report.drifts))
            applied = sa.apply_plan(plan)
            self.assertFalse(applied.ok)
            self.assertEqual((bad / "sentinel.txt").read_text(encoding="utf-8"), "keep\n")
            self.assertFalse((root / ".agents").exists())

    def test_invalid_preflight_blocks_stale_write_and_extra_prune_together(self) -> None:
        def snapshot(root: Path) -> dict[str, tuple[int, int, bytes | None]]:
            state: dict[str, tuple[int, int, bytes | None]] = {}
            for base in (root / ".agents", root / ".claude"):
                for path in sorted(base.rglob("*")):
                    st = path.lstat()
                    payload = path.read_bytes() if path.is_file() else None
                    state[path.relative_to(root).as_posix()] = (
                        st.st_mode, st.st_mtime_ns, payload
                    )
            return state

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            canonical = root / "skills" / "a" / "SKILL.md"
            write(canonical, "---\nname: a\n---\n# A\n")
            manifest = sa.load_manifest(_manifest(root))
            self.assertTrue(sa.apply_plan(sa.build_sync_plan(manifest, root, "skills")).ok)
            write(canonical, "---\nname: a\n---\n# Changed\n")
            write(root / ".agents" / "skills" / "orphan.txt", "must not prune\n")
            invalid = root / ".claude" / "skills" / "a" / "SKILL.md"
            invalid.unlink()
            write(invalid / "sentinel.txt", "must not replace\n")
            before = snapshot(root)
            report = sa.apply_plan(sa.build_sync_plan(manifest, root, "skills"))
            self.assertFalse(report.ok)
            self.assertTrue(any(d.status == sa.INVALID for d in report.drifts))
            self.assertEqual(snapshot(root), before)

    def test_file_in_expected_parent_chain_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / ".claude" / "skills", "parent is a file\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            report = sa.check_plan(plan)
            self.assertTrue(any(d.status == sa.INVALID for d in report.drifts))
            self.assertFalse(sa.apply_plan(plan).ok)
            self.assertEqual((root / ".claude" / "skills").read_text(encoding="utf-8"), "parent is a file\n")

    def test_class_isolation_does_not_scan_or_modify_other_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            sentinel = root / ".codex" / "agents" / "sentinel.toml"
            write(sentinel, "do not touch\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertTrue(sa.apply_plan(plan).ok)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "do not touch\n")

    def test_rogue_skill_directory_without_skill_md_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "skills" / "rogue" / "README.md", "rogue\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertFalse(sa.check_plan(plan).ok)
            self.assertTrue(any("rogue" in d.path for d in plan.diagnostics))
            sa.apply_plan(plan)
            self.assertFalse((root / ".claude").exists())

    def test_extra_file_in_skill_package_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "skills" / "a" / "notes.txt", "not allowed\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertFalse(sa.check_plan(plan).ok)
            self.assertTrue(any(d.path.endswith("notes.txt") for d in plan.diagnostics))

    def test_agent_name_stem_mismatch_blocks_render(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "agents" / "writer.md", _agent_document(name="other"))
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "agents")
            report = sa.check_plan(plan)
            self.assertFalse(report.ok)
            self.assertTrue(any("stem" in d.message or "name" in d.message for d in report.diagnostics))

    def _make_symlink_or_skip(self, link: Path, target: Path, *, target_is_directory: bool = False) -> None:
        try:
            link.parent.mkdir(parents=True, exist_ok=True)
            link.symlink_to(target, target_is_directory=target_is_directory)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"symlink capability unavailable: {exc}")

    def test_source_symlink_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            external = root / "external.md"
            write(external, "---\nname: a\n---\n# A\n")
            link = root / "skills" / "a" / "SKILL.md"
            self._make_symlink_or_skip(link, external)
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertFalse(sa.check_plan(plan).ok)
            self.assertTrue(any("link" in d.message.lower() for d in plan.diagnostics))

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO requires POSIX")
    def test_special_file_in_managed_root_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertTrue(sa.apply_plan(plan).ok)
            fifo = root / ".claude" / "skills" / "unexpected.fifo"
            os.mkfifo(fifo)
            report = sa.check_plan(plan)
            self.assertTrue(any(d.status == sa.INVALID and d.path.endswith("unexpected.fifo") for d in report.drifts))


class WriteMechanicsTests(unittest.TestCase):
    def test_write_is_idempotent_and_mtime_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "INSTRUCTIONS.md", "# Root\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root)
            sa.apply_plan(plan)
            target = root / ".claude" / "skills" / "a" / "SKILL.md"
            mtime_before = target.stat().st_mtime_ns
            sa.apply_plan(plan)  # second write should be a no-op for unchanged files
            self.assertEqual(target.stat().st_mtime_ns, mtime_before)

    @unittest.skipUnless(os.name != "nt", "POSIX mode contract")
    def test_generated_mode_is_exactly_0644(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "INSTRUCTIONS.md", "# Root\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root, skills_count=1)), root)
            sa.apply_plan(plan)
            mode = (root / ".claude" / "skills" / "a" / "SKILL.md").stat().st_mode & 0o777
            self.assertEqual(mode, 0o644)

    @unittest.skipUnless(os.name != "nt", "POSIX mode contract")
    def test_mode_only_repair_preserves_bytes_and_mtime(self) -> None:
        for bad_mode in (0o600, 0o664, 0o755):
            with self.subTest(mode=oct(bad_mode)), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
                plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
                self.assertTrue(sa.apply_plan(plan).ok)
                target = root / ".claude" / "skills" / "a" / "SKILL.md"
                expected = target.read_bytes()
                os.chmod(target, bad_mode)
                fixed_time = 1_600_000_000_123_456_789
                os.utime(target, ns=(fixed_time, fixed_time))
                report = sa.check_plan(plan)
                drift = next(d for d in report.drifts if d.path == ".claude/skills/a/SKILL.md")
                self.assertEqual(drift.status, sa.STALE)
                self.assertTrue(sa.apply_plan(plan).ok)
                self.assertEqual(target.read_bytes(), expected)
                self.assertEqual(target.stat().st_mtime_ns, fixed_time)
                self.assertEqual(target.stat().st_mode & 0o777, 0o644)

    @unittest.skipUnless(os.name != "nt", "POSIX mode contract")
    def test_generated_hook_is_not_executable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "hooks")
            self.assertTrue(sa.apply_plan(plan).ok)
            self.assertEqual((root / ".claude" / "hooks" / "validate.sh").stat().st_mode & 0o777, 0o644)

    def test_strict_utf8_and_no_crlf_in_canonical(self) -> None:
        bad_sources = {
            "crlf": b"---\r\nname: a\r\n---\r\n# A\r\n",
            "lone-cr": b"---\nname: a\n---\n# A\r\n",
            "bom": b"\xef\xbb\xbf---\nname: a\n---\n# A\n",
            "invalid-utf8": b"\xff\xfe",
        }
        for label, raw in bad_sources.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "skills" / "a").mkdir(parents=True)
                (root / "skills" / "a" / "SKILL.md").write_bytes(raw)
                plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
                report = sa.check_plan(plan)
                self.assertFalse(report.ok)
                self.assertTrue(any("canonical source" in d.message for d in report.diagnostics))
                sa.apply_plan(plan)
                self.assertFalse((root / ".claude").exists())

    def _replace_failure_case(self, failing_symbol: str) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest = sa.load_manifest(_manifest(root))
            initial = sa.build_sync_plan(manifest, root, "skills")
            self.assertTrue(sa.apply_plan(initial).ok)
            targets = [
                root / ".agents" / "skills" / "a" / "SKILL.md",
                root / ".claude" / "skills" / "a" / "SKILL.md",
            ]
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# Changed\n")
            plan = sa.build_sync_plan(manifest, root, "skills")
            orphan = root / ".agents" / "skills" / "orphan.txt"
            write(orphan, "must survive failed write\n")
            before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in targets}
            with mock.patch(failing_symbol, side_effect=OSError("injected failure")):
                report = sa.apply_plan(plan)
            self.assertFalse(report.ok)
            self.assertTrue(any(d.severity == sa.ERROR and "injected failure" in d.message
                                for d in report.diagnostics))
            self.assertEqual(
                {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in targets},
                before,
            )
            self.assertEqual(orphan.read_text(encoding="utf-8"), "must survive failed write\n")
            temp_files = [p for p in root.rglob("*") if p.is_file() and ".tmp" in p.name]
            self.assertEqual(temp_files, [])

    def _fdopen_failure_case(self, failure: str) -> None:
        real_fdopen = sa.os.fdopen

        class FaultyWriter:
            def __init__(self, inner: object) -> None:
                self.inner = inner

            def __enter__(self) -> "FaultyWriter":
                return self

            def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
                self.inner.close()

            def fileno(self) -> int:
                return self.inner.fileno()

            def write(self, data: bytes) -> int:
                if failure == "write":
                    raise OSError("injected write failure")
                if failure == "short":
                    return self.inner.write(data[:-1])
                return self.inner.write(data)

            def flush(self) -> None:
                if failure == "flush":
                    raise OSError("injected flush failure")
                self.inner.flush()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest = sa.load_manifest(_manifest(root))
            self.assertTrue(sa.apply_plan(sa.build_sync_plan(manifest, root, "skills")).ok)
            target = root / ".agents" / "skills" / "a" / "SKILL.md"
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# Changed\n")
            plan = sa.build_sync_plan(manifest, root, "skills")
            orphan = root / ".agents" / "skills" / "orphan.txt"
            write(orphan, "must survive failed write\n")
            before = (target.read_bytes(), target.stat().st_mtime_ns)

            def faulty_fdopen(fd: int, mode: str) -> FaultyWriter:
                return FaultyWriter(real_fdopen(fd, mode))

            with mock.patch.object(sa.os, "fdopen", side_effect=faulty_fdopen):
                report = sa.apply_plan(plan)
            self.assertFalse(report.ok)
            self.assertEqual((target.read_bytes(), target.stat().st_mtime_ns), before)
            self.assertTrue(orphan.exists())
            self.assertFalse(any(p.is_file() and p.name.endswith(".tmp") for p in root.rglob("*")))

    def test_fsync_failure_is_reported_cleaned_and_does_not_prune(self) -> None:
        self._replace_failure_case("sync_adapters.os.fsync")

    def test_replace_failure_is_reported_cleaned_and_does_not_prune(self) -> None:
        self._replace_failure_case("sync_adapters.os.replace")

    def test_write_failure_is_reported_cleaned_and_does_not_replace(self) -> None:
        self._fdopen_failure_case("write")

    def test_short_write_is_rejected_before_replace(self) -> None:
        self._fdopen_failure_case("short")

    def test_flush_failure_is_reported_cleaned_and_does_not_replace(self) -> None:
        self._fdopen_failure_case("flush")

    def test_mkstemp_failure_is_reported_and_does_not_prune(self) -> None:
        self._replace_failure_case("sync_adapters.tempfile.mkstemp")

    @unittest.skipUnless(os.name != "nt", "POSIX fchmod contract")
    def test_fchmod_failure_is_reported_cleaned_and_does_not_prune(self) -> None:
        self._replace_failure_case("sync_adapters.os.fchmod")

    @unittest.skipUnless(os.name != "nt", "POSIX chmod contract")
    def test_mode_only_chmod_failure_preserves_content_mtime_and_extras(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertTrue(sa.apply_plan(plan).ok)
            target = root / ".agents" / "skills" / "a" / "SKILL.md"
            os.chmod(target, 0o600)
            fixed_time = 1_600_000_000_123_456_789
            os.utime(target, ns=(fixed_time, fixed_time))
            orphan = root / ".agents" / "skills" / "orphan.txt"
            write(orphan, "must survive chmod failure\n")
            before = target.read_bytes()
            with mock.patch.object(sa.os, "chmod", side_effect=OSError("chmod failure")):
                report = sa.apply_plan(plan)
            self.assertFalse(report.ok)
            self.assertEqual(target.read_bytes(), before)
            self.assertEqual(target.stat().st_mtime_ns, fixed_time)
            self.assertTrue(orphan.exists())

    def test_prune_failure_is_reported_without_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            self.assertTrue(sa.apply_plan(plan).ok)
            orphan = root / ".agents" / "skills" / "orphan.txt"
            write(orphan, "keep after prune error\n")
            with mock.patch.object(sa, "_prune_extras", side_effect=OSError("prune failure")):
                report = sa.apply_plan(plan)
            self.assertFalse(report.ok)
            self.assertTrue(any(d.severity == sa.ERROR and "prune failure" in d.message
                                for d in report.diagnostics))
            self.assertEqual(orphan.read_text(encoding="utf-8"), "keep after prune error\n")

    def test_preexisting_tmp_symlink_blocks_without_write_through(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            plan = sa.build_sync_plan(sa.load_manifest(_manifest(root)), root, "skills")
            external = root / "external-sentinel.txt"
            write(external, "outside must survive\n")
            link = root / ".claude" / "skills" / "a" / "SKILL.md.tmp"
            try:
                link.parent.mkdir(parents=True, exist_ok=True)
                link.symlink_to(external)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"symlink capability unavailable: {exc}")
            report = sa.apply_plan(plan)
            self.assertFalse(report.ok)
            self.assertEqual(external.read_text(encoding="utf-8"), "outside must survive\n")
            self.assertFalse((link.parent / "SKILL.md").exists())

    def test_generated_hardlink_is_invalid_and_never_mutated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest = sa.load_manifest(_manifest(root))
            self.assertTrue(sa.apply_plan(sa.build_sync_plan(manifest, root, "skills")).ok)
            target = root / ".agents" / "skills" / "a" / "SKILL.md"
            external = root / "external-hardlink.txt"
            try:
                os.link(target, external)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"hardlink capability unavailable: {exc}")
            before = (
                target.read_bytes(), target.stat().st_mtime_ns,
                external.read_bytes(), external.stat().st_mtime_ns,
            )
            plan = sa.build_sync_plan(manifest, root, "skills")
            report = sa.check_plan(plan)
            self.assertTrue(any("hardlink" in d.message for d in report.diagnostics))
            self.assertTrue(any(d.status == sa.INVALID for d in report.drifts))
            self.assertFalse(sa.apply_plan(plan).ok)
            self.assertEqual(
                (
                    target.read_bytes(), target.stat().st_mtime_ns,
                    external.read_bytes(), external.stat().st_mtime_ns,
                ),
                before,
            )


# ---------------------------------------------------------------------------
# CLI behavior
# ---------------------------------------------------------------------------


class CliTests(unittest.TestCase):
    def _run(self, argv: list[str]) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = sa.main(argv)
        return result, stdout.getvalue(), stderr.getvalue()

    def test_default_mode_is_read_only_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest = _manifest(root)
            code, stdout, stderr = self._run(["--manifest", str(manifest), "--class", "skills"])
            self.assertEqual(code, 1)
            self.assertIn("missing", stdout.lower())
            self.assertIn("sync-adapters summary:", stdout)
            self.assertEqual(stderr, "")
            self.assertFalse((root / ".claude").exists())

    def test_temp_repo_write_then_check_and_space_in_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repository with spaces"
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest = _manifest(root)
            code, _, stderr = self._run(
                ["--write", "--manifest", str(manifest), "--class", "skills"]
            )
            self.assertEqual((code, stderr), (0, ""))
            code, stdout, stderr = self._run(
                ["--check", "--manifest", str(manifest), "--class", "skills"]
            )
            self.assertEqual((code, stderr), (0, ""))
            self.assertIn("2 ok", stdout)

    def test_missing_and_invalid_manifest_are_exit_one_without_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [root / "missing.toml", root / "invalid.toml"]
            write(cases[1], "this is not toml = [\n")
            for manifest in cases:
                with self.subTest(manifest=manifest.name):
                    code, stdout, stderr = self._run(["--manifest", str(manifest)])
                    self.assertEqual(code, 1)
                    self.assertEqual(stdout, "")
                    self.assertIn("ERROR:", stderr)
                    self.assertNotIn("Traceback", stderr)

    def test_state_json_reports_stale_then_fresh_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest_path = _manifest(root)

            code, stdout, stderr = self._run(
                ["--check", "--state-json", "--manifest", str(manifest_path)]
            )
            self.assertEqual(code, 1)
            self.assertEqual(stderr, "")
            stale = json.loads(stdout)
            self.assertEqual(stale["status"], "stale")
            self.assertGreater(stale["counts"]["missing"], 0)
            self.assertFalse((root / ".claude").exists())
            self.assertFalse((root / ".agents").exists())

            write_code, _, write_stderr = self._run(
                ["--write", "--manifest", str(manifest_path)]
            )
            self.assertEqual((write_code, write_stderr), (0, ""))
            before = {
                path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file()
            }
            code, stdout, stderr = self._run(
                ["--check", "--state-json", "--manifest", str(manifest_path)]
            )
            after = {
                path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file()
            }
            self.assertEqual((code, stderr), (0, ""))
            self.assertEqual(after, before)
            fresh = json.loads(stdout)
            self.assertEqual(
                set(fresh),
                {
                    "schema_version", "status", "manifest_digest", "source_digest",
                    "checked_commit", "checked_at", "counts", "check_command",
                    "drifts", "diagnostics",
                },
            )
            self.assertEqual(fresh["schema_version"], 1)
            self.assertEqual(fresh["status"], "fresh")
            self.assertRegex(fresh["manifest_digest"], r"^[0-9a-f]{64}$")
            self.assertRegex(fresh["source_digest"], r"^[0-9a-f]{64}$")
            self.assertRegex(fresh["checked_at"], r"^\d{4}-\d{2}-\d{2}T.*Z$")
            self.assertEqual(fresh["drifts"], [])
            self.assertEqual(fresh["diagnostics"], [])

    def test_state_json_rejects_write_and_partial_class(self) -> None:
        for argv in (["--write", "--state-json"], ["--state-json", "--class", "skills"]):
            with self.subTest(argv=argv):
                stdout = io.StringIO()
                stderr = io.StringIO()
                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    with self.assertRaises(SystemExit) as raised:
                        sa.main(argv)
                self.assertEqual(raised.exception.code, 2)
                self.assertIn("state-json", stderr.getvalue())

    def test_state_json_invalid_manifest_has_empty_stdout(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "invalid.toml"
            write(manifest, "version = [\n")
            code, stdout, stderr = self._run(
                ["--check", "--state-json", "--manifest", str(manifest)]
            )
            self.assertEqual(code, 1)
            self.assertEqual(stdout, "")
            self.assertIn("ERROR: invalid manifest", stderr)

    def test_adapter_state_digests_track_only_declared_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "skills" / "a" / "SKILL.md"
            write(skill, "---\nname: a\n---\n# A\n")
            manifest_path = _manifest(root)
            manifest = sa.load_manifest(manifest_path)

            manifest_digest = sa.compute_manifest_digest(manifest_path)
            source_digest = sa.compute_source_digest(manifest, root)
            self.assertEqual(manifest_digest, hashlib.sha256(manifest_path.read_bytes()).hexdigest())
            self.assertEqual(source_digest, sa.compute_source_digest(manifest, root))

            write(root / ".claude" / "unmanaged.txt", "generated-only change\n")
            self.assertEqual(source_digest, sa.compute_source_digest(manifest, root))

            write(skill, "---\nname: a\n---\n# Changed\n")
            changed_content_digest = sa.compute_source_digest(manifest, root)
            self.assertNotEqual(source_digest, changed_content_digest)

            destination = root / "skills" / "b"
            destination.parent.mkdir(parents=True, exist_ok=True)
            skill.parent.rename(destination)
            changed_path_digest = sa.compute_source_digest(manifest, root)
            self.assertNotEqual(changed_content_digest, changed_path_digest)

    def test_write_failure_is_exit_one_without_traceback_or_partial_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest = _manifest(root)
            with mock.patch.object(sa, "_atomic_write_if_needed", side_effect=OSError("CLI write failure")):
                code, stdout, stderr = self._run(
                    ["--write", "--manifest", str(manifest), "--class", "skills"]
                )
            self.assertEqual(code, 1)
            self.assertIn("ERROR:", stdout)
            self.assertNotIn("Traceback", stdout + stderr)
            self.assertFalse((root / ".agents").exists())
            self.assertFalse((root / ".claude").exists())

    def test_mutually_exclusive_modes_exit_two(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as raised:
                sa.main(["--write", "--check"])
        self.assertEqual(raised.exception.code, 2)
        self.assertIn("usage:", stderr.getvalue().lower())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_bad_class_rejected_after_manifest_load(self) -> None:
        # --class is a free string (source classes are manifest-declared); an
        # unknown class is rejected after the manifest loads, returning 1.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            manifest = _manifest(root)
            code, stdout, stderr = self._run(["--manifest", str(manifest), "--class", "not-a-class"])
        self.assertEqual(code, 1)
        self.assertIn("not-a-class", stderr)
        self.assertNotIn("Traceback", stdout + stderr)

    def test_diff_preview_is_bounded_per_file_and_for_first_ten_files(self) -> None:
        long_expected = "".join(f"expected {i}\n" for i in range(50))
        long_actual = "".join(f"actual {i}\n" for i in range(50))
        preview = sa._diff_preview(long_expected, long_actual)
        self.assertLessEqual(len(preview.splitlines()), 20)
        self.assertIn("truncated", preview)

        report = sa.CheckReport(
            drifts=[sa.Drift(sa.STALE, f"generated/{i:02}.txt", f"preview-{i}") for i in range(12)]
        )
        formatted = "\n".join(sa._format_report(report))
        for i in range(12):
            self.assertIn(f"STALE: generated/{i:02}.txt", formatted)
        self.assertEqual(sum(f"preview-{i}" in formatted for i in range(12)), 10)
        self.assertIn("diff previews omitted for 2 additional file(s)", formatted)


# ---------------------------------------------------------------------------
# Repository integration (read-only Gate 3/4 evidence)
# ---------------------------------------------------------------------------


class RepoBaselineTests(unittest.TestCase):
    """Require permanent exact generated freshness after Gate 4."""

    def setUp(self) -> None:
        self.manifest = sa.load_manifest(sa.DEFAULT_MANIFEST)
        self.plan = sa.build_sync_plan(self.manifest, REPO_ROOT)

    def test_agents_post_gate4_copy_is_noop_and_idempotent(self) -> None:
        def snapshot(root: Path) -> dict[str, tuple[bytes, int, int]]:
            result: dict[str, tuple[bytes, int, int]] = {}
            for base in (".claude/agents", ".codex/agents"):
                for path in sorted((root / base).glob("*")):
                    if path.is_file():
                        st = path.stat()
                        result[path.relative_to(root).as_posix()] = (
                            path.read_bytes(), st.st_mtime_ns, st.st_mode
                        )
            return result

        with tempfile.TemporaryDirectory(prefix="cdd gate4 rehearsal ") as tmp:
            root = Path(tmp)
            shutil.copy2(REPO_ROOT / "cdd-manifest.toml", root / "cdd-manifest.toml")
            shutil.copytree(REPO_ROOT / "agents", root / "agents", copy_function=shutil.copy2)
            shutil.copytree(
                REPO_ROOT / ".claude" / "agents",
                root / ".claude" / "agents",
                copy_function=shutil.copy2,
            )
            shutil.copytree(
                REPO_ROOT / ".codex" / "agents",
                root / ".codex" / "agents",
                copy_function=shutil.copy2,
            )
            manifest = sa.load_manifest(root / "cdd-manifest.toml")
            plan = sa.build_sync_plan(manifest, root, "agents")
            self.assertEqual(
                sa.check_plan(plan).counts(),
                {sa.OK: 106, sa.STALE: 0, sa.MISSING: 0, sa.EXTRA: 0, sa.INVALID: 0},
            )
            before = snapshot(root)
            first = sa.apply_plan(plan)
            after_first = snapshot(root)
            self.assertEqual(after_first, before)
            self.assertEqual(
                first.counts(),
                {sa.OK: 106, sa.STALE: 0, sa.MISSING: 0, sa.EXTRA: 0, sa.INVALID: 0},
            )
            second = sa.apply_plan(sa.build_sync_plan(manifest, root, "agents"))
            self.assertTrue(second.ok)
            self.assertEqual(snapshot(root), after_first)

    def test_all_generated_outputs_are_exactly_fresh(self) -> None:
        report = sa.check_plan(self.plan)
        # Total = sum of each source's expected_count * its declared target count.
        expected_total = sum(
            src.expected_count * len(src.targets)
            for src in self.plan.manifest.sources.values()
        )
        self.assertEqual(expected_total, 302)  # 74*2 + 53*2 + 12*2 + 1*2 + 16(claude) + 3 dirs *2 nested
        self.assertEqual(len(self.plan.rendered), expected_total)
        self.assertEqual(len(report.drifts), expected_total)
        self.assertEqual(report.diagnostics, [])
        self.assertEqual(
            report.counts(),
            {sa.OK: expected_total, sa.STALE: 0, sa.MISSING: 0, sa.EXTRA: 0, sa.INVALID: 0},
        )
        self.assertTrue(all(d.status == sa.OK for d in report.drifts))
        for rendered in self.plan.rendered:
            self.assertEqual((REPO_ROOT / rendered.dest).read_bytes(), rendered.expected, rendered.dest)

    def test_rules_canonical_claude_only_and_byte_identical(self) -> None:
        # rules/ is canonical; .claude/rules/ is a byte-identical Claude-only
        # generated projection. (Codex has no rules output; see
        # test_codex_native_rules_survive_generation for the survival contract.)
        canonical = {p.name: p.read_bytes() for p in sorted((REPO_ROOT / "rules").glob("*.md"))}
        self.assertEqual(len(canonical), 16)
        for name, blob in canonical.items():
            self.assertEqual((REPO_ROOT / ".claude" / "rules" / name).read_bytes(), blob, name)
        self.assertEqual(self.plan.manifest.sources["rules"].targets, ("claude",))

    def test_codex_native_rules_survive_generation(self) -> None:
        # A user's native .codex/rules/default.rules must survive --check and
        # --write: rules targets Claude only, so .codex/rules is never a managed
        # root and the generator must not flag or prune it.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "skills" / "a" / "SKILL.md", "---\nname: a\n---\n# A\n")
            write(root / "rules" / "engine-code.md", "---\npaths:\n  - src/core/**\n---\nzero allocs\n")
            native = root / ".codex" / "rules" / "default.rules"
            write(native, 'prefix_rule(pattern=["echo"], decision="allow")\n')
            manifest = root / "cdd-manifest.toml"
            write(manifest, (
                'version = 2\n[runtimes.claude]\nlabel="Claude"\n[runtimes.codex]\nlabel="Codex"\n'
                '[sources.skills]\nroot="skills"\ninclude="*/SKILL.md"\nexpected_count=1\n'
                '[sources.rules]\nroot="rules"\ninclude="*.md"\nexpected_count=1\ntargets=["claude"]\n'
                '[[outputs]]\nsource="skills"\nruntime="claude"\ndest_root=".claude/skills"\ndest_pattern="{relative}"\ntransforms=[]\nowns_tree=true\n'
                '[[outputs]]\nsource="skills"\nruntime="codex"\ndest_root=".agents/skills"\ndest_pattern="{relative}"\ntransforms=[]\nowns_tree=true\n'
                '[[outputs]]\nsource="rules"\nruntime="claude"\ndest_root=".claude/rules"\ndest_pattern="{name}"\ntransforms=[]\nowns_tree=true\n'
            ))
            m = sa.load_manifest(manifest)
            plan = sa.build_sync_plan(m, root, "all")
            self.assertTrue(sa.apply_plan(plan).ok, plan.diagnostics)
            self.assertEqual(native.read_text(), 'prefix_rule(pattern=["echo"], decision="allow")\n')
            report = sa.check_plan(sa.build_sync_plan(m, root, "all"))
            self.assertTrue(report.ok, report.diagnostics)

    def test_nested_instructions_byte_identical_siblings(self) -> None:
        for d in ("src", "design", "docs"):
            inst = (REPO_ROOT / d / "INSTRUCTIONS.md").read_bytes()
            self.assertEqual((REPO_ROOT / d / "CLAUDE.md").read_bytes(), inst, f"{d}/CLAUDE.md")
            self.assertEqual((REPO_ROOT / d / "AGENTS.md").read_bytes(), inst, f"{d}/AGENTS.md")
            # Nested guidance is runtime-neutral: no CLAUDE.md self-reference.
            self.assertNotIn(b"CLAUDE.md", (REPO_ROOT / d / "AGENTS.md").read_bytes(), f"{d}/AGENTS.md")
        for name in ("nested-src", "nested-design", "nested-docs"):
            self.assertEqual(self.plan.manifest.sources[name].targets, ("claude", "codex"))

    def test_real_53_codex_agents_are_byte_and_value_exact(self) -> None:
        expected = {
            rendered.dest: rendered.expected
            for rendered in self.plan.rendered
            if rendered.dest.startswith(".codex/agents/")
        }
        self.assertEqual(len(expected), 53)
        for path, expected_bytes in sorted(expected.items()):
            actual_bytes = (REPO_ROOT / path).read_bytes()
            self.assertEqual(actual_bytes, expected_bytes, path)
            self.assertFalse(actual_bytes.startswith(b"\xef\xbb\xbf"), path)
            self.assertNotIn(b"\r", actual_bytes, path)
            actual_text = actual_bytes.decode("utf-8")
            expected_text = expected_bytes.decode("utf-8")
            actual_values = sa.tomllib.loads(actual_text)
            expected_values = sa.tomllib.loads(expected_text)
            required = {"name", "description", "developer_instructions"}
            self.assertEqual(set(actual_values), required, path)
            self.assertEqual(set(expected_values), required, path)
            self.assertEqual(actual_values, expected_values, path)


if __name__ == "__main__":
    unittest.main()
