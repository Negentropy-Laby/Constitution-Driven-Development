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
Ordinary Target imports do not require an additional complete copy of Source-root
`agents/` or `skills/`. Follow [Ordinary Target installation](../standards/directory-structure.md#ordinary-target-installation)
for the selected runtime's paths and required-input closure. Keep complete required
originals locally; optional authorized Source copies remain allowed. Installation
need and Target Git eligibility are separate decisions.
Changing canonical definitions and their projections requires covered write
authority, an exact approved canonical-change/platform-output write scope and
review of the complete canonical inputs and generated result. Consumer updates
review the required local-input allowlist separately from Target Git candidates.

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

A consumer uses its approved installed platform files, complete local CDD inputs
and project rules. First establish actual framework provenance, ownership and
delivery role; apply purpose rules only within that confirmed CDD collection.
Project-owned skills, roles, tools, configuration and documents follow their own
rules, including development capabilities. Development use alone does not make
them CDD templates, regardless of native fields or directory placement.

Confirmed CDD templates, full projections and exclusive support stay outside Target
Git tracking/staging/commits/delivery/publication. Minimal bindings and independent
configuration cannot carry or reconstruct those CDD bodies. Tailoring or renaming
a CDD template does not itself change its ownership. Review shared/mixed CDD and
project portions separately; preserve each actual owner. General CDD source mirrors
and maintenance tools remain local-only in consumers.

Local presence inside or outside a project is allowed and grants no Source authority,
move/delete or log-path authority. Git exclusion and ignore rules do not prohibit
authorized local retention, discovery, loading, effect or use. Read complete installed
entries and required references for the selected platform. A maintenance toolkit,
reader, profile or lock is not a normal-use prerequisite; optional authorized local
maintenance may run. Installed-file observations alone do not prove current Source,
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

## Required local-use inputs and Git submission candidates

Confirm actual CDD framework provenance, ownership and delivery role before
applying instruction-purpose rules to the confirmed CDD package and support.
Project-owned skills, independent/native roles, tools, configuration and documents
retain project rules, including development capabilities. Development purpose,
TOML/native instruction fields and platform directories do not make them CDD assets.

Confirmed CDD framework templates and exclusive references/overlays remain local-only
in a Target even when tailored or fully projected. Minimal bindings and independent
configuration must not carry or reconstruct CDD instruction bodies/support; a native
loader alone cannot qualify a copied CDD role body. These CDD-related limits do not
exclude independently established project-owned development roles. Git exclusion
preserves authorized local discovery/loading/effect/use; missing actual required
local inputs, not ignore membership, leaves affected CDD work pending.

First establish asset ownership and delivery role under `standards/skill-purpose.md`.
Within the confirmed CDD collection, inspect complete instruction bodies and support.
Native discovery, customization or projection does not change a CDD template's owner
or grant Git eligibility. Keep complete required CDD packages in the local-input
closure; do not truncate them to make Git candidates appear minimal. Preserve
project-owned portions and review local-input and Git candidate sets separately.

Build a reviewed per-file local-input allowlist for the selected runtime and intended
workflows. For import/update, first apply the layout-resolution owner in
`standards/directory-structure.md`, section "Consumer layout resolution for imports
and updates". Bind the allowlist to the resolved consumer tree and old-to-new
mapping, including actual readers, generation/configuration effects, authority,
recovery and unresolved destinations; an old layout's self-consistency is not
current alignment. Keep that plan with its existing scoped owner, not a new
mandatory manifest or lock. Include its installed entries, required relative references, actual
agent readers and applicable policies; follow required direct/indirect references
to closure. Keep necessary neutral originals locally at their owner paths. This
readable-input set is separate from Target Git candidates; a required CDD
original does not gain tracking, staging, commit or publication eligibility. Example,
future-output and inapplicable references do not silently become required inputs,
but missing required originals cannot be replaced by similarly named placeholders.

| Workflow scope | Necessary neutral inputs |
|---|---|
| Shared governance and skill purpose | `standards/skill-purpose.md`, `standards/evidence-lifecycle.md`, `standards/notes-adr-sync.md`, `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`; actual project instructions, `standards/technical-preferences.md` and applicable `rules/` |
| Constitution initialization | The actual `templates/memory-bank/` originals listed by `/constitute`, including `framework_contract.md` and unchanged `adapter_state.yaml`; `skill_testing/README.md`, `catalog.yaml`, `quality-rubric.md`, `specs/skills/`, `specs/agents/` and `templates/` |
| Workflow routing and T2 mirrors | `workflow/workflow-catalog.yaml`, `docs/PHASE-CHECKLISTS.md`, `workflow/generated/gate-required-artifacts.md`; any further required view/policy referenced by the selected workflow |
| Full CDD adoption and document-kind review | Complete installed `/brainstorm`, `/quick-design`, `/map-systems` and `/design-system` owners; `design/INSTRUCTIONS.md`, `rules/design-docs.md`, `templates/game-concept.md`, `templates/product-concept.md`, `templates/module-index.md`; `/adopt` and selected review entries with their required references, applicable agent readers and `standards/director-gates.md` |
| Stack setup and project work | The selected skill's installed references, actual document templates, standards, version references and policy originals required by its configured domain/capabilities |

Expand the selected directory entries into exact files and independently review
the resulting local-input allowlist before import/update. `/constitute` uses its
listed neutral originals; other scopes need their own smaller required closure.
These reusable templates/specs are normal-use local-only inputs in a target,
distinct from CDD maintenance scripts, test fixtures and process evidence. Preserve existing
project-owned inputs and customizations. Exclude general root `agents/` or
`skills/` mirrors, maintenance tools/metadata and entire Source checkouts from
Target Git delivery; this does not prohibit authorized local copies. Resolve a
missing required input at its actual owner path rather than requiring a general
source mirror as the installation fix. Missing/unread originals leave the
affected workflow pending. Complete
installed inputs remain usable offline; common updates require the sole Source.

## Consumer differences and migration order

**Existing tracked neutral inputs.** When a boundary change affects reusable
confirmed CDD template/standard/workflow/spec originals or CDD instruction packages
already tracked under earlier
guidance, record reconciliation as pending until the applicable governance gate
closes. Earlier tracking is neither automatically grandfathered as compliant nor
judged a violation under an unaccepted rule. Keep local originals and Git history.
After acceptance or a valid scoped exception under existing governance, obtain
separate exact-path project migration authority before removing reviewed reusable
originals or CDD development-template/support content from Git tracking. Retain their local files, required-reference closure,
project customizations and recoverable before bytes; review the actual index/diff
and separately eligible Git candidates. Commit/publication still require their
own authority. This differs from already-tracked maintenance content and grants
no untracking, deletion, relocation or migration authority by itself.

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
