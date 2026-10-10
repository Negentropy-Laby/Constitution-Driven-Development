# Skill Test Spec: /constitute

## Skill Summary

`/constitute` establishes or refreshes project governance for both game and
product projects. It replaces the deleted legacy onboarding flow. The skill reads current
artifacts, detects project stage and domain, asks structured onboarding
questions, writes T0/T1 memory bank files, and routes the user to the next
workflow step. It initializes the framework contract and deterministic
uninitialized adapter-state template without fabricating freshness evidence.

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

**Input:** `/constitute`

**Expected behavior:**
- Asks domain first and accepts "game"
- Routes to `/brainstorm` before deriving principles
- Explains that the user should return to `/constitute` after concept creation
- Does not write game-specific laws before a concept exists

### Case 2: Fresh product project

**Fixture:**
- No concept docs
- No source code
- No memory bank

**Input:** `/constitute`

**Expected behavior:**
- Asks domain first and accepts "general product"
- Uses product examples such as web app, CLI, API, library, mobile app, or data pipeline
- Routes to `/brainstorm` product mode or `/setup-engine` stack setup depending on user state
- Does not mention game engine as mandatory

### Case 3: Existing project with product concept

**Fixture:**
- `design/cdd/product-concept.md` exists
- `src/` has source files
- No `memory_bank/t0_core/basic_law_index.md`

**Input:** `/constitute`

**Expected behavior:**
- Detects existing product work
- Derives constitution from User Promise, JTBD, product principles, stack context, and current source state
- Writes T0/T1 memory-bank files only after approval
- Recommends `/constitute-check` or `/project-stage-detect` as follow-up

### Case 4: Existing game project

**Fixture:**
- `design/cdd/game-concept.md` exists
- Game CDDs and `src/gameplay/` exist
- No constitution exists

**Input:** `/constitute`

**Expected behavior:**
- Detects game domain
- Derives laws from Game pillars, Player Fantasy, CDDs, engine setup, and current game systems
- Preserves game-specific vocabulary and next steps
- Does not convert game terms into generic product wording

### Case 5: Adapter governance initialization

**Fixture:**
- Constitution ratification or derivation is approved
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
- Selected installed entries and required neutral originals are delivered
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

## Protocol Compliance

- [ ] Reads before asking for writes
- [ ] Asks before creating or updating files
- [ ] Keeps Game and Product routing inside the same command
- [ ] Does not reference any deleted onboarding command as an active command
- [ ] Produces clear next steps after constitution work
- [ ] Never fabricates adapter freshness evidence
- [ ] Concept/content/write approval does not accept laws; exact ratification is independently verified
- [ ] Required neutral originals remain necessary; unavailable Source alone does not block complete offline installed inputs
