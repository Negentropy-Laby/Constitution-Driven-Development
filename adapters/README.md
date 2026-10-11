# Adapter Boundaries

This directory documents runtime adapter boundaries for CDD.

## Common canonical source assets

In the designated Source library, canonical authority assets are hand-authored
outside adapter runtime trees:

| Root | Role |
|------|------|
| `workflow/` | Canonical workflow catalog and generated workflow views |
| `templates/` | Canonical document and memory-bank templates |
| `standards/` | Shared coding, coordination, context, and setup standards |
| `skill_testing/` | Cross-project skill and agent testing catalog, specs, rubric, and spec templates |
| `docs/` | User manuals, references, examples, and acceptance documentation |
| `skills/` | Canonical slash-command skills (one `<name>/SKILL.md` each) |
| `agents/` | Canonical agent definitions (flat `<name>.md`) |
| `hooks/` | Canonical hook scripts |
| `rules/` | Canonical path-scoped coding policies (Claude-only generated projection) |
| `INSTRUCTIONS.md` | Canonical root project instructions |

## Runtime-facing roots (mixed ownership)

Generated subtrees expose canonical definitions to runtime surfaces.
Use installed platform files directly; ordinary template use does not require
a local maintenance kit. Those derived outputs are never independently authored;
whole runtime roots also contain hand-authored/runtime-owned configuration:

| Root | Role |
|------|------|
| `.claude/` | Mixed: generated skills/agents/hooks/rules; hand-authored settings.json/statusline.sh and compatibility pointers |
| `.agents/` | Codex slash-command skill adapter copy (generated) |
| `.codex/` | Mixed: generated agents/hooks; hand-authored hooks.json and runtime-owned native command rules/config |

Read the installed adapters and their required neutral originals directly.
Changing canonical definitions and their projections requires covered write
authority, an exact delivery allowlist and review of the complete result.

Do not move canonical workflow catalogs, templates, standards, or skill testing
assets into adapter runtime trees. Adapter directories may contain wrappers,
settings, generated copies, or compatibility pointers only.

Codex's native `.codex/rules/*.rules` command-approval policy is runtime-owned
and never generated. `rules/` projects to Claude only (`.claude/rules/`); Codex
has no path-glob equivalent and consults canonical `rules/` through root guidance.
Nested per-directory instructions (`src/`, `design/`, `docs/`) are runtime-neutral
canonical sources that generate a `CLAUDE.md` + `AGENTS.md` sibling pair.

## Imported consumer projects

The reusable project norms are in
`templates/memory-bank/t0_core/basic_law_index.md`, section "CDD Source and
Target Project Boundaries". Their complete text is carried by each installed
`constitute` entry. New constitution drafts include it; `adopt full` and
`adopt infra` check for an approved additive merge into the existing project
instructions or law index. Include those full entries in an initialization or
import package. Their use does not need the general source trees or local
maintenance tools, and it does not authorize a project write or law acceptance.

A consumer uses its approved installed platform files, necessary neutral support
and project rules. General root `agents/` and `skills/` mirrors are excluded from
consumer Git submission/publication. Local presence inside or outside a project
is allowed and does not establish another Source or authorize moving/deleting
files. Read complete installed entries and the actual required references
for the selected platform; a local maintenance reader, profile or lock is not a
normal-use prerequisite. Optional diagnostics can verify additional identities
when provided, but installed-file observations alone do not prove current Source,
runtime execution or workflow completion. An unavailable Source blocks Source
reproduction, generation and common edits, not ordinary authorized artifact use.

Use the actual Source and the approved disposable source stage for generation;
review exact candidates and deploy only the approved allowlist. Do not run this
Source library's generic generator main/write against a consumer. Installed
Codex TOML, a catalog, an offline context or a copied checker is not full source
authority. Template-maintenance checkers remain separate local maintenance
files excluded from consumer Git submission/publication regardless of local
placement; they are not normal-use dependencies or
permission to activate hooks.

## Required delivery inputs

Build a reviewed per-file allowlist for the selected runtime and intended
workflows. Include its installed entries, required relative references, actual
agent readers and applicable policies; follow required direct/indirect references
to closure. Include necessary neutral originals at their owner paths. Example,
future-output and inapplicable references do not silently become required inputs,
but missing required originals cannot be replaced by similarly named placeholders.

