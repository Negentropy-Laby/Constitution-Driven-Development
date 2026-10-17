# Skill Test Spec: /constitute

## Skill Summary

`/constitute` establishes or refreshes project governance for both game and
product projects. It replaces the deleted legacy onboarding flow. The skill reads current
artifacts, detects project stage and domain, asks structured onboarding
questions, writes T0/T1 memory bank files, and routes the user to the next
workflow step. It initializes the framework contract and deterministic
uninitialized adapter-state template without fabricating freshness evidence.

## Fixture and evidence contract

The cases below describe isolated fixture inputs. Apply the complete current
`/skill-test` owner and `standards/evidence-lifecycle.md`: spec reasoning,
static structure checks, fixture execution and independent review are separate
results. An expected result or fixture description is not a recorded runtime PASS.

Before execution, bind the selected runtime entries, actual governing project
instructions, configuration and required direct/indirect input bytes. Use
`standards/technical-preferences.md` as the canonical preference path.
Read substantive bodies; missing/unread required originals leave the affected
check pending. Optional, example, future-output and inapplicable references are
not required inputs merely because their paths appear in an instruction.

Establish actual CDD provenance, ownership and Source/Target delivery role before
classifying purpose. Source developer templates and complete projections are
framework product assets. In a Target, confirmed CDD packages/support remain
local-only but readable ignored inputs may be discovered, loaded and used within
authority. Project-owned development skills, native roles, tools and documents
retain project rules. A maintenance toolkit is optional for ordinary use.

Reasoning/review-only runs invoke no write entrypoint. Any expected writer action
runs only in an isolated fixture with the exact named paths/effects approved.
Reuse matching authority without repeated per-file/section questions; report-only
covers its assigned new report and excludes inputs/indexes/state. Law/ADR acceptance,
evidence publication, runtime qualification and Story/stage completion remain
separate. Preserve before bytes and disclose unavailable checks.

---

## Static Assertions (Structural)

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Mentions that it is a stage-aware unified onboarding entry
- [ ] Detects both `design/cdd/game-concept.md` and `design/cdd/product-concept.md`
- [ ] Writes under `memory_bank/` and `production/review-mode.txt`
- [ ] Uses `AskUserQuestion` for domain and starting-point decisions
- [ ] Provides next-step routing for game and product projects
- [ ] Initializes `framework_contract.md` and `adapter_state.yaml` from templates

---

## Test Cases

### Case 1: Fresh game project

**Fixture:**
- No concept docs
- No source code
- No memory bank
- User answers domain `A game`, then starting point `A) Starting fresh`.
- `production/review-mode.txt` already contains `lean`; no review-mode write
  is needed. The user has not supplied a clear spec or requested legislation.

**Input:** `/constitute`

**Expected behavior:**
- Asks domain first and accepts "game"
- For the selected A route, recommends `/brainstorm open` before deriving principles
- Explains that the user should return to `/constitute` after concept creation
- Does not derive/write game laws in this A-route run; no constitution writes
  occur before discovery.
- Counterexample within this case: a fresh user instead selects `C) Clear spec`,
  supplies a concrete game specification, then selects `Formalize your constitution
  first`. With exact draft/skeleton write scope and actual required local originals,
  Phase 3 may draft Proposed laws before a formal concept document exists. It
  separately verifies ratification and uses Phase 3f to hand off to `/brainstorm`.
  The absence of a concept alone must not reject this legitimate route.

### Case 2: Fresh product project

**Fixture:**
- No concept docs
- No source code
- No memory bank
- User answers domain `A general product`, then `A) Starting fresh`.
- Review mode is already `lean`; there is no populated Product stack or clear spec.

**Input:** `/constitute`

**Expected behavior:**
- Asks domain first and accepts "general product"
- Uses product examples such as web app, CLI, API, library, mobile app, or data pipeline
- For this A-route fixture, recommends `/brainstorm open` with Product examples;
  later stack setup follows the selected route and current catalog, not a mandatory
  engine step for an unconfigured Product.
- Does not mention game engine as mandatory

### Case 3: Existing project with product concept

**Fixture:**
- `design/cdd/product-concept.md` has substantive User Promise, JTBD, principles,
  target CLI workflow, scope and technology context; `src/cli/` contains that work.
- No `memory_bank/t0_core/basic_law_index.md` or production tracking exists.
- User chooses `Derive constitution now`, then approves the displayed exact
  T0/T1/skeleton paths/effects. Required originals and Source-binding project facts
  are readable; law acceptance is absent and remains separately pending.

**Input:** `/constitute`

**Expected behavior:**
- Detects existing product work
- Derives constitution from User Promise, JTBD, product principles, stack context, and current source state
- Writes T0/T1 memory-bank files only after approval
- Recommends `/constitute-check` or `/project-stage-detect` as follow-up

### Case 4: Existing game project

**Fixture:**
- `design/cdd/game-concept.md` has substantive Player Fantasy, Game pillars,
  core loop, target platform and scope; combat/movement module CDDs and matching
  `src/gameplay/` bodies exist. Actual engine preferences are Godot 4 + GDScript.
- No constitution or production tracking exists.
- User chooses `Derive constitution now`; displayed exact T0/T1/skeleton write
  paths/effects are approved. Required originals are readable; draft permission
  alone grants no law acceptance.

**Input:** `/constitute`

**Expected behavior:**
- Detects game domain
- Derives laws from Game pillars, Player Fantasy, CDDs, engine setup, and current game systems
- Preserves game-specific vocabulary and next steps
- Does not convert game terms into generic product wording

