---
name: constitute
description: "Constitution Driven Development project governance — establishes, derives, updates, or amends governing principles at any project stage. Reads existing artifacts to derive a constitution, audits alignment, tracks versions, and supports formal amendment workflow. Domain-agnostic, stage-aware unified onboarding entry."
argument-hint: "[no arguments]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, AskUserQuestion
---

## Authority, required reading and terminal facts

Read and apply `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`,
`standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md`. Reuse named
authority across sections/roles/recovery; show the exact draft/paths/effects for
material new scope. Content agreement, file writes, law/ADR acceptance, required
independent review, publication and completion remain separate. Review-only
invokes no write entrypoint; report-only covers only its new assigned report,
excluding laws, initialization, indexes and stage/state. Each other effect needs
its own covered scope. No automatic governance decisions or Memory Bank activation.

Detect actual stage first and apply the matching existing stage-routing section
before later workflows. Resolve domain from actual bodies/configuration under
`standards/technical-preferences.md`; filenames or copied placeholders cannot
override evidence. Unknown blocks only dependent domain work; neutral discovery
and browsing remain possible. A stage label, file count or concept agreement
proves no qualification or ratification.

References are relative to this installed package. Read the selected stage, branch
and phase before its dependent questions/proposals/effects; linking is not reading.
Missing, unread or truncated required material leaves affected steps INCOMPLETE.
Read long applicable sections in consecutive bounded chunks (at most 8,000 UTF-16
units per result), including the full selected Stage 0 section when needed.
Do not load all initialization/derivation/amendment references for a browse-only
route. Ship complete package references and selected required neutral originals
for offline use; no maintenance kit/live Source substitute or prerequisite.

Keep the Reusable Project Boundary Template inline below: `/adopt full` and
`/adopt infra` read this installed section without requiring Source access.
New interactive/derived laws stay Proposed unless exact text/revision, Support IDs
and legal action have verified acceptance authority. Preserve actual version and
sign-off history. Initial `adapter_state.yaml` remains unchanged/uninitialized;
latest layout plans and approved writes are not installed/freshness evidence.
Bind the designated CDD Source identity/revision; unresolved facts stay unconfigured.

## Principle Lifecycle Reference

All laws in `basic_law_index.md` must have a `Status` field:

| Status | Meaning | When to use |
|--------|---------|-------------|
| `Proposed` | Drafted, not yet ratified | New interactive or derived laws before exact acceptance authority is verified |
| `Accepted` | In effect | After exact ratification (Phase 3e), including independently verified ratification for Phase 4 derived laws |
| `Accepted (amended [date])` | In effect, text changed | After amendment (Phase 6) |
| `Superseded by BL-XX ([date])` | Replaced by another law | When a new law makes this one obsolete |
| `Deprecated ([date])` | Intentionally removed | When a principle is no longer relevant with no replacement |

---

## User Guide

- When to use: Establish, derive, audit or amend Game/Product project governance
  at the actual detected stage through the unified `/constitute` entry.
- Inputs: Existing project artifacts, decisions, scoped write authority and any
  separately verified ratification; no command arguments are required.
- Outputs: The selected route's proposals, reports and covered project documents.
- Memory-bank writes: Only selected authorized T0/T1/T2/T3, document-map/README
  and skeleton/index effects listed in the initialization reference; each path
  remains separately scoped. Review mode is its own `production/review-mode.txt` effect.
- Next steps: Use Phase 7's actual catalog and stage route; recommendations do
  not auto-run commands, ratify laws or advance state.

# Constitution Legislation — Stage-Aware Project Governance

This skill initializes the `memory_bank/` governance control plane: T0 core
laws and current state, T1 supporting axioms, T2 execution mirrors/indexes, and
T3 archive indexes. It also writes `production/review-mode.txt`.

Unlike the legacy first-session-only onboarding flow, this skill can be
invoked at **any project stage**. It detects what you've already built and
adapts: deriving a constitution from existing artifacts, auditing alignment,
running formal amendments with version tracking, or guiding a fresh project
through discovery.

---

## Purpose before Project Governance

Confirm actual CDD provenance, ownership and Source/Target delivery role before
instruction purpose. Read `standards/skill-purpose.md` for the complete package
and required support; apply the full inline Reusable Project Boundary Template
below. Names, directory placement or development use alone do not decide CDD
ownership. Unresolved ownership stays pending only for its affected action.
Preserve project-owned development capabilities, complete authorized local inputs
and their independent Git/delivery review; this routing grants no migration.

