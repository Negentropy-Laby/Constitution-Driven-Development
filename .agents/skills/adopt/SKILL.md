---
name: adopt
description: "Brownfield onboarding — audits existing project artifacts for template format compliance (not just existence), classifies gaps by impact, and produces a numbered migration plan. Run this when joining an in-progress project or upgrading from an older template version. Distinct from /project-stage-detect (which checks what exists) — this checks whether what exists will actually work with the template's skills."
argument-hint: "[focus: full | cdds | adrs | stories | infra]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, AskUserQuestion
agent: technical-director
---
Read and apply `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`,
`standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md` for scoped
authority, exact evidence and decision ownership. Existing named authority
continues; analysis is read-only and report-only excludes input/index/state writes.


## Reading, scope and acceptance controls

References ship with this package and resolve relative to this entry. Read the
matching mode/phase sections before their work; links and summaries do not count
as reads. Missing, unread or truncated required content leaves affected checks
INCOMPLETE, outside the compliant count. Complete long sections in consecutive
bounded chunks (at most 8,000 UTF-16 units per result); do not force all references
into every subset mode.

Standalone format audits use complete installed entries and neutral originals
offline. Only explicitly selected import/update/layout migration resolves the
latest applicable actual Source, complete consumer target tree and old/new mapping
under `standards/directory-structure.md`; unselected alignment is NotAssessed.
A plan is advisory: its authority covers no repair, review-mode persistence,
law/ADR acceptance, Story/stage completion or other state write. Zero real gaps
produce no invented tasks; unread required inputs never become zero-gap evidence.

## User Guide