### Case 5: Adapter governance initialization

**Fixture:**
- Constitution derivation and the displayed exact skeleton-write paths/effects
  are approved; any ratification is a separately verified exact law-set decision.
- The actual `templates/memory-bank/` originals listed by Phase 3e.1,
  `docs/PHASE-CHECKLISTS.md`, `workflow/generated/gate-required-artifacts.md`,
  workflow catalog and required `skill_testing/` bodies are complete/readable.
- Project-owned binding evidence supplies actual selected installed paths,
  required neutral-input closure, portable sole Source identity and retained
  customizations; unresolved facts are explicitly unconfigured.
- No existing `memory_bank/t2_execution/adapter_state.yaml`

**Expected behavior:**
- Initializes `framework_contract.md` from its matching delivered template and binds actual installed paths, required neutral inputs, project customizations and the sole external CDD Source; unresolved bindings remain unconfigured
- Copies `adapter_state.yaml` unchanged from its matching template, at `status: uninitialized` with empty digests, commit, timestamp and check command
- Does not claim adapters are fresh without running `/constitute-check`
- Recommends `/constitute-check` after writing the approved skeleton

---

### Case 6: Concept and draft approval are not law acceptance

**Fixture:**
- A Game or Product concept was approved
- Exact draft/file-write scope covers the law-index sections
- No acceptance authority covers the displayed derived law text/revision and Support IDs

**Expected behavior:**
- Newly derived laws remain `Proposed`, with initial version 0.1 (Draft)
- Derivation source and content/write approval are recorded separately from ratification
- Missing law acceptance is not manufactured from concept approval, a director recommendation or successful writing
- Presents the exact law set for Phase 3e ratification; only verified acceptance of that set allows Accepted status and its actual sign-off
- Matching existing exact acceptance authority is reused; unrelated or changed-text approval does not match
- An unratified draft does not satisfy a gate that requires Accepted laws

### Case 7: Consumer initialization from delivered neutral originals

**Fixture:**
- Selected installed entries and the Phase 3e.1 per-file neutral original set are
  delivered at usable owner paths, including complete required direct/indirect
  reference closure. Actual project/root configuration declares installed paths,
  portable sole Source binding and retained customizations. Exact skeleton-write
  scope is approved; unresolved values remain explicitly unconfigured.
- No local general `agents/` or `skills/` source trees and no maintenance scripts
- External Source is temporarily unavailable
- Variant: a required workflow view or listed skeleton original is missing while a similarly named placeholder exists

**Expected behavior:**
- Complete delivered originals support authorized offline skeleton initialization
- T2 mirrors use actual delivered `docs/PHASE-CHECKLISTS.md` and `workflow/generated/gate-required-artifacts.md` inputs through ordinary file tools
- Adapter state remains exactly the deterministic uninitialized template; Source freshness is unavailable
- The variant identifies the exact missing/unread original and leaves its affected output pending; a placeholder does not satisfy it
- Keeps approved project customizations and recoverable before bytes; never recreates general CDD source trees or installs a maintenance kit to proceed

---

### Case 8: Framework import resolves layout before affected skeleton bindings

**Fixture:**
- A Product invocation explicitly includes CDD import/update in addition to
  constitution initialization. Complete required originals and the verified latest
  applicable Source inputs are available, and exact skeleton/installation effects
  are authorized; law ratification remains a separate decision.
- An older binding points at legacy platform locations. The applicable current
  consumer contract resolves different runtime-installed locations.

**Expected behavior:**
- Reads the single layout owner in `standards/directory-structure.md` and prepares
  the resolved consumer tree and old-to-new mapping before affected writes.
- Preserves substantive content and valid changes through the mapping rather than
  freezing legacy paths or copying the Source tree. Canonical edits/projections
  follow actual Source-stage authority, not direct adapter editing.
- Binds observed installed paths/completed effects separately from planned or
  unresolved paths in `framework_contract.md`; no proposed pin becomes installed fact.
- Copies the deterministic adapter state unchanged; import, writing and structural
  agreement do not establish freshness, law acceptance or project qualification.

### Case 9: Missing update resolution does not disable independent offline use

**Fixture:**
- Start from Case 7's complete delivered initialization inputs.
- Variant A adds a requested framework update but the latest Source or an affected
  destination/ownership decision cannot be verified. Variant B requests ordinary
  offline skeleton initialization only, with no framework update or migration.

**Expected behavior:**
- A records the exact unresolved input/decision and pending affected update;
  it neither guesses a final layout nor invokes dependent installation/retirement.
- B retains Case 7's authorized offline behavior with installed inputs; it does
  not require a maintenance toolkit/live Source or certify unassessed latest alignment.
- Local copy presence alone triggers neither a physical-directory ban nor an old
  layout exemption. Independent effects proceed only within their actual authority.

---

## Protocol Compliance

- [ ] Reads before asking for writes
- [ ] Reuses matching named write authority; only missing/new paths/effects ask
  after a concrete draft or path-and-effect summary
- [ ] Keeps Game and Product routing inside the same command
- [ ] Does not reference any deleted onboarding command as an active command
- [ ] Produces clear next steps after constitution work
- [ ] Never fabricates adapter freshness evidence
- [ ] Concept/content/write approval does not accept laws; exact ratification is independently verified
- [ ] Required neutral originals remain necessary; unavailable Source alone does not block complete offline installed inputs
- [ ] Selected framework import/update resolves the consumer tree/mapping before
  affected writes; actual installed bindings and proposed destinations stay distinct
