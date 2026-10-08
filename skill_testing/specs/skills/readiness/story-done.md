# Skill Test Spec: /story-done

## Skill Summary

`/story-done` closes the loop between design and implementation. Run at the
end of implementing a story, it reads the story file and verifies each
acceptance criterion against the implementation. It checks for GDD and ADR
deviations, prompts a code review, updates the story status to `Complete`,
logs any tech debt, and surfaces the next ready story from the sprint. It
produces a COMPLETE / COMPLETE WITH NOTES / BLOCKED verdict and writes to
the story file and optionally to `docs/tech-debt-register.md`.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥5 phase headings (complex skill warranting `context: fork` if applicable)
- [ ] Contains verdict keywords: COMPLETE, BLOCKED
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff (surfaces next story from sprint)

---

## Test Cases

### Case 1: Happy Path — All acceptance criteria met, no deviations

**Fixture:**
- Story file at `production/epics/core/story-light-pickup.md` with:
  - 3 acceptance criteria, all implemented as described
  - `TR-ID: TR-light-001` referencing a GDD requirement
  - `ADR: docs/architecture/adr-003-inventory.md` (Accepted)
  - `Status: In Progress`
- Implementation files listed in story exist in `src/`
- GDD requirement text at TR-light-001 matches how the feature was implemented
- ADR guidance was followed (no deviations)
- Required ACs have retained, matching actual PASS evidence; all selected independent
  reviews and decisions are satisfied. Exact Story closure effects are authorized.

**Input:** `/story-done production/epics/core/story-light-pickup.md`

