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

From a clean Source clone, run `git diff --check` and review each changed entry,
its required references, governing standards and applicable Game/Product
behavior. Verify the actual delivery allowlist and platform projections against
the complete canonical inputs. Missing required originals remain incomplete.

Local generators, linters, maintenance tests and historical Source CI are supplied
separately and excluded from template delivery. When those tools are actually
provided and their scope is authorized, use their supported read-only checks and
retain the results outside the deliverable templates. Do not require a fresh
clone to execute absent tools, restore their tracking, or use an old CI result
to certify a new revision. Report static review, fixture checks and live runtime
trials separately.

## Pull Request Expectations

- Keep each PR focused on one behavior, documentation contract, or quality gate.
- Include validation commands and results in the PR description.
- Update examples, quick-start docs, workflow catalog entries, and gate wording
  together when changing phase behavior.
- Keep any local consistency-check changes separate from deliverable templates.

## Skill Changes

When editing a canonical skill package — `skills/<name>/SKILL.md` or its
on-demand references under `skills/<name>/references/` (never hand-edit the
generated `.claude/skills` or `.agents/skills` trees directly) — prepare matching
runtime adapters in an authorized Source stage using the separately provided
renderer. Review the full output scope before installation; unavailable rendering
remains NotRun and does not justify hand-editing generated copies:

- Preserve frontmatter fields and command names.
- Keep explicit invocation guards where present.
- Keep Game and Product branches at comparable detail.
- Avoid broken Markdown markers such as standalone `**` lines or unclosed
  inline code spans.
- Review the edited skill and its required references; use strict lint only when the local diagnostic is provided.
- Keep package layout to Markdown only: the entrypoint must be the package-root
  `SKILL.md` (nested `SKILL.md` files are rejected by the generator), and
  `references/` holds supporting material that `SKILL.md` links to instead of
  duplicating prose. Every `*.md` in a package is mirrored to both runtimes.
