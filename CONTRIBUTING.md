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

**Confirm asset ownership before instruction purpose.** First establish actual CDD
framework provenance, ownership and delivery role for the complete package and its
required support. Apply instruction-purpose classification only within that confirmed
CDD asset collection. Project-owned skills, agents/roles, tools, configuration and
documents follow their project's rules; development use, native instruction fields
and skill-directory placement do not make them CDD assets. Renaming or tailoring a
CDD template does not itself change its ownership. Unresolved ownership stays pending.

**Target Git separation preserves authorized local use.** CDD framework assets and
maintenance tools are excluded from Target Git tracking, staging, commits and delivery/
publication contents. This does not prohibit their authorized local retention,
discovery, loading, effect or use. Keep complete required inputs at usable paths.
Ordinary template use must not depend on the local maintenance toolkit. Ignore and
runtime loading are separate; existing tracked content requires separately authorized,
recoverable tracking-only migration that leaves local files and required references intact.

Ordinary Target use requires complete installed agent/skill packages for the
selected runtime and all required local inputs. It does not require an additional
complete copy of the Source-root `agents/` or `skills/` trees. This does not waive
required originals, prohibit authorized local copies or change Git eligibility.
Source development, reproduction, generation and explicitly selected checks of
canonical originals retain their own input and authorization requirements. Resolve
consumer installation paths under `standards/directory-structure.md`, section
"Consumer layout resolution for imports and updates".

Within confirmed CDD packages, independent portable configuration must neither carry
nor reconstruct CDD instruction bodies or exclusive support, and must have substantive
readers independent of those packages. A native loader alone does not qualify.

From a clean Source clone, run `git diff --check` and review each changed entry,
its required references, governing standards and applicable Game/Product
behavior. Verify proposed Source Git submission candidates and exact approved
platform-output write paths against the complete canonical inputs. For a Target
import/update, review its required local-input allowlist separately from Git
candidates. Apply `standards/skill-purpose.md` only to whole packages and support
confirmed as CDD by actual provenance, ownership and delivery role. Source developer
templates and complete projections remain framework product assets. In a Target,
CDD instruction bodies, projections and exclusive support remain outside Git delivery
while retaining authorized local use, even when tailored. Project-owned development
skills, roles, tools, configuration and documents follow project rules. Minimal CDD
bindings and independent configuration must neither carry nor reconstruct framework
instruction bodies or exclusive support. Missing required originals stay incomplete.

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
- Keep each delivered entrypoint's consumer body below 28,000 UTF-16 code units
  and at most 7,000 estimated tokens. Measure the exact body returned by the
  consumer's frontmatter parser, including its remaining whitespace and fenced
  content; use JavaScript `body.length` and `Math.round(body.length / 4)`.
  Check canonical and generated runtime entries separately. This is this
  project's compatibility budget for the reviewed consumer, not a universal
  hard limit for every host or an actual tokenizer count. Move long details into
  conditionally required package references with explicit read timing and
  incomplete handling, preserving the controlling rules in the entrypoint.
