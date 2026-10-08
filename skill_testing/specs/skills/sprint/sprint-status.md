# Skill Test Spec: /sprint-status

## Skill Summary

`/sprint-status` is a Haiku-tier read-only skill that reads the current active
sprint file and the session state to produce a concise sprint health summary.
It reports story counts by status (Complete / In Progress / Blocked / Not Started)
and emits one of three sprint-health verdicts: ON TRACK, AT RISK, or BLOCKED.
It never writes files and does not invoke any director gates. It is designed for
fast, low-cost status checks during a session.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings or numbered check sections
- [ ] Contains verdict keywords: ON TRACK, AT RISK, BLOCKED
- [ ] Does NOT require "May I write" language (read-only skill)
- [ ] Has a next-step handoff (what to do based on the verdict)

---

## Director Gate Checks

None. `/sprint-status` is a read-only reporting skill; no gates are invoked.

---

## Test Cases

### Case 1: Happy Path — Mixed sprint, AT RISK with named blocker

**Fixture:**
- `production/sprints/sprint-004.md` exists and is the newest sprint file for blank-argument discovery
- Sprint contains 6 stories:
  - 3 with `Status: Complete`
  - 2 with `Status: In Progress`
  - 1 with `Status: Blocked` (blocker: "Waiting on physics ADR acceptance")
- Sprint end date is 2 days away

**Input:** `/sprint-status`

**Expected behavior:**
1. With no argument, skill finds the most recently modified actual file in `production/sprints/` and reports its path; mtime is discovery only
2. Skill reads `production/sprints/sprint-004.md`
3. Skill counts stories by status: 3 Complete, 2 In Progress, 1 Blocked
4. Skill detects a Blocked story and the approaching deadline
5. Skill outputs AT RISK verdict with the blocker named explicitly

**Assertions:**
- [ ] Output includes story count breakdown by status
- [ ] Output names the specific blocked story and its blocker reason
- [ ] Verdict is AT RISK (not BLOCKED, not ON TRACK) when any story is Blocked
- [ ] Skill does not write any files

---

### Case 2: All Stories Complete — Sprint COMPLETE verdict

**Fixture:**
- `production/sprints/sprint-004.md` exists
- All five claimed Complete Stories have exact eligible closures with required actual PASS/review/decision/completion authority

**Input:** `/sprint-status`

**Expected behavior:**
1. Skill reads linked exact closure/evidence inputs; all five eligible completions verified, never inferred from body keywords/YAML rows
2. Skill outputs ON TRACK verdict or SPRINT COMPLETE label
3. Skill suggests running `/milestone-review` or `/sprint-plan` as next steps

**Assertions:**
- [ ] Verdict is ON TRACK or SPRINT COMPLETE when all stories are Complete
- [ ] Verified Story closure count is separate from sprint/stage completion obligations and authority
- [ ] Next-step suggestion references `/milestone-review` or `/sprint-plan`
- [ ] No files are written

---

### Case 3: No Active Sprint File — Guidance to run /sprint-plan

**Fixture:**
- `production/sprints/` directory is empty or absent

**Input:** `/sprint-status`

**Expected behavior:**
1. Skill applies argument matching or blank-argument file discovery directly under `production/sprints/`
2. Skill checks `production/sprints/` — finds no files
3. Skill outputs an informational message: no active sprint detected
4. Skill suggests running `/sprint-plan` to create one

**Assertions:**
- [ ] Skill does not error or crash when no sprint file exists
- [ ] Output clearly states no active sprint was found
- [ ] Output recommends `/sprint-plan` as the next action
- [ ] No verdict keyword is emitted (no sprint to assess)

---

### Case 4: Date Age Hint vs Actual Stalled Activity

**Fixture:** `production/sprints/sprint-004.md` references an In Progress Story
whose own `Last updated: 2026-03-30` is older than two days. No blocked Story or
actual activity evidence establishes stalled progress.
**Input:** `/sprint-status`
**Expected:** read actual sprint/Story files, calculate metadata date age and
show STALE metadata as an attention hint. Do not assert no-progress/hiddenblocker
or force At Risk from the timestamp; activity remains Unknown and other actual
completion/deadline/blocker facts determine burndown.

**Counterfixture:** exact relevant activity/dependency evidence establishes
stalled work over a stated interval or an actual blocker. Cite that evidence and
scope before supported no-progress/At Risk escalation.

**Assertions:**
- [ ] Date-age hint is distinct from observed stalled activity and Blocked state.
- [ ] Date/mtime alone cannot prove intervening work absent or force risk escalation.
- [ ] Only actual relevant activity evidence supports a no-progress claim.
- [ ] Skill stays read-only and does not write/refetch absent activity evidence.

---

### Case 5: Gate Compliance — Read-only; no gate invocation

**Fixture:**
- `production/sprints/sprint-004.md` exists with 4 stories (2 Complete, 2 In Progress)
- `production/review-mode.txt` contains `full`

**Input:** `/sprint-status`

**Expected behavior:**
1. Skill reads sprint and produces status summary
2. Skill does NOT invoke any director gate regardless of review mode
3. Output is a plain status report with ON TRACK, AT RISK, or BLOCKED verdict
4. Skill does not prompt for user approval or ask to write any file

**Assertions:**
- [ ] No director gate is invoked in any review mode
- [ ] Output does not contain any "May I write" prompt
- [ ] Skill completes and returns a verdict without user interaction
- [ ] Review mode file is ignored (or confirmed irrelevant) by this skill

---

## Protocol Compliance

- [ ] Does NOT use Write or Edit tools (read-only skill)
- [ ] Presents story count breakdown before emitting verdict
- [ ] Does not ask for approval
- [ ] Ends with a recommended next step based on verdict
- [ ] Runs on Haiku model tier (fast, low-cost)

---

## Read-Only Authority Counterexample

An existing named changeset for another workflow does not turn `/sprint-status`
into a writer: it returns a conversation-only status report without write/gate
entrypoints, index/state repair or new write questions. Preserve actual required
closure/QA facts and direct needed work to its real owner.
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

**Input:** `/sprint-status` with each stated policy/evidence variant

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

**Input:** `/sprint-status` under the stated scope

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

## Coverage Notes

- The case where multiple sprints are active simultaneously is not tested;
  argument matching selects a requested sprint; blank input discovers the most recently modified sprint file and reports its actual path.
- Partial sprint completion percentages are not explicitly verified; the
  count-by-status output implies them.
- The `solo` mode review-mode variant is not separately tested; gate
  behavior in Case 5 applies to all modes equally.
