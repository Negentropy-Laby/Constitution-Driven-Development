# Skill Test Spec: /gate-check

## Skill Summary

`/gate-check` validates whether the project is ready to advance to the next
development phase. It checks for required artifacts, runs quality checks, asks
the user about unverifiable items, and produces a PASS/CONCERNS/FAIL verdict.
On PASS with user confirmation, it writes the new stage name to
`production/stage.txt`. It governs all 6 phase transitions and is the most
critical gate-keeping skill in the pipeline.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings (numbered Phase N or ## sections)
- [ ] Contains verdict keywords: PASS, CONCERNS, FAIL
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end (Follow-Up Actions section)

---

## Test Cases

### Case 1: Happy Path — All Concept artifacts present, advancing to Systems Design

**Fixture:**
- `design/cdd/game-concept.md` exists, has content including all required sections
- `design/cdd/game-pillars.md` exists (or pillars defined within concept doc)
- No systems index yet (which is correct for this stage)

**Input:** `/gate-check systems-design`

**Expected behavior:**
1. Skill reads `design/cdd/game-concept.md` and verifies it has content
2. Skill checks for game pillars (in concept or separate file)
3. Skill checks quality items (core loop described, target audience identified)
4. Skill outputs structured checklist with all items marked
5. Skill presents PASS/CONCERNS/FAIL verdict
6. If PASS: skill asks "May I update `production/stage.txt` to 'Systems Design'?"

**Assertions:**
- [ ] Skill uses Glob or Read to verify `design/cdd/game-concept.md` exists before marking it checked
- [ ] Output includes a "Required Artifacts" section with check status per item
- [ ] Output includes a "Quality Checks" section with check status per item
- [ ] Output includes a "Verdict" line with one of PASS / CONCERNS / FAIL
- [ ] Skill asks about unverifiable quality items (e.g., "Has this been reviewed?") rather than assuming PASS
- [ ] Skill asks "May I write" before updating `production/stage.txt`
- [ ] Skill does NOT write `production/stage.txt` without explicit user confirmation

---

### Case 2: Failure Path — Missing required artifacts for Concept → Systems Design

**Fixture:**
- `design/cdd/game-concept.md` does NOT exist
- No game pillars document exists
- `design/cdd/` directory is empty or absent

**Input:** `/gate-check systems-design`

**Expected behavior:**
1. Skill attempts to read `design/cdd/game-concept.md` — file not found
2. Skill marks required artifact as missing (not present)
3. Skill outputs FAIL verdict
4. Skill lists blocker: "No game concept document found"
5. Skill suggests remediation: run `/brainstorm` to create one

**Assertions:**
- [ ] Verdict is FAIL (not PASS or CONCERNS) when required artifacts are missing
- [ ] Output explicitly names `design/cdd/game-concept.md` as missing
- [ ] Output includes a "Blockers" section with at least 1 item
- [ ] Output recommends `/brainstorm` as the remediation action
- [ ] Skill does NOT write `production/stage.txt` when verdict is FAIL

---

### Case 3: No Argument — Auto-detect current stage

**Fixture:**
- `production/stage.txt` contains `Concept`
- `design/cdd/game-concept.md` exists with content
- No systems index yet

**Input:** `/gate-check` (no argument)

**Expected behavior:**
1. Skill reads `production/stage.txt` to determine current stage
2. Skill determines the next gate is Concept → Systems Design
3. Skill proceeds with the Systems Design gate checks
4. Output clearly states which transition is being validated

**Assertions:**
- [ ] Skill reads `production/stage.txt` (or uses project-stage-detect heuristics) to determine current stage
- [ ] Output header names both current and target phases (e.g., "Gate Check: Concept → Systems Design")
- [ ] Skill does not ask the user which gate to check if current stage is determinable

---

### Case 4: Edge Case — Manual check items flagged correctly

**Fixture:**
- All required artifacts for Concept → Systems Design are present
- No playtest or review record exists (can't auto-verify quality checks)

**Input:** `/gate-check systems-design`

**Expected behavior:**
1. Skill verifies all artifact files exist
2. Skill encounters quality check: "Game concept reviewed (not MAJOR REVISION NEEDED)"
3. Since no review record exists, skill marks item as MANUAL CHECK NEEDED
4. Skill asks the user: "Has the game concept been reviewed for design quality?"
5. Skill waits for user input before finalizing verdict

**Assertions:**
- [ ] Items that cannot be auto-verified are marked `[?] MANUAL CHECK NEEDED` rather than assumed PASS
- [ ] Skill uses a question to the user for at least one unverifiable quality item
- [ ] Skill does not mark unverifiable items as PASS by default

---

---

### Case 5: Director Gate — lean vs full vs solo mode

**Fixture:**
- `production/review-mode.txt` exists with an actual valid value
- All required artifacts for the target gate are present
- `design/cdd/game-concept.md` exists

**Case 5a — full mode:**
- `review-mode.txt` contains `full`

**Input:** `/gate-check systems-design` (with full mode active)

**Expected behavior:**
1. Skill reads review mode — determines `full`
2. Skill spawns all 4 PHASE-GATE director prompts in parallel:
   - CD-PHASE-GATE (creative-director)
   - TD-PHASE-GATE (technical-director)
   - PR-PHASE-GATE (producer)
   - AD-PHASE-GATE (art-director)
3. If one director returns CONCERNS → overall gate verdict is at minimum CONCERNS
4. All 4 verdicts are collected before producing final output

**Assertions (5a):**
- [ ] Skill reads review-mode before deciding which directors to spawn
- [ ] All 4 PHASE-GATE director prompts are spawned (not just 1 or 2)
- [ ] Directors are spawned in parallel (simultaneous, not sequential)
- [ ] A CONCERNS verdict from any one director propagates to overall verdict
- [ ] Verdict is NOT auto-PASS if any director returns CONCERNS or REJECT

**Case 5b — solo mode:**
- `review-mode.txt` contains `solo`

**Input:** `/gate-check systems-design` (with solo mode active)

**Expected behavior:**
1. Skill reads review mode — determines `solo`
2. Each director is noted as skipped: "[CD-PHASE-GATE] skipped — Solo mode"
3. Gate verdict is derived from artifact/quality checks only
4. No director gates spawn

**Assertions (5b):**
- [ ] No director gates are spawned in solo mode
- [ ] Each skipped gate is explicitly noted in output: "[GATE-ID] skipped — Solo mode"
- [ ] Verdict is based on artifact and quality checks only

**Note on Case 3 correction:**
The Case 3 assertions previously stated "Skill does not ask the user which gate to check
if current stage is determinable." This is correct. However, the skill DOES use
AskUserQuestion to confirm the auto-detected transition before running full checks —
this is a confirmation step, not a gate selection. Assertions for Case 3 should not
treat this confirmation as a failure.

---

## Protocol Compliance

- [ ] Reuse covered exact stage transition/path authority; ask "May I write" only for missing/new effects, preserving actual gate truth
- [ ] Presents the full checklist before any missing/new write-scope question; covered authority continues without repeated confirmation
- [ ] Ends with a "Follow-Up Actions" section listing next steps per verdict
- [ ] Stage advancement requires covered existing/new exact transition authority and governing conditions; report/content approval alone cannot grant it
- [ ] Creating absent `production/stage.txt` needs that exact covered create/transition effect; otherwise ask for new scope, without inventing gate PASS

---

## Review Mode Validation Counterexamples

- Valid explicit full/lean/solo overrides valid global; valid global applies when
  explicit absent; only both absent falls back to lean.
- Present `--review` without a value, an invalid value, or existing empty/invalid
  `production/review-mode.txt`: stop before gates/skips/state or closure writes;
  name invalid source and ask correction. No silent lean or invented gate result.

## Shared Contract Cases

Owners: project-root `standards/evidence-lifecycle.md`,
`standards/notes-adr-sync.md` and the canonical skill's QA policy.
Evaluate this skill's own actions/findings/recommendations, without
treating planning or uninvoked closure workflows as runtime execution.

### Case 6: Exact QA policy and closure counterexamples

**Fixture:**
Separate variants: default optional orchestration with actual required PASS;
explicit strict check unavailable; one required AC untested or Must Have blocked;
legacy RISKS label with passing vs failing required facts; report-only/self-review/
stale or missing originals/Unknown scope; exact permitted historical results.

**Input:** `/gate-check` with each stated policy/evidence variant

**Expected behavior:**
1. Read the actual catalog, owning requirements and each variant's policy/authority/evidence.
2. Keep sufficiency, operation finish, execution, risk acceptance and completion separate.
3. Report only eligible scope and remaining required owner/actions.

**Assertions:**
- [ ] Default optional plan/team orchestration, every required AC/check actual PASS: no invented
      strict gate; optional follow-up retains owner/due phase.
- [ ] Explicit selected strict check unavailable: actual source/authority/scope recorded;
      NotRun/Blocked/Pending prevents dependent qualification/closure. Review mode or missing QA
      Context cannot silently invent/waive strict or passing status.
- [ ] One required AC untested (even below 50%) or Blocked Must Have: no eligible Story
      COMPLETE/COMPLETE WITH NOTES/done or all-complete message. Optional orchestration waives no
      required behavior. Planning cases/ADEQUATE review is not execution.
- [ ] Legacy COMPLETE WITH RISKS aliases NOTES only after every required actual PASS/
      decision/review/completion authority fact verified; original label preserved.
      Failed/unexecuted scope stays BLOCKED with separate risk acceptance.
- [ ] Report-only authority, self-review, explicit gate skip, unbound/stale evidence, missing
      original or Unknown scope leaves required dependent findings incomplete; no index/state/phase
      repair or broadened partial-scope approval.
- [ ] Exact permitted historical results retain original runtime/observer/inputs/scope and
      historical label, never this run's execution. Performance, required distinct sessions, target-
      platform/Product qualification need actual bound observations; file counts/keywords/line
      quotes/assumptions do not prove them.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 7: Optional context absence

**Fixture:**
No Memory Bank/QA Context exists; no strict selection is recorded. A separate
variant has actual conflicting policy or unresolved required applicability.

**Input:** `/gate-check` under the stated scope

**Expected behavior:**
1. Read actual catalog/defaults and required owning inputs.
2. Continue unaffected work without initializing optional context.

**Assertions:**
- [ ] No Memory Bank/QA Context exists and no explicit strict selection is recorded: use actual
      catalog default optional orchestration, disclose optional absence and continue required
      Story/DoD/evidence checks. Do not invent Unknown policy, a strict gate, passing execution,
      initialization or stage/closure authority. Actual conflicting policy or unresolved required
      applicability remains Unknown for dependent claims.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 8: Continuing named authority

**Fixture:**
Existing user approval names the exact output path and create/update effect.
A variant authorizes only a report, excluding inputs/index/status/closure; another
introduces a materially new effect. Current input identities are supplied.

**Input:** `/gate-check` under the stated scope

**Expected behavior:**
1. Match current inputs and planned effects to the retained approval.
2. Execute covered effects and request only missing material scope.

**Assertions:**
- [ ] An existing user-authorized changeset already names this exact output path and create/update
      effect. Reuse that authority through roles/retries and proceed after required facts/reviews
      pass; do not ask "May I write" again for the same scope. Missing authority or a materially new
      path/effect asks once after a concrete draft. A new report alone does not cover
      input/index/status/closure effects; director or content approval does not independently
      authorize writes.

**Case Verdict:** PASS / FAIL / PARTIAL

## Coverage Notes

- The Production → Polish and Polish → Release gates are not covered here
  because they require complex multi-artifact setups (sprint plans, playtest
  data, QA sign-off); these are deferred to dedicated follow-up specs.
- The "CONCERNS" verdict path (minor gaps, not blocking) is not explicitly
  tested here; it falls between Case 1 and Case 2 and follows the same pattern.
- The Vertical Slice validation block (Pre-Production → Production gate) is not
  covered because it requires a playable build context that cannot be expressed
  as a document fixture.
