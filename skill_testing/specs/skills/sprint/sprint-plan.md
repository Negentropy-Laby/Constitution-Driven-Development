# Skill Test Spec: /sprint-plan

## Skill Summary

`/sprint-plan` reads the current milestone file and backlog stories, then
generates a new numbered sprint with stories prioritized by implementation layer
and priority score. In full mode the PR-SPRINT director gate runs after the
sprint draft is compiled (producer reviews the plan). In lean and solo modes
the gate is skipped. The skill asks "May I write to `production/sprints/sprint-NNN.md`?"
before persisting. Verdicts: COMPLETE (sprint generated and written) or
BLOCKED (cannot proceed due to missing data or gate failure).

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: COMPLETE, BLOCKED
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff (what to do after sprint is written)

---

## Director Gate Checks

| Gate ID   | Trigger condition        | Mode guard         |
|-----------|--------------------------|--------------------|
| PR-SPRINT | After sprint draft built | full only (not lean/solo) |

---

## Test Cases

Unless a case overrides it, existing planning fixtures have actual configured
Game domain/engine and gameplay evidence; concept absence alone is not that evidence.

### Case 1: Happy Path — Backlog with stories generates sprint

**Fixture:**
- `production/milestones/milestone-02.md` exists with capacity `10 story points`
- Backlog contains 5 unstarted stories across 2 epics, mixed priorities
- `production/review-mode.txt` contains `full`
- Next sprint number is `003` (sprints 001 and 002 already exist)

**Input:** `/sprint-plan`

**Expected behavior:**
1. Skill reads current milestone to obtain capacity and goals
2. Skill reads all unstarted stories from backlog; sorts by layer + priority
3. Skill drafts sprint-003 with stories fitting within capacity
4. Skill presents draft to user before invoking gate
5. Skill invokes PR-SPRINT gate (full mode); producer approves
6. After PR-SPRINT and actual QA-scope handling, reuse covered plan/YAML authority or ask for missing/new exact effects: "May I write to `production/sprints/sprint-003.md`?"
7. User approves; file is written

**Assertions:**
- [ ] Stories are sorted by implementation layer before priority
- [ ] Sprint draft is shown before any write or gate invocation
- [ ] PR-SPRINT gate is invoked in full mode after draft is ready
- [ ] Plan/YAML stay drafts through selected producer review and QA handling; write only covered named effects, asking "May I write" only for missing/new scope
- [ ] Written file path matches `production/sprints/sprint-003.md`
- [ ] Verdict is COMPLETE after successful write

---

### Case 2: Blocked Path — Backlog is empty

**Fixture:**
- `production/milestones/milestone-02.md` exists
- No unstarted stories exist in any epic backlog

**Input:** `/sprint-plan`

**Expected behavior:**
1. Skill reads backlog — finds no unstarted stories
2. Skill outputs "No unstarted stories in backlog"
3. Skill suggests running `/create-stories` to populate the backlog
4. No gate is invoked; no file is written

**Assertions:**
- [ ] Verdict is BLOCKED
- [ ] Output contains "No unstarted stories" or equivalent message
- [ ] Output recommends `/create-stories`
- [ ] PR-SPRINT gate is NOT invoked
- [ ] No write tool is called

---

### Case 3: Gate returns CONCERNS — Sprint overloaded, revised before write

**Fixture:**
- Backlog has 8 stories totalling 16 points; milestone capacity is 10 points
- `review-mode.txt` contains `full`

**Input:** `/sprint-plan`

**Expected behavior:**
1. Skill drafts sprint with all 8 stories (over capacity)
2. PR-SPRINT gate runs; producer returns CONCERNS: sprint is overloaded
3. Skill presents concern to user and asks which stories to defer
4. User selects 3 stories to defer; sprint is revised to 5 stories / 10 points
5. Skill asks "May I write" with revised sprint; writes on approval

**Assertions:**
- [ ] CONCERNS from PR-SPRINT gate surfaces to user before any write
- [ ] Skill allows sprint to be revised after gate feedback
- [ ] Revised sprint (not original) is written to file
- [ ] Verdict is COMPLETE after revision and write

---

### Case 4: Lean Mode — PR-SPRINT gate skipped

**Fixture:**
- Backlog has 4 stories; milestone capacity is 8 points
- `review-mode.txt` contains `lean`

**Input:** `/sprint-plan`

**Expected behavior:**
1. Skill reads review mode — determines `lean`
2. Skill drafts sprint and presents it to user
3. PR-SPRINT gate is skipped; output notes "[PR-SPRINT] skipped — Lean mode"
4. Skill asks user for direct approval of the sprint
5. User approves; sprint file is written

