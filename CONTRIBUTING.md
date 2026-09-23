# Contributing

Thank you for improving Constitution Driven Development. This repository is a
workflow template, so changes must preserve the public command surface and the
Game/Product parity contract.

## Contribution Rules

- Do not rename slash commands.
- Do not split Product support into product-only replacement commands.
- Do not remove existing Game workflows, examples, agents, or documentation.
- Add Product support beside the matching Game branch inside the same command.
- Keep `workflow-catalog.yaml` as the required-step source of truth.
- Keep story paths under `production/epics/[epic-slug]/story-NNN-[slug].md`.
- Keep evidence under `production/qa/evidence/`.

## Local Checks

Run these before opening a pull request:

```powershell
git diff --check
python scripts\skill_lint.py --self-test
python -m unittest discover -s tests -p "*_test.py"
python scripts\skill_lint.py --strict skills
python scripts/sync_adapters.py --check
python scripts\workflow_consistency.py
```

`skill_lint.py --strict skills` lints every canonical skill Markdown file —
`skills/<name>/SKILL.md` plus its on-demand `skills/<name>/references/*.md` —
and must report `0 error(s)`. Frontmatter checks apply to entrypoints only, so
reference files are checked for Markdown and command-reference defects without
needing skill frontmatter. (Template-path warnings remain advisory under the
existing contract.) These commands mirror the `Template Consistency` CI checks.

## Pull Request Expectations

- Keep each PR focused on one behavior, documentation contract, or quality gate.
- Include validation commands and results in the PR description.
- Update examples, quick-start docs, workflow catalog entries, and gate wording
  together when changing phase behavior.
- Add or update consistency checks when fixing workflow drift.

## Skill Changes

When editing a canonical skill package — `skills/<name>/SKILL.md` or its
on-demand references under `skills/<name>/references/` (never hand-edit the
generated `.claude/skills` or `.agents/skills` trees directly) — regenerate the
runtime adapters afterward by running `python scripts/sync_adapters.py --write --class skills`:

- Preserve frontmatter fields and command names.
- Keep explicit invocation guards where present.
- Keep Game and Product branches at comparable detail.
- Avoid broken Markdown markers such as standalone `**` lines or unclosed
  inline code spans.
- Run strict lint on the edited skill and the full skills directory.
- Keep package layout to Markdown only: the entrypoint must be the package-root
  `SKILL.md` (nested `SKILL.md` files are rejected by the generator), and
  `references/` holds supporting material that `SKILL.md` links to instead of
  duplicating prose. Every `*.md` in a package is mirrored to both runtimes.