Identify whether the task uses delivered functions or develops/governs the actual
project. This CDD constitution skill and its exclusive framework support are
local-only Target inputs, including tailored/full native copies; the designated
Source delivers them as framework product assets. Project documents produced
under their own authority retain their project ownership. Route independent
product-use tasks through their actual product capabilities without forcing CDD
initialization.

## Reusable Project Boundary Template

The reusable source is `templates/memory-bank/t0_core/basic_law_index.md`,
section "CDD Source and Target Project Boundaries". Include that section in each
new or derived `memory_bank/t0_core/basic_law_index.md` draft. It is separate
from the project's three to five numbered laws; retain their IDs and approval
or ratification status. Existing projects receive only an approved, additive
merge into their governing project instructions or law index.

An installed consumer can use the complete template text below directly.
Reading it and creating approved project documents require no local maintenance
scripts, profile, lock or copy of the general source trees. When the source
template is available, use its structure; when only this installed entry is
available, include the same boundary text while drafting the project laws.
Missing other skeleton inputs remain separate pending work.

```markdown
## CDD Source and Target Project Boundaries

These rules distinguish the CDD Source library from a business project using its
installed platform files; Source-only restrictions do not govern the business
project's own code, documents or delivery evidence.

“严格分离”“不混入”“仅保留”约束的是 Git 跟踪、暂存、提交及发布的文件内容集合，与本地存放目录无关。
In these CDD boundaries, "strict separation", "must not mix" and "only retain"
constrain the content selected for Git tracking, staging, commits and delivery/
publication, not directory layout or local disk presence. CDD templates, platform
projections and maintenance material may remain inside or outside either repository
and be discovered, loaded, take effect and be used under existing authorization.
Git exclusion and ignore rules are not runtime loading controls. Local presence
alone is not a violation and must not trigger moving, deleting or relocating logs.
不进入 Git 并不禁止经授权的本地保留、发现、加载、生效和使用。

Before submission or publication, review the actual changed content, Git index
and intended delivery set. Use precise shared `.gitignore` rules against accidental
addition of untracked maintenance files; they do not remove tracked/staged content
or prevent forced addition or separate publication. Already-tracked maintenance
content needs separately authorized exclusion from tracking/delivery while keeping
recoverable originals. This rule alone grants no such action.

### CDD source library

The Source library submits development templates and necessary template-use
instructions/support. Exclude template-maintenance tools, checkers, maintenance
fixtures, maintenance-only annotations (including hidden comments), actual
maintenance reports/logs and other maintenance-process records from that set.
Substantive template-use rules and reusable report/test templates remain eligible;
they are distinct from maintenance notes and actual execution records. Ordinary
template use must not depend on the local maintenance toolkit.

In the actual CDD Source, delivered developer templates and their complete platform
projections are framework product assets. A Target copy does not gain that Source
role, and Source-local maintenance tools/procedures do not become product assets.

### Target business project

A target project submits project-owned skills, agents/roles, tools, configuration,
business code, substantive documents, tests and QA/history under its own rules,
including its development capabilities. Its CDD-related Git set contains only
minimal required adaptations and independent portable configuration without CDD
framework instruction bodies or exclusive support. Confirmed reusable CDD templates,
generic standards/workflow originals and `skill_testing/` assets remain local-only.

**Confirm asset ownership before instruction purpose.** Apply
`standards/skill-purpose.md` after establishing actual CDD framework provenance,
ownership and delivery role for the complete package and its required support.
Classify purpose only within that confirmed CDD asset collection. Project-owned
skills, agents/roles, tools, configuration and documents follow their project's
rules, including development capabilities; development use, native instruction
fields and skill-directory placement do not make them CDD assets. Renaming or
tailoring a CDD template does not itself change its ownership. Unresolved ownership
stays pending only for the affected action.

Confirmed CDD developer templates, full platform projections and exclusive support
remain local-only in a Target, excluded from Git tracking/staging/commits/delivery/
publication. Within that CDD collection, inspect complete bodies, conditional
branches and direct/indirect support; split mixed CDD/project content before
submission. Native `developer_instructions` fields and standalone roles receive
the same ownership review even without a skill dependency. Minimal adaptations
and independent configuration must not carry or reconstruct CDD framework
instruction bodies or exclusive support; a native loader alone does not qualify
a copied CDD role as independent configuration. This CDD-related restriction does
not exclude independently established project-owned development skills or roles.
Names/fields such as test or release do not decide ownership or purpose.

Git exclusion does not disable authorized local retention, discovery, loading,
effect or use. Preserve complete required local CDD inputs at usable paths; an
input allowlist does not grant them Git eligibility. Missing/unread required
originals leave the affected CDD workflow pending. A fresh Target clone may need
those inputs provisioned separately. Review Git candidates separately from local
inputs and update-write scope. Ordinary template use must not depend on a local
maintenance toolkit, reader, lock, live Source or Source ADR reader; optional
authorized local maintenance operations remain allowed.

Do not submit a general CDD source mirror, template-maintenance tools/annotations,
tool-only metadata, maintenance locks/caches or actual template-maintenance output.
The designated CDD Source owns general CDD definitions independently of local
storage. Local copies alone do not establish Source authority or authorize moving,
deleting or changing log paths.

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

Business build/runtime files, tests, control manifests, design/production documents
and genuine business QA, acceptance and historical evidence remain governed by
the project's own rules. Classify by purpose and delivery role, not words such as
"maintenance", a hash or selector. Ordinary installed-platform use must work
without a local CDD maintenance reader, tool or lock. Updates still require the
actual Source identity, covered write authority, independent review of the exact
delivery and preservation of project customizations and recoverable before bytes.

These boundaries grant no moving, deletion, untracking, history-rewrite, log-path,
commit, push or publication authority. Existing collaboration, approval and
safety rules remain controlling. They do not ratify project laws, accept ADRs,
initialize governance, advance stages or establish execution/qualification evidence.
```