- When to use: Brownfield onboarding — audits existing project artifacts for template format compliance (not just existence), classifies gaps by impact, and produces a numbered migration plan. Run this when joining an in-progress project or upgrading from an older template version. Distinct from /project-stage-detect (which checks what exists) — this checks whether what exists will actually work with the template's skills.
- Inputs: Command arguments: `/adopt [focus: full | cdds | adrs | stories | infra]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Adopt — Brownfield Template Adoption

This skill audits an existing project's artifacts for **format compliance** with
the template's skill pipeline, then produces a prioritised migration plan.

**This is not `/project-stage-detect`.**
`/project-stage-detect` answers: *what exists?*
`/adopt` answers: *will what exists actually work with the template's skills?*

Existing CDDs/ADRs/Stories may lack required substantive contracts or exact
identity. Report the actual affected gap; do not claim already-repaired consumers
silently auto-pass, or certify runtime behavior from an artifact format.

**Output:** `docs/adoption-plan-[date].md` — a persistent, checkable migration plan.

**Argument modes:**

**Audit mode:** `$ARGUMENTS[0]` (blank = `full`)

- **No argument / `full`**: Complete audit — all artifact types
- **`cdds`**: CDD format compliance only
- **`adrs`**: ADR format compliance only
- **`stories`**: Story format compliance only
- **`infra`**: Infrastructure artifact gaps only (registry, manifest, sprint-status, stage.txt)

---

### Skill purpose before adoption

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

Identify the governed project/product and the user's task. This CDD adoption
workflow is a local-only Target template; Source delivery is a separate framework
product role. In relevant modes classify product-use/development-only/mixed/
unresolved only within confirmed CDD packages, using complete bodies and references
before Git selection. Preserve project-owned development skills, independent roles,
tools, configuration and documents under project rules. Split confirmed CDD content
and exclusive support from project-owned candidates; tailoring does not change CDD
ownership. Keep required local packages complete. Existing tracked CDD reconciliation
needs its governance gate and separate exact-path tracking-only migration authority,
with local originals, reference closure, customizations and Git history preserved.
This audit grants no migration/untracking.

### Project boundary delivery in full and infra adoption

For `full` and `infra`, read the project's actual governing instructions or
law index and the complete installed `constitute` entry's "Reusable Project
Boundary Template". The reusable source is
`templates/memory-bank/t0_core/basic_law_index.md`; its boundary text is also
carried inside that installed entry, so a local maintenance kit or copied
general source tree is not an audit prerequisite.

If the two owner scopes are missing, include an additive merge into the actual
project-owned instruction file, or into an already-authorized
`memory_bank/t0_core/basic_law_index.md`, in the migration plan. Preserve business
code, project design/QA/acceptance documents, histories and existing authorities.
Prepare required neutral templates/spec assets for authorized local use, following
their actual reference closure under `adapters/README.md`. Review Target Git
candidates separately. Project-owned skills/roles, including development
capabilities, tools, configuration and substantive documents follow project rules.
Within the CDD-related candidate set, minimal adaptations and independent portable
configuration must not carry/reconstruct CDD framework instruction bodies or
exclusive support. Confirmed CDD templates and required local inputs remain usable
for authorized discovery, loading, effect and use but do not gain Git eligibility
from being required. Missing/unread required originals leave affected use
incomplete. Exclude general CDD source mirrors and template-maintenance materials
from Target Git tracking/staging/commits/delivery/publication; ignore rules do not
control runtime loading.
Local presence inside or outside the project is allowed; it does not justify
a move, deletion, log-path change or untracking. Review actual diffs/index and
delivery contents; ignore rules alone do not exclude already-tracked material.
Plan approval does not authorize that merge, activate Memory Bank or accept laws.
If the installed boundary text is missing, report that precise delivery gap.

When requested `full` or `infra` scope includes CDD import/update or layout
migration, read `standards/directory-structure.md`, section "Consumer layout
resolution for imports and updates", before resolving the plan or proposing
affected writes. Bind the verified latest applicable Source inputs and resolve
the consumer tree/mapping under that owner. Missing Source or conflicting
requirements leave only the affected layout action pending; do not freeze an old
path as a customization exemption. A standalone artifact-format audit is not an
implicit framework update: complete installed inputs remain usable offline, with
unselected layout alignment NotAssessed and live freshness separately unavailable.

## Phase 1: Detect Project State

Emit one line before reading: `"Scanning project artifacts..."` — this confirms the
skill is running during the silent read phase.

Then read silently before presenting anything else.

### Existence check
- `production/stage.txt` — read declared phase; verify relied-on transition evidence
  separately, without inferring qualification from the value/path
- `design/cdd/game-concept.md` or `design/cdd/product-concept.md` — concept exists?
- `design/cdd/module-index.md` — module index exists?
- Count CDD files: `design/cdd/*.md` (excluding game-concept.md, product-concept.md, module-index.md, and principles.md)
- Count ADR files: `docs/architecture/adr-*.md`
- Count story files: `production/epics/**/*.md` (excluding EPIC.md)
- `standards/technical-preferences.md` — technology stack configured?
- `docs/engine-reference/` or `docs/reference/` — reference docs present?
- Glob `docs/adoption-plan-*.md` — note the filename of the most recent prior plan if any exist

### Candidate phase
Read `standards/technical-preferences.md` domain/capability evidence and concept
bodies; missing/ambiguous concepts never default Game. Use advisory indicators
from `/project-stage-detect`, not completion proofs. Phase names are shown as
**[游戏专用] Game** / **[通用产品] Product**:

- Actual ongoing implementation evidence → candidate Production / Implementation;
  source counts indicate scale only
- Stories in `production/epics/` → Pre-Production / Pre-Implementation
- ADRs exist → Technical Setup / Architecture
- module-index.md exists → Systems Design / Specification
- game-concept.md or product-concept.md exists → Concept
- Nothing → Fresh (not a brownfield project — suggest `/constitute`)

If the project appears fresh (no artifacts at all), use `AskUserQuestion`:
- "This looks like a fresh project — no existing artifacts found. `/adopt` is for
  projects with work to migrate. What would you like to do?"
  - "Run `/constitute` — establish project governance and route to the right workflow"
  - "My artifacts are in a non-standard location — help me find them"
  - "Cancel"

Then stop — do not proceed with the audit regardless of which option the user picks
(each option leads to a different skill or manual investigation).

Report declared phase, observed artifacts, candidate phase and verified qualified
state separately, including CDD/ADR/Story counts. Missing qualification stays
unverified; this format audit does not execute runtime skills.

---

## Phase 2: Format Audit

For each artifact type in scope (based on argument mode), check not just that
the file exists but that it contains the internal structure the template requires.

Audit CDDs in `cdds` or `full`, and infrastructure in `infra` or `full`.
Other subset modes cover only their actual artifact types; a full audit includes
all applicable types. If the argument or applicability is unresolved, retain
Unknown; missing required inputs do not justify skipping their audit. Audit scope
grants no repair, status or runtime authority.

Before checking each selected type, Read its applicable checklist section:

| Audit mode | Required sections before the corresponding audit |
|---|---|
| `full` | All applicable 2a-2f sections below; missing required owners remain incomplete |
| `cdds` | 2a CDD and 2c actual module-index owners in [CDD/ADR Checklists](references/audit-checklists.md) |
| `adrs` | 2b ADR in [CDD/ADR Checklists](references/audit-checklists.md) |
| `stories` | 2d Story in [Story/Infrastructure Checklists](references/story-infra-checklists.md) |
| `infra` | 2e infrastructure and 2f preferences in [Story/Infrastructure Checklists](references/story-infra-checklists.md), plus the installed boundary owner above |

Read only the selected sections/domain and their actual required originals.
Resolve DocKind through `design/INSTRUCTIONS.md`: module semantic eight retains
substantive aliases; Concept, Module Index and other kinds use their actual owners.
Neither headings nor status labels establish approval; retain history and exact
evidence. Missing/unread required bodies cannot be excluded to manufacture compliance.

### Per-artifact Format Tallies

Record each in-scope CDD, ADR and Story as format-compliant, with gaps, or
unverified, naming missing roles/inputs. Count each document once even with
multiple severity findings; report issue counts separately. Totals reconcile to
the actual selected inventory. A missing/unread required body cannot enter the
compliant count; an unaudited subset is NotAudited rather than zero. Valid
CDD/no-ADR dispositions and actually unassigned TR-IDs follow their owners;
do not manufacture ADRs/TR-IDs. Format tallies do not certify executed AC,
Story closure, runtime qualification or project completion.


---

## Phase 3: Classify and Prioritise Gaps

Organise every gap found across all audits into four severity tiers:

**BLOCKING** — An actual required contract/decision/evidence gap blocks its
dependent workflow or qualification; name the owner and affected scope.
Examples: a relied-on ADR missing Status, a module-index value that actually
blocks the selected downstream comparison, or missing required technology context.
A valid owner-defined alias or parenthetical note alone is not a blocking gap.

**HIGH** — Will cause stories to be generated with missing safety checks, or
infrastructure bootstrapping will fail.
Examples: ADRs missing Technology Compatibility section, CDDs missing Acceptance Criteria
(stories can't be generated from them), tr-registry.yaml missing.

**MEDIUM** — Degrades quality and pipeline tracking but does not break functionality.
Examples: CDDs missing Tuning Knobs or Formulas sections, stories missing TR-IDs,
sprint-status.yaml missing.

**LOW** — Retroactive improvements that are nice-to-have but not urgent.
Examples: Stories missing Manifest Version stamps, CDDs missing Open Questions section.

Count actual issues per tier and disclose unverified inputs separately. Only
a complete applicable audit with zero BLOCKING/HIGH findings may report no such
gaps in its selected format scope; qualification remains separately unverified.
Unread required inputs do not manufacture a zero-gap result.

---

## Phase 4: Build the Migration Plan

For a selected import/update/layout migration, first form the target-tree and
old-to-new mapping sections owned by the layout contract above. Resolve actual
role/ownership, required consumer readers and current Source requirements before
the ordered repair actions. Separate substantive preservation from old location
retention, history-only references from active dependencies, and mapping/write
authority from plan-only permission. Record unresolved destinations with their
responsible authority and affected actions; do not invent a Source-shaped target
or call an internally consistent old installation aligned. Classify actual gaps
by the existing severity/impact rules, without adding a director or phase gate.
Ordinary format-only audits omit these layout sections and do not invent work.

Compose a numbered, ordered action plan. Ordering rules:
1. BLOCKING gaps first (must fix before any pipeline skill runs reliably)
2. HIGH gaps next, infrastructure before CDD/ADR content (bootstrapping needs correct formats)
3. MEDIUM gaps ordered: CDD gaps before ADR gaps before story gaps (stories depend on CDDs and ADRs)
4. LOW gaps last

For each gap, produce a plan entry with:
- A clear problem statement (one sentence, no jargon)
- The exact command to fix it, if a skill handles it
- Manual steps if it requires direct editing
- A time estimate (rough: 5 min / 30 min / 1 session)
- A checkbox `- [ ]` for tracking

**Special case — module-index values blocking the selected workflow:**
Include only the actual affected comparison found in Phase 2c. Keep valid aliases
and historical notes; propose precise scoped treatment and retain before bytes.
Order by actual severity/dependency, without automatic label migration.

**Special case — ADRs missing Status field:**
For each affected ADR, the fix is:
`/architecture-decision retrofit docs/architecture/adr-[NNNN]-[slug].md`
List each ADR as a separate checkable item.

**Special case — CDDs missing sections:**
For each affected CDD, list which sections are missing and the fix:
`/design-system retrofit design/cdd/[filename].md`

**Infrastructure bootstrap ordering** — include only applicable missing effects,
after checking actual owners and authority, in this sequence:
1. Fix ADR formats first (registry depends on reading ADR Status fields)
2. Run `/architecture-review` → bootstraps `tr-registry.yaml`
3. Run `/create-control-manifest` → creates manifest with version stamp
4. Run `/sprint-plan update` → creates `sprint-status.yaml`
5. Run `/gate-check [phase]` → evaluate actual required evidence; stage writes
   need separately covered transition authority

**Existing stories** — note explicitly:
> Preserve in-progress/done bodies and historical labels. Missing TR/manifest
> identity needs owning-workflow legacy recheck; it never automatically passes.
> Repair approved gaps only, preserving exact reviewed baselines.

---

## Phase 5: Present Summary and Ask to Write

Present a compact summary before writing:

Before presenting the summary, Read Phase 5 in
[Adoption Summary and Plan Formats](references/adoption-plan-format.md). Show
actual per-artifact tallies, unverified paths, subset exclusions and severity
counts; format compliance never certifies runtime execution/acceptance.

Before asking to write, show a **Gap Preview**:
- List every BLOCKING gap as a one-line bullet describing the actual problem
  (e.g. `module-index.md: 3 rows have parenthetical status values`,
  `adr-0002.md: missing ## Status section`). No counts — show the actual items.