**Assertions:**
- [ ] PR-SPRINT gate is NOT invoked in lean mode
- [ ] Skip is explicitly noted in output
- [ ] User approval is still required before write (gate skip ≠ approval skip)
- [ ] Verdict is COMPLETE after write

---

### Case 5: Edge Case — Previous sprint still has open stories

**Fixture:**
- `production/sprints/sprint-002.md` exists with 2 stories still `Status: In Progress`
- Backlog has 5 new unstarted stories
- `review-mode.txt` contains `full`

**Input:** `/sprint-plan`

**Expected behavior:**
1. Skill reads sprint-002 and detects 2 open (in-progress) stories
2. Skill flags: "Sprint 002 has 2 open stories — confirm carry-over before planning sprint 003"
3. Skill presents user with choice: carry stories over, defer them, or cancel
4. User confirms carry-over; carried stories are prepended to new sprint with `[CARRY]` tag
5. Sprint draft is built; PR-SPRINT gate runs; sprint is written on approval

**Assertions:**
- [ ] Skill checks the most recent sprint file for open stories
- [ ] User is asked to confirm carry-over before sprint planning continues
- [ ] Carried stories appear in the new sprint draft with a distinguishing label
- [ ] Skill does not silently ignore open stories from the previous sprint

---

## Protocol Compliance

- [ ] Shows draft sprint before invoking PR-SPRINT gate or asking to write
- [ ] Reuses covered named plan/YAML authority; asks "May I write" only for missing/new effects after selected review and QA handling
- [ ] PR-SPRINT gate only runs in full mode
- [ ] Skip message appears in lean and solo mode output
- [ ] Verdict is clearly stated at the end of the skill output

---

## Review Mode Validation Counterexamples

Valid explicit full/lean/solo wins; otherwise use valid trimmed existing global;
only both absent defaults lean. Present empty/invalid explicit or global values
stop before director gates, gate skipping or plan/status writes; name source and
request correction, preserving the existing CLI without inventing another flag.

## Write Ordering and Status Return Counterexamples

Full mode: YAML and plan remain in-memory drafts until actual PR-SPRINT review
and Phase 5 QA-scope handling complete. Lean/solo retain their legal recorded
PR-SPRINT skips, which grant neither passing QA facts nor write authority. Any
selected required QA obligation stays Pending/NotRun/Blocked when unresolved;
independent planning may continue without claiming qualification. Only final
covered effects write, with plan-only authority excluding YAML. `status` outputs
a conversation report and returns before later gate/write phases.

## Positional Base Mode Counterexamples

- `/sprint-plan` with no positional selector uses `new`; explicit `new`, `update`
  and `status` select their existing branches, with `status` returning conversation-only.
- Legal flag-only `/sprint-plan --review full` uses base `new` and explicit review
  `full`. Review flags and their values are parsed independently of the selector;
  they are not mistaken for invalid positional mode names.
- `/sprint-plan unknown` or another unsupported non-flag selector stops before
  context-dependent gates or writes, names the invalid value and requests correction.
  It cannot silently become `new`; missing/invalid review values retain the existing
  separate review-validation failure and cannot silently become lean.

## Domain routing paired counterexamples

**Fixture A:** No concept; actual configured Product CLI/API/data workflow.
**Fixture B:** No concept and no configured domain evidence.
**Fixture C:** Legacy Game with actual configured engine/domain and gameplay.
**Fixture D:** Contradictory Game/Product concept bodies, or explicit mixed scope
without a concrete Game or Product selection for the dependent branch.
- [ ] A routes Product without engine/player assumptions; C retains Game compatibility.
- [ ] B/D remain unresolved, blocking dependent single-domain routing/claims;
  do not invent a Both project route or completed phase. Neutral
  `status`/independent reporting continues without invented completed scope.
- [ ] Domain detection writes no state or Memory Bank and does not alter existing
  positional selectors, review-mode resolution, QA handling or director gates.
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

**Input:** `/sprint-plan new` with each stated policy/evidence variant

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

**Input:** `/sprint-plan new` under the stated scope

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

**Input:** `/sprint-plan new` under the stated scope

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

- The case where no milestone file exists is not explicitly tested; behavior
  follows the BLOCKED pattern with a suggestion to run `/gate-check` for
  milestone progression.
- Solo mode behavior is equivalent to lean (gate skipped, user approval
  required) and is not separately tested.
- Parallel story selection algorithms are not tested here; those are unit
  concerns for the sprint-plan subagent.