## Phase 1: Silent State Detection

Before asking anything, gather context silently. Do NOT show these results
unprompted — they inform your recommendations, not the conversation opener.

Check each of these and classify the project into one of 6 stages:

| Check | What to look for |
|-------|-----------------|
| Constitution exists? | `memory_bank/t0_core/basic_law_index.md` |
| Concept doc exists? | `design/cdd/game-concept.md` or `design/cdd/product-concept.md` |
| Tech prefs configured? | `standards/technical-preferences.md` (not `[CHOOSE]` or `[TO BE CONFIGURED]`) |
| Module index exists? | `design/cdd/module-index.md` |
| CDDs exist? | `design/cdd/*.md` (excluding concept, index, principles) |
| ADRs exist? | `docs/architecture/adr-*.md` |
| Architecture doc exists? | `docs/architecture/architecture.md` |
| Source code exists? | `src/` has source files |
| Production artifacts? | `production/sprints/`, `production/epics/` |
| Current stage? | `production/stage.txt` |
| Prototypes exist? | `prototypes/` has subdirectories |
| Review mode set? | `production/review-mode.txt` |

**Stage classification:**

| Stage | Detection |
|-------|-----------|
| **0. Empty** | No concept doc, no source, no ADRs |
| **1. Concept only** | Concept doc exists, no module index, no ADRs, no constitution |
| **2. Designed** | Module index + CDDs exist, no or few ADRs |
| **3. Architected** | ADRs exist, architecture doc may exist |
| **4a. Source only** | Source code exists, no production artifacts (no `production/sprints/`, no `production/epics/`) |
| **4b. Implemented** | Source code + production artifacts both exist |
| **5. Constitution exists** | `memory_bank/t0_core/basic_law_index.md` exists |

**Priority rule**: If `basic_law_index.md` exists, classify as Stage 5 first regardless
of what else is present. Then inspect concept doc, CDDs, ADRs, and source changes
inside Stage 5 to determine what the returning user needs (audit, amend, or revise).

---

## Phase 2: Route Based on Detected Stage

After Phase 1 determines the current stage, read only the matching stage section in [stage routing](references/stage-routing.md). Apply that route before entering Phase 3 or any later workflow. The reference contains the stage-specific questions, artifact rules, and return-user behavior.

## Phase 3: Interactive Legislation (from scratch)

Enter only through the selected stage's manual/formalize route. Before the
questions/drafts, Read [Interactive Legislation](references/interactive-legislation.md)
through Phase 3e. Reuse an established domain; ask only if unresolved. Gather
Project Name, Core Thesis (BL-01) and Anti-Thesis, then 3-5 falsifiable principles
with tension, current-state requirement and design test (BL-02 through BL-06).

New laws are Proposed. Keep the full inline boundary separate from numbered laws.
Covered draft writes use `memory_bank/t0_core/active_context.md` at 0.1 (Draft),
`memory_bank/t0_core/basic_law_index.md` and selected T1 context paths. Review-mode
choice/persistence is a separate effect at `production/review-mode.txt`.

Present the exact complete constitution for explicit Ratify / Revise first /
Leave as Draft choices. Only verified ratification of that precise law set grants
Accepted statuses, version 1.0, actual sign-off/changelog and separately covered
README/context writes. Draft/content/write approval is not ratification. A draft
remains 0.1 (Draft)/Proposed until that authority exists.

### Phase 3e.1: Memory Bank Control Plane Skeleton