- Show HIGH / MEDIUM / LOW as counts only (e.g. `HIGH: 4, MEDIUM: 2, LOW: 1`).

This gives the user enough context to judge scope before committing to writing the file.

If a prior adoption plan was detected in Phase 1, add a note:
> "A previous plan exists at `docs/adoption-plan-[prior-date].md`. The new plan will
> reflect current project state — it does not diff against the prior run."

When exact plan authority is absent, use `AskUserQuestion` after the summary:
- "Ready to write the migration plan?"
  - "Yes — write `docs/adoption-plan-[date].md`"
  - "Show me the full plan preview first (don't write yet)"
  - "Cancel — I'll handle migration manually"

If the user picks "Show me the full plan preview", output the complete plan as a
fenced markdown block. Then request only missing write authority; matching named plan scope continues.

---

## Phase 6: Write the Adoption Plan

Reuse matching plan-only authority; missing/new authority follows Phase 5. Render
only actions for actual Phase 4 gaps. Omit empty action groups and number remaining
steps consecutively. With zero BLOCKING findings, omit the whole blocking-repair
action section; the audit summary still reports `BLOCKING: 0`. Apply the same rule
to HIGH/MEDIUM/LOW and infrastructure: valid existing registry/manifest/sprint/stage
artifacts never become fictitious bootstrap tasks. Unverified inputs remain pending
checks, not compliant facts.