| Workflow scope | Necessary neutral inputs |
|---|---|
| Shared governance | `standards/evidence-lifecycle.md`, `standards/notes-adr-sync.md`, `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`; actual project instructions, `standards/technical-preferences.md` and applicable `rules/` |
| Constitution initialization | The actual `templates/memory-bank/` originals listed by `/constitute`, including `framework_contract.md` and unchanged `adapter_state.yaml`; `skill_testing/README.md`, `catalog.yaml`, `quality-rubric.md`, `specs/skills/`, `specs/agents/` and `templates/` |
| Workflow routing and T2 mirrors | `workflow/workflow-catalog.yaml`, `docs/PHASE-CHECKLISTS.md`, `workflow/generated/gate-required-artifacts.md`; any further required view/policy referenced by the selected workflow |
| Full CDD adoption and document-kind review | Complete installed `/brainstorm`, `/quick-design`, `/map-systems` and `/design-system` owners; `design/INSTRUCTIONS.md`, `rules/design-docs.md`, `templates/game-concept.md`, `templates/product-concept.md`, `templates/module-index.md`; `/adopt` and selected review entries with their required references, applicable agent readers and `standards/director-gates.md` |
| Stack setup and project work | The selected skill's installed references, actual document templates, standards, version references and policy originals required by its configured domain/capabilities |

Expand the selected directory entries into exact files and independently review
the resulting allowlist before import/update. `/constitute` uses its listed
neutral originals; other scopes need their own smaller required closure. These
reusable templates/specs are normal-use inputs, distinct from local-only CDD
maintenance scripts, test fixtures and process evidence. Preserve existing
project-owned inputs and customizations. Do not deliver general root `agents/`
or `skills/`, maintenance tools/metadata or an entire Source checkout to fill a
gap. Missing/unread originals leave the affected workflow pending. Complete
installed inputs remain usable offline; common updates require the sole Source.

## Consumer differences and migration order

A consumer retains portable project differences and the actual selected platform
paths. Preserve the designated Source authority independently of local placement;
exclude general source mirrors from consumer Git delivery. Preserve project
customizations, runtime-owned settings and complete historical originals.
Updates require the actual Source, exact input identities, scoped authority,
independent candidate review and readback of the approved delivery.
Unresolved identity or ownership
conflicts stop affected updates. Normal installed-file use remains available
without a maintenance reader or lock and does not establish live freshness.

## Transforms and actual runtime claims

`skills/` copies verbatim to `.claude/skills/`. For `.agents/skills/`, the
Accepted `runtime_substitute` contract applies the Source-declared literal
replacement pairs deterministically. It is blind substitution, not a
context-aware rewrite or a promise of equivalent native capabilities.
The Accepted post-substitution guard rejects a repeated token across a short
connector (`and`/`or`/`,`), only when that token contains a replacement target;
residual forbidden source literals also fail. Preserve these exact conditions
without broadening the guard. See ADR-0002's D2/D3 contracts.

Agent Markdown copies to Claude; Codex TOML keeps
`name`, `description` and `developer_instructions`. The seven known dropped
fields are `tools`, `model`, `maxTurns`, `memory`, `skills`, `disallowedTools`
and `isolation`. Unknown agent fields block generation; canonical metadata is
retained at its source, not promised as equivalent runtime behavior.

Codex manually consults canonical `rules/*.md`; its native `.codex/rules/*.rules`
command-approval namespace is independent. Generation does not install/activate
runtime configuration or Memory Bank. Runtime availability/loading/hook firing/
agent execution needs actual supported metadata and observations. CLI structure/
help and discovery fixtures do not certify live autoload or skill/spec/category
qualification. This framework source generates real usable adapters; optional
project initialization or a different project's state is not its activation truth.

A platform comparison does not certify all linked neutral supports. Review
inputs bind needed support bytes separately under `standards/evidence-lifecycle.md`.
Projected skill text should use canonical owner paths/actual runtime metadata,
avoiding cross-runtime comparison literals that blind substitution can corrupt.