Before naming, authorizing or writing any skeleton effects, Read the complete
selected initialization checklist and operations in
[Memory Bank Initialization](references/initialization-inputs.md). It owns every
T0-T3 output path, neutral original, mirror and mount operation. Interactive
initialization follows ratification; Phase 4 also uses it for separately authorized
derived skeletons without accepting Proposed laws.

Read actual delivered `templates/memory-bank/` originals, `docs/PHASE-CHECKLISTS.md`,
`workflow/generated/gate-required-artifacts.md`, catalog, listed `skill_testing/`
assets and required indirect owners before dependent writes. Missing/unread or
placeholder substitutes leave affected files pending. Preserve project-owned
content/customizations, recoverable before bytes and complete local-use closure;
required CDD inputs remain separate from Target Git candidates. Ordinary offline
initialization does not require a maintenance kit or live Source.

Only when import/update/layout migration is selected, apply
`standards/directory-structure.md`'s consumer layout owner first: verify latest
applicable Source inputs, resolve the complete consumer tree/old-new mapping and
keep ambiguous destinations pending before affected writes. Old paths or an
internally consistent installation do not prove current alignment. Bind actual
observed installed paths/effects separately from proposed/unresolved destinations
in `memory_bank/t2_execution/framework_contract.md`.

Copy `adapter_state.yaml` from its matching template unchanged. It must remain
exactly `uninitialized`: no fabricated digests, commit, timestamp, check command
or fresh result. Leave unresolved bindings explicitly unconfigured. Use ordinary
file tools for delivered mirrors and leave a missing view's mirror pending;
maintenance scripts are not a prerequisite for constitution initialization.
Recommend `/constitute-check` only after actual covered writes/readback; unavailable
Source/checks preserve state and leave live freshness unavailable.

### Phase 3f: Handoff After Interactive Legislation

Before the handoff, Read Phase 3f in
[Interactive Legislation](references/interactive-legislation.md). For clear-spec
formalization with no concept, route directly to `/brainstorm [your spec]` to
create the Game/Product concept, then return to `/constitute`. Do not use Stage
1a routing that assumes an existing concept. The return with an existing
constitution and new concept uses Stage 5 Revise from source -> Phase 6 amendment.

## Phase 4: Auto-Derivation Workflow (from existing artifacts)

Before collecting/deriving source sections, Read
[Constitution Derivation Workflow](references/derivation-workflow.md). Read actual
concept/CDD/ADR/configuration bodies for the chosen stage and extract each element
from its named owner; show/edit/skip each proposed section within the actual scope.
Keep these legal and version controls in force for every derived section:

Include the reusable source/target boundary section in the law-index draft
submitted for approval. Its inclusion does not make it an already-approved
source-derived law or ratify new project laws. Write each approved section to
the appropriate `memory_bank/` file immediately.
Create directories as needed. All newly derived laws start as `Status: Proposed`.
Concept/content approval and permission to write the law index do not accept laws.
Independently verify any existing law-acceptance authority against the exact
presented text/revision, Support IDs and scope before recording `Accepted`;
retain the matching authority/date/evidence and preserve prior history.
When that authority is absent or does not match, keep the laws Proposed and use
Phase 3e to present the exact law set for explicit ratification. Reuse verified
matching ratification authority without asking again; missing acceptance stays
pending, never inferred from concept approval or a successful file write.

Write the actual version/status to `active_context.md`: use version 0.1 (Draft)
while initial derived laws remain Proposed; version 1.0 requires the separately
verified ratification above. Append the derivation source entry:
`Initial constitution derived from concept doc and [N] CDDs / [M] ADRs`.
Record content/write approval separately from exact law-acceptance sign-off.
Only a verified ratification records its actual authority, scope and date; do not
manufacture sign-off or reuse a concept approval as the acceptance record.

Before any included skeleton writes, read and apply Phase 3e.1's full checklist.
Populate maps/current state/workflow/T1 indexes only from actual evidence; otherwise
retain clear missing/not-started placeholders.

Report Draft versus ratified status explicitly. A draft cannot satisfy a gate
requiring Accepted laws. Review-mode persistence has its own path/effect authority.
Use the stage-aware handoff in the reference and the current catalog in Phase 7;
recommendations execute no command or transition.

## Phase 5: Alignment Report (standalone audit)

For a standalone alignment audit over an existing constitution and CDDs/ADRs/code,
before reporting Read only Step 4d in
[Constitution Derivation Workflow](references/derivation-workflow.md). Use its
actual version/Draft status, Principles, Gaps and ALIGNED/NEEDS ATTENTION format;
this does not select the derivation/write route. Stage 3-4 audits use the same
report. A missing inline source/target boundary in actual governing instructions
or law index is an additive merge proposal; the audit does not write it.