Include one concrete primary recommendation and reason for every completed audit.
For a complete zero-gap audit, recommend `/project-stage-detect` for a broader
health/qualification check after reading applicable installed inputs. If these
are unavailable, report the specific input to resolve first. A recommendation
executes no repair, gate or state change.

Before previewing or writing the plan, Read the Phase 6 conditional structure in
[Adoption Summary and Plan Formats](references/adoption-plan-format.md).
If approved, write only `docs/adoption-plan-[date].md` in that format:

Keep audit summary, one concrete primary recommendation, only nonempty actual
action groups and the existing-Story/re-run guidance. Include complete resolved
consumer tree and path/ownership mapping only when import/update/layout migration
was selected; pending Source/destinations never masquerade as installed alignment.

---

## Phase 6b: Set Review Mode

Only when review-mode setup is in requested scope, check whether
`production/review-mode.txt` exists.

**If it exists**: Read/trim its actual value. Valid `full`/`lean`/`solo` may be
reused without another prompt; an empty/invalid value is reported for correction
before dependent mode claims, never silently skipped, defaulted or rewritten.

**If it does not exist**: Use `AskUserQuestion`:

- **Prompt**: "One more setup step: how much design review would you like as you work through the workflow?"
- **Options**:
  - `Full` — Director specialists review at each key workflow step. Best for teams, learning the workflow, or when you want thorough feedback on every decision.
  - `Lean (recommended)` — Directors only at phase gate transitions (/gate-check). Skips per-skill reviews. Balanced for solo devs and small teams.
  - `Solo` — No director reviews at all. Maximum speed. Best for game jams, prototypes, or if reviews feel like overhead.