**Expected behavior:**
1. Skill reads the story file and extracts all key fields
2. Skill reads the GDD requirement fresh from `tr-registry.yaml` (not from story's quoted text)
3. Skill reads the referenced ADR to understand implementation constraints
4. Skill evaluates each acceptance criterion (auto where possible, manual prompt where not)
5. Skill checks for GDD requirement deviations
6. Skill checks for ADR guideline deviations
7. Skill prompts user: "Please provide the code review outcome for this story"
8. Skill presents COMPLETE verdict
9. If exact story status/Completion Notes effects are not already authorized, skill asks "May I update story Status to Complete and add Completion Notes?"; covered effects proceed without another ask.
10. If yes: skill updates the story file
11. Skill surfaces an eligible `Ready` / `ready-for-dev` story from the owning sprint

**Assertions:**
- [ ] Skill reads `docs/architecture/tr-registry.yaml` for TR-ID requirement text (not just story)
- [ ] Skill reads the referenced ADR file (not just the story reference)
- [ ] Each acceptance criterion is listed with VERIFIED / DEFERRED / FAILED status
- [ ] Skill prompts the user for code review outcome (does not skip this step)
- [ ] Verdict is COMPLETE when all criteria are verified and no deviations exist
- [ ] Skill resolves exact story-write authority; asks "May I write" only for missing or materially new named effects
- [ ] Story status updates require covered existing/new authorization and eligible closure facts; content/director approval alone is insufficient
- [ ] After completion, skill surfaces the next ready story from `production/sprints/`

---

### Case 2: Blocked Path — Acceptance criterion cannot be verified

**Fixture:**
- Story file has an acceptance criterion: "Player sees correct animation on pickup"
- No automated test for this criterion exists
- Manual verification has not been performed
- All other criteria are met

**Input:** `/story-done production/epics/core/story-light-pickup.md`

**Expected behavior:**
1. Skill processes all acceptance criteria
2. Reaches the animation criterion — cannot auto-verify
3. Skill asks the user: "Acceptance criterion 'Player sees correct animation on
   pickup' cannot be auto-verified. Has this been manually tested?"
4. If user says No, required criterion is NotRun/Pending and closure BLOCKED
5. Preserve actual findings and offer only an authorized new partial report; Story/projections stay incomplete
6. Risk acceptance/write approval cannot turn the untested required AC into COMPLETE WITH NOTES

**Assertions:**
- [ ] Skill asks the user about unverifiable criteria rather than assuming PASS
- [ ] Any required unexecuted AC blocks both completion levels regardless of coverage percentage
- [ ] The deferred criterion is explicitly named in the completion notes
- [ ] Skill reuses covered exact story-write authority; missing/new scope gets a "May I write" question

---

### Case 3: Blocked Path — GDD deviation detected

**Fixture:**
- Story TR-ID points to requirement: "Player can carry max 3 light sources"
- Implementation in `src/` uses a variable `MAX_CARRIED_LIGHTS = 5`
- This is a deliberate deviation from the GDD

**Input:** `/story-done production/epics/core/story-light-pickup.md`

**Expected behavior:**
1. Skill reads the GDD requirement text (max 3)
2. Skill detects discrepancy between requirement and implementation value (5)
3. Skill flags this as a GDD deviation and asks the user to classify it:
   - INTENTIONAL: document the deviation and reason
   - ERROR: implementation must be fixed before story can be marked Complete
   - OUT OF SCOPE: requirement changed and GDD needs updating
4. If INTENTIONAL, preserve the conflict and route actual governing requirement/decision revision or valid scoped exception; eligible closure still needs actual required PASS/review/authority
5. If ERROR: verdict is BLOCKED until implementation is corrected

**Assertions:**
- [ ] Skill detects the mismatch between GDD requirement and implementation value
- [ ] Skill asks the user to classify the deviation (not auto-assumes either way)
- [ ] INTENTIONAL declaration alone resolves no required CDD/ADR conflict and grants no completion
- [ ] ERROR deviation → BLOCKED verdict until fixed
- [ ] Detected deviations are recorded in completion notes or tech debt register

---

### Case 4: Edge Case — No argument, auto-detect current story

**Fixture:**
- `production/session-state/active.md` contains a reference to
  `production/epics/core/story-oxygen-drain.md` as the active story
- That story file exists with `Status: In Progress`

**Input:** `/story-done` (no argument)

**Expected behavior:**
1. Skill reads `production/session-state/active.md`
2. Skill finds the active story reference
3. Skill reads that story file and proceeds normally
4. Output confirms which story was auto-detected

**Assertions:**
- [ ] Skill reads `production/session-state/active.md` when no argument is given
- [ ] Skill identifies and confirms the auto-detected story before proceeding
- [ ] If no story is found in session state, skill asks the user to provide a path

---

---

### Case 5: Director Gate — LP-CODE-REVIEW behavior across review modes

**Fixture:**
- Story file at `production/epics/core/story-light-pickup.md`
- All acceptance criteria verified, no GDD deviations
- `production/review-mode.txt` exists

**Case 5a — full mode:**
- `review-mode.txt` contains `full`

**Input:** `/story-done production/epics/core/story-light-pickup.md` (full mode)

**Expected behavior:**
1. Skill reads review mode — determines `full`
2. After implementation verification, skill invokes LP-CODE-REVIEW gate
3. Lead programmer reviews the implementation
4. If LP verdict is NEEDS CHANGES → story cannot be marked Complete
5. If LP verdict is APPROVED → skill proceeds to mark story Complete

**Assertions (5a):**
- [ ] Skill reads review mode before deciding whether to invoke LP-CODE-REVIEW
- [ ] LP-CODE-REVIEW gate is invoked in full mode after implementation check
- [ ] An LP NEEDS CHANGES verdict prevents story from being marked Complete
- [ ] Gate result is noted in output: "Gate: LP-CODE-REVIEW — [result]"
- [ ] LP approval does not grant story-write authority; reuse an already covered named effect or ask for missing/new scope

**Case 5b — lean or solo mode:**
- `review-mode.txt` contains `lean` or `solo`

**Expected behavior:**
1. Skill reads review mode — determines `lean` or `solo`
2. LP-CODE-REVIEW gate is SKIPPED
3. Output notes the skip: "[LP-CODE-REVIEW] skipped — Lean/Solo mode"
4. Required actual PASS evidence, decisions, selected reviews and completion authority still apply; skip is no independent approval

**Assertions (5b):**
- [ ] LP-CODE-REVIEW gate does NOT spawn in lean or solo mode
- [ ] Skip is explicitly noted in output
- [ ] Eligible closure facts and covered exact story-write authority are required; no repeated ask when that scope is already authorized

---

### Case 6: Next Story uses actual Markdown/YAML vocabulary

**Fixture:**
The owning sprint contains separate Ready/ready-for-dev, Draft/backlog,
Blocked/blocked, Complete/done, in-progress and review Stories. Must/Should Have
priorities and dependency facts are supplied; a variant has conflicting states.

**Input:** `/story-done [owning Story path]` after eligible authorized closure

**Expected behavior:**
1. Read owning sprint, Story bodies and matching sprint-status entries.
2. Surface Ready/ready-for-dev candidates only when priority/dependencies permit.
3. List Draft/backlog separately for readiness; report contradictory states for resolution.

**Assertions:**
- [ ] Ready candidates are not skipped by a nonexistent READY/NOT STARTED storage filter.
- [ ] Blocked, done/Complete and already in-progress/review Stories are excluded from the next ready
      list.
- [ ] Draft/backlog is not declared development-ready; no status is repaired while selecting
      candidates.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 7: Owning sprint wins over newest mtime; ambiguity remains explicit

**Fixture:**
active.md and the supplied Story identify sprint A. An unrelated sprint B
has newer mtime. Variants omit active state or give contradictory/multiple Story
ownership references in sprint-status and plan bodies.

**Input:** `/story-done [owning Story path]`; no-argument variants use the stated active/status sources

**Expected behavior:**
1. Reconcile explicit input, active references, real IDs and sprint ownership.
2. Select A only when evidence agrees; surface real paths for ambiguous/conflicting variants.

**Assertions:**
- [ ] Newer sprint B is not selected merely by mtime.
- [ ] Conflicting/multiple candidates are not silently repaired or resolved.
- [ ] Dependent closure/next-story claims remain unresolved; independent checks may continue.

**Case Verdict:** PASS / FAIL / PARTIAL

## Protocol Compliance

- [ ] Reuses covered story-write scope; uses "May I write" for missing/new story effects
- [ ] Reuses covered tech-debt entry effects; asks "May I write" only for missing/new `docs/tech-debt-register.md` scope
- [ ] Presents complete findings (criteria check, deviation check) before asking approval
- [ ] Ends by surfacing the next ready story from the sprint plan
- [ ] Does not mark a story Complete if any criteria are in ERROR state
- [ ] Does not skip the code review prompt

---

## Review Mode Validation Counterexamples

- Valid explicit full/lean/solo overrides valid global; valid global applies when
  explicit absent; only both absent falls back to lean.
- Present `--review` without a value, an invalid value, or existing empty/invalid
  `production/review-mode.txt`: stop before gates/skips/state or closure writes;
  name invalid source and ask correction. No silent lean or invented gate result.

## Public CLI Contract Ownership Counterexample

The owning CDD specifies the user command default `--dry-run=false`. Its
argparse parser defaults to false and explicitly forwards `args.dry_run`
to a private helper whose convenience default is true. Read that public
flow before evaluating the CDD: the private default alone is no violation
of the command-owned default. Keep genuine uncovered CLI/I/O/API-doc
requirements and actual NotRun/FAIL independently; correcting this false
finding does not make the Story eligible for completion. Scoped true/zero
spy calls are not unauthorized writes; actual non-dry-run callbacks remain
prohibited under review-only/report-only authority.

## Shared Contract Cases

Owners: project-root `standards/evidence-lifecycle.md`,
`standards/notes-adr-sync.md` and the canonical skill's QA policy.
Evaluate this skill's own actions/findings/recommendations, without
treating planning or uninvoked closure workflows as runtime execution.

### Case 8: Exact QA policy and closure counterexamples

**Fixture:**
Separate variants: default optional orchestration with actual required PASS;
explicit strict check unavailable; one required AC untested or Must Have blocked;
legacy RISKS label with passing vs failing required facts; report-only/self-review/
stale or missing originals/Unknown scope; exact permitted historical results.

**Input:** `/story-done [fixture Story path]` with each stated policy/evidence variant

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

### Case 9: Optional context absence

**Fixture:**
No Memory Bank/QA Context exists; no strict selection is recorded. A separate
variant has actual conflicting policy or unresolved required applicability.

**Input:** `/story-done [fixture Story path]` under the stated scope

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

### Case 10: Continuing named authority

**Fixture:**
Existing user approval names the exact output path and create/update effect.
A variant authorizes only a report, excluding inputs/index/status/closure; another
introduces a materially new effect. Current input identities are supplied.

**Input:** `/story-done [fixture Story path]` under the stated scope

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

- The full 8-phase flow of the skill is exercised across Cases 1-3; not all
  edge cases within each phase are covered.
- Tech debt logging (deferred items written to `docs/tech-debt-register.md`)
  is mentioned in Case 2 but not the primary assertion focus; dedicated
  coverage deferred.
- Sprint/session/T3 projections each need covered named paths/effects and exact eligible closure; no implicit authority from Story writing.
- Stories with multiple TR-IDs or multiple ADRs are not explicitly tested.