---

## Phase 6: Amendment Workflow

Amendments are triggered when:
- User selects "Amend constitution" (Stage 5)
- User selects "Revise from source" (Stage 5)
- Concept document has changed (Stage 3-4 with existing constitution)
- `/constitute-check` flags stale principles
- User explicitly requests amendment

Before comparing or proposing changes, Read
[Constitution Amendment Workflow](references/amendment-workflow.md). Read the
current law index/active context and changed source originals, then show exact
changed/new/deprecated drafts, Support IDs, rationale, old/new impacts and unchanged
principles. User review of each precise legal action is separate from file writes;
reuse only verified exact matching authority. Rejected changes retain the binding
prior law. Missing acceptance keeps a Proposed amendment without changing it.

Only with both exact acceptance/amend/supersede authority and covered write effects:
retain changed laws' Support IDs, assign new IDs to new laws, record actual
Accepted/amended/superseded/deprecated status and preserve prior versions/history.
Name each law-index, active-context version/changelog/sign-off, amendment-log and
T3 amendment-evidence effect in the authorized changeset. Use the reference's
unique version/date/suffix evidence naming rather than overwriting prior records.
Record trigger, rationale, rejected alternatives, approval, impacted T1/T2/T3 files
and follow-up checks. Read back actual effects before reporting completion and
surface downstream review impacts; no implicit dependent repair or publication.

## Phase 7: Pipeline and Hand Off

Show the journey for the actual selected stage and resolved domain. Read
`workflow/workflow-catalog.yaml` for the current complete order, applicability,
required/optional/required_when flags and phase boundaries. The navigation below
does not replace that body or promote optional steps into blockers. Missing/unread
catalog leaves route recommendations incomplete. Present all applicable steps:

Materialize the catalog's complete applicable steps and artifacts for Concept,
Systems Design / Specification, Technical Setup / Architecture, Pre-Production /
Pre-Implementation, Production / Implementation, Polish / Verification and
Release. Show each required gate and surface condition with the actual commands;
do not substitute a remembered abbreviated pipeline. Include accessibility from
`templates/accessibility-requirements.md`, configured test baseline, applicable
UX/surface work and actual implementation/readiness/closure steps as owned there.
Preserve three cumulative Game playtests or Product validation sessions in the
Polish/Verification scope. Release communications `/changelog` and `/patch-notes`
remain optional; `/hotfix` is emergency-only.

`/qa-plan` is optional by default; `/smoke-check` follows its actual owning scope,
not a replacement for catalog evidence. Apply actual explicitly selected strict
obligations without inventing them from review mode.

- **Stage 0**: preserve the chosen Starting Fresh route. A may `/brainstorm` first
  and return for principles; constitution work remains required before the Concept
  boundary. Clear-spec formalization uses Phase 3f, not a route assuming a concept.
- **Stage 1**: concept review -> Concept gate -> `/map-systems`, then Systems
  Design / Specification.
- **Stage 2a**: `/map-systems next` or `/design-system` for incomplete MVP CDDs,
  then `/design-review` and remaining Systems Design work.
- **Stage 2 (Designed)**: without ADRs, `/review-all-gdds` -> Systems Design gate
  -> `/setup-engine`; with ADRs, use the next applicable architecture step.
- **Stages 3-5**: highlight the next actually incomplete phase; show the complete
  catalog route for context. Declared phase, counts and existing files are not
  qualified completion or permission to skip gates.

Use `AskUserQuestion` with 3-4 concrete stage-appropriate next steps and
`Something else`. When confirmed, say "Type `[skill command]` to begin."
Recommendations execute no command, legal acceptance or transition.

Verdict: **COMPLETE** only for the actually handled selected route and its
required reads/checks/authorized effects. Report incomplete or pending portions
precisely; a completed draft/browse/handoff does not establish Accepted laws,
installed updates, fresh adapters, publication or a qualified project stage.

---

## Collaborative Protocol

1. **Detect first** — never assume the project stage
2. **Derive when possible** — extract from existing artifacts rather than asking from scratch
3. **Present diffs** — show old vs new when amending
4. **Section-by-section approval** — each constitutional element approved individually
5. **Track versions** — every write bumps the version and logs the change
6. **Record sign-off** — every ratification or amendment records who approved it and when
7. **Flag impacts** — after amendments, note what downstream artifacts need review
8. **No auto-execution** — recommend next skill, don't run it without asking

Next steps: use the selected stage's actual catalog handoff in Phase 7; unresolved
required inputs/actions remain explicit before any later `/gate-check`.