Review preference is content agreement, not a hidden write effect. Reuse authority
naming `production/review-mode.txt`; otherwise show that path/effect and ask
"May I write this review mode?" before persisting:
- `Full` → write `full`
- `Lean (recommended)` → write `lean`
- `Solo` → write `solo`

Create the `production/` directory if it does not exist.

---

## Phase 7: Offer First Action

After the completed audit, whether the plan was saved or declined, name one
primary next action and explain why. Select actual gaps by severity and Phase 4
dependencies; the branches below are examples within that order. Read the selected
installed command/required inputs before an actionable recommendation. Unavailable
inputs remain explicit pending work. Use `AskUserQuestion` for unresolved follow-up
choices; no repair is auto-run.

**If a module-index value is the highest-priority confirmed blocking gap:**
Use `AskUserQuestion`:
- "The most urgent fix is `module-index.md` — [N] rows have parenthetical status
  values (e.g. `Needs Revision (see notes)`) that break /gate-check,
  /create-stories, and /architecture-review right now. I can fix these in-place."
  - "Fix it now — edit module-index.md"
  - "I'll fix it myself"
  - "Done — leave me with the plan"

**If ADRs are missing `## Status` (and no parenthetical issue):**
Use `AskUserQuestion`:
- "The most urgent fix is adding `## Status` to [N] ADR(s): [list filenames].
  Without it, required decision status/acceptance remains unverified. Start with
  [first affected filename]?"
  - "Yes — retrofit [first affected filename] now"
  - "Retrofit all [N] ADRs one by one"
  - "I'll handle ADRs myself"

**If CDDs are missing Acceptance Criteria (and no blocking issues above):**
Use `AskUserQuestion`:
- "The most urgent gap is missing Acceptance Criteria in [N] CDD(s):
  [list filenames]. Without them, /create-stories can't generate stories.
  Start with [highest-priority CDD filename]?"
  - "Yes — add Acceptance Criteria to [CDD filename] now"
  - "Do all [N] CDDs one by one"
  - "I'll handle CDDs myself"

**If only MEDIUM/LOW gaps remain:**
Name the first actual gap, its path and concrete owning command/manual action
as the primary recommendation. Optional alternatives stay secondary; do not
replace this with a generic invitation to review improvements.

**If the complete audit has no gaps:**
Recommend `/project-stage-detect` as the single primary next action for a broader
health check, explain its distinct scope and offer it as a follow-up choice. No
blocking-repair section, bootstrap task or gate invocation is generated. The
user may instead finish with the report.

---

## Collaborative Protocol

1. **Read silently** — complete the full audit before presenting anything
2. **Show the summary first** — let the user see scope before asking to write
3. **Scoped writes** — reuse named plan authority; ask only for missing/new effects.
   Plan-only excludes repairs, review mode and state.
4. **Offer, don't force** — the plan is advisory; the user decides what to fix and when
5. **One action at a time** — after handing off the plan, offer one specific next step,
   not a list of six things to do simultaneously
6. **Preserve existing bodies/history** — repair named approved gaps only;
   do not silently regenerate CDDs/ADRs/Stories or destroy unique prior content.

Read stack/version context when the selected Product audit evaluates
infrastructure, applicable ADR compatibility, or a CDD/Story contract that names
that stack. Resolve the actual stack key from configuration. Do not limit this
to infrastructure or require it for every Product subset; unresolved applicability
stays Unknown.

Read actual Product user promise/API/CLI/SDK/data/auth/workflow contracts, surface
profile and `docs/reference/[stack]/VERSION.md` as applicable. Retain Game Player
Fantasy/formulas/tuning/engine/playtest examples. Missing inapplicable infrastructure
gets justified N/A. Diagnose/offer repairs independently of plan saving; zero
BLOCKING/HIGH counts do not certify runtime/template qualification.
