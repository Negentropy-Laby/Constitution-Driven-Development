# Skill Test Spec: /team-qa

## Skill Summary

Orchestrates the actual defined QA phases (1, 2, 3, 4, 6, 7) without inventing a missing phase. Coordinates
qa-lead (strategy, test plan, sign-off report) and qa-tester (test case writing,
bug report writing). Covers scope detection, story classification, QA plan
generation, smoke check gate, test case writing, manual QA execution with bug
filing, and a final sign-off report with an APPROVED / APPROVED WITH CONDITIONS /
NOT APPROVED verdict. Parallel qa-tester spawning is used in Phase 4 for
independent stories.

---

## Static Assertions (Structural)

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: COMPLETE, BLOCKED
- [ ] Contains verdict keywords for sign-off report: APPROVED, APPROVED WITH CONDITIONS, NOT APPROVED
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has an Error Recovery Protocol section
- [ ] Reuses covered named changeset authority, asking only for material choices/new effects
- [ ] Phase 2 actual required smoke failure/incompleteness stops dependent qualification/execution; independent Phase 3/4 drafts need sufficient actual inputs and covered authority, and create no PASS
- [ ] Bug reports are written to `production/qa/bugs/` with `BUG-[NNN]-[short-slug].md` naming
- [ ] Next-step guidance differs by verdict (APPROVED / APPROVED WITH CONDITIONS / NOT APPROVED)
- [ ] Independent qa-tester tasks in Phase 4 are spawned in parallel

---

## Test Cases

### Case 1: Happy Path — All stories pass manual QA, APPROVED verdict

**Fixture:**
- `production/sprints/sprint-03/` exists with 4 story files
- Stories are a mix of types: 1 Logic, 1 Integration, 2 Visual/Feel
- All stories have acceptance criteria populated
- `tests/smoke/` contains a smoke test list; all items are verifiable
- No existing bugs in `production/qa/bugs/`

**Input:** `/team-qa sprint-03`

**Expected behavior:**
1. Phase 1: Reads all story files in `production/sprints/sprint-03/`; reads `production/stage.txt`; reports "Found 4 stories. Current stage: [stage]. Ready to begin QA strategy?"
2. Phase 2: Spawns `qa-lead` via Task; produces strategy table classifying all 4 stories; no blockers flagged; presents to user; AskUserQuestion: user selects "Looks good — proceed to test plan"
3. Phase 3: Produces QA plan document; reuses exact named QA-plan write authority, or asks "May I write the QA plan to `production/qa/qa-plan-sprint-03-[date].md`?" for missing/new scope; writes only covered effects
4. Phase 2 smoke qualification uses actual exact-bound results; reviewing a scenario list alone cannot return execution PASS
5. Phase 4: Spawns `qa-tester` via Task for each Visual/Feel and Integration story (2–3 stories); run in parallel; presents test cases grouped by story; AskUserQuestion per group; user approves
6. Phase 6: Walks through each approved story; user marks all as PASS; result summary: "Stories PASS: 4, FAIL: 0, BLOCKED: 0"
7. Phase 7: Spawns `qa-lead` via Task to produce sign-off report; all selected required checks have actual PASS and required review/authority satisfied; no bugs filed; Verdict: APPROVED; reuse exact named report authority or ask "May I write this QA sign-off report to `production/qa/qa-signoff-sprint-03-[date].md`?" for missing/new scope
8. Verdict: COMPLETE — QA cycle finished

**Assertions:**
- [ ] Phase 1 correctly counts and reports 4 stories with current stage
- [ ] Strategy table in Phase 2 classifies all 4 stories with correct types
- [ ] QA plan writes use covered existing/new named authority; only missing/new scope asks "May I write?"
- [ ] Smoke check PASS allows pipeline to continue without user intervention
- [ ] Phase 4 qa-tester tasks for independent stories are issued in parallel
- [ ] Sign-off report includes Test Coverage Summary table and Verdict: APPROVED
- [ ] Sign-off report writes use covered existing/new named authority; only missing/new scope asks "May I write?"
- [ ] Verdict: COMPLETE appears in final output
- [ ] Next step: "Run `/gate-check` to validate advancement."

---

### Case 2: Actual smoke failure or required unexecuted checks in Phase 2

Fixture: actual smoke results show core navigation FAIL, or two required items
cannot be executed. Expected: record actual FAIL or NotRun/Blocked/Pending and
smoke FAIL/INCOMPLETE; stop dependent qualification/execution. Continue only
independent planning/evidence work, preserving existing plans/partial findings.
No full-scope APPROVED sign-off from missing/unexecuted/failed required checks.

Assertions:
- [ ] Failure and unavailable execution retain different underlying facts.
- [ ] The actual Phase 2 smoke step, not an invented Phase 4/5 smoke phase, is used.
- [ ] Independent useful work/partial reports are preserved under covered authority.

---

### Case 3: Bug Found — Visual/Feel story fails manual QA, bug report filed

**Fixture:**
- `production/sprints/sprint-05/` exists with 2 story files: 1 Logic (passes automated tests), 1 Visual/Feel
- `tests/smoke/` smoke check passes
- The Visual/Feel story's animation timing is visibly wrong (acceptance criterion not met)
- `production/qa/bugs/` directory exists (empty or with existing bugs)

**Input:** `/team-qa sprint-05`

**Expected behavior:**
1. defined phases before execution complete normally; test cases are written for the Visual/Feel story
2. Phase 6: User marks Visual/Feel story as FAIL; AskUserQuestion collects failure description: "Animation plays at 2x speed — jitter visible on every loop"
3. Phase 6: Spawns `qa-tester` via Task to write a formal bug report; bug report written to `production/qa/bugs/BUG-001-animation-speed-jitter.md` (or next increment if bugs exist); report includes severity field
4. Result summary: "Stories PASS: 1, FAIL: 1 — bugs filed: BUG-001"
5. Phase 7: Spawns `qa-lead` to produce sign-off report; Bugs Found table lists BUG-001 with severity and status Open; Verdict: NOT APPROVED (S1/S2 bug open, or any required FAIL/NotRun/Blocked/Pending, even with a documented workaround)
6. Sign-off report write is offered; writes after approval
7. Next step: "Resolve S1/S2 bugs and re-run `/team-qa` or targeted manual QA before advancing."

**Assertions:**
- [ ] FAIL result in Phase 6 triggers AskUserQuestion to collect the failure description before the bug report is written
- [ ] `qa-tester` is spawned via Task to write the bug report — orchestrator does not write it directly
- [ ] Bug report follows naming convention: `BUG-[NNN]-[short-slug].md` in `production/qa/bugs/`
- [ ] Bug report NNN is incremented correctly from existing bugs in the directory
- [ ] Phase 7 sign-off report Bugs Found table includes the bug ID, story name, severity, and status
- [ ] Verdict in sign-off report is NOT APPROVED
- [ ] Next step explicitly mentions re-running `/team-qa`
- [ ] Verdict: COMPLETE is still issued by the orchestrator (the QA cycle finished — the verdict is NOT APPROVED, but the skill completed its pipeline)

---

### Case 4: No Argument — Skill infers active sprint or asks user

**Fixture (variant A — state files present):**
- `production/session-state/active.md` exists and contains a reference to `sprint-06`
- `production/sprint-status.yaml` exists and identifies `sprint-06` as active

**Fixture (variant B — state files absent):**
- `production/session-state/active.md` does NOT exist
- `production/sprint-status.yaml` does NOT exist

**Input:** `/team-qa` (no argument)

**Expected behavior (variant A):**
1. Phase 1: No argument provided; reads `production/session-state/active.md`; reads `production/sprint-status.yaml`
2. Detects `sprint-06` as the active sprint from both sources
3. Proceeds as if `/team-qa sprint-06` was the input; reports "No sprint argument provided — inferred sprint-06 from session state. Found [N] stories."

**Expected behavior (variant B):**
1. Phase 1: No argument provided; attempts to read `production/session-state/active.md` — file missing; attempts to read `production/sprint-status.yaml` — file missing
2. Cannot infer sprint; uses AskUserQuestion: "Which sprint or feature should QA cover?" with options to type a sprint identifier or cancel

**Assertions:**
- [ ] Skill does NOT default to a hardcoded sprint name when no argument is provided
- [ ] Skill reads both `production/session-state/active.md` AND `production/sprint-status.yaml` before asking the user (variant A)
- [ ] When both state files are absent, skill uses AskUserQuestion rather than guessing (variant B)
- [ ] Inferred sprint is reported to the user before proceeding (variant A transparency)
- [ ] Skill does NOT error out when state files are missing — it falls back to asking (variant B)

---

### Case 5: Mixed Results — Some PASS, one FAIL with S1 bug, one BLOCKED

**Fixture:**
- `production/sprints/sprint-07/` exists with 4 story files
- Smoke check passes
- Story A (Logic): exact-bound actual configured runner evidence proves required AC tests pass — PASS
- Story B (UI): manual QA — PASS WITH NOTES (minor text overflow)
- Story C (Visual/Feel): manual QA — FAIL; tester identifies S1 crash on ability activation
- Story D (Integration): cannot test — BLOCKED (dependency system not yet implemented)

**Input:** `/team-qa sprint-07`

**Expected behavior:**
1. defined phases before execution proceed; Phase 4 test cases cover stories B, C, D
2. Phase 6: Story A automation PASS is sourced from the fixture's actual exact-bound runner originals; otherwise automation remains NotRun/Pending. Story B manual: PASS WITH NOTES; Story C: FAIL; Story D: BLOCKED
3. After Story C FAIL: qa-tester spawned to write bug report `BUG-001-crash-ability-activation.md` with S1 severity
4. Result summary presented: "Stories PASS: 1, PASS WITH NOTES: 1, FAIL: 1 — bugs filed: BUG-001 (S1), BLOCKED: 1"
5. Phase 7: qa-lead produces sign-off report covering all 4 stories; BUG-001 listed as S1/Open; Story D listed as BLOCKED; Verdict: NOT APPROVED
6. Sign-off report writes reuse covered exact authority or obtain missing/new scope with "May I write?"
7. Next step: "Resolve S1/S2 bugs and re-run `/team-qa` or targeted manual QA before advancing."

**Assertions:**
- [ ] All 4 stories appear in the Phase 7 sign-off report Test Coverage Summary table — none are silently omitted
- [ ] Story D (BLOCKED) is listed in the report with a BLOCKED status, not silently dropped
- [ ] S1 bug causes Verdict: NOT APPROVED regardless of the other stories passing
- [ ] PASS WITH NOTES stories do not downgrade to FAIL — they are tracked separately
- [ ] BUG-001 severity is listed as S1 in the Bugs Found table
- [ ] Partial results are preserved — the sign-off report is still produced even with failures and blocks
- [ ] Verdict: COMPLETE is issued by the orchestrator (pipeline completed); sign-off verdict is NOT APPROVED

---

## Protocol Compliance

- [ ] `AskUserQuestion` used at Phase 2 (strategy review), Phase 4 (test case approval per group), and Phase 6 (per-story manual QA result)
- [ ] Actual Phase 2 required smoke failure/incompleteness blocks dependent qualification/execution; preserve partial findings and allow only sufficiently grounded, authorized independent drafts
- [ ] Plan/report/Bug/index effects each have covered named scope; an existing changeset can cover them without repeated asks
- [ ] Bug reports are always written by `qa-tester` via Task — orchestrator does not write directly
- [ ] Phase 4 qa-tester tasks for independent stories are issued in parallel where possible
- [ ] Error recovery: any BLOCKED agent is surfaced immediately with AskUserQuestion options
- [ ] Partial report always produced — no work is discarded because one story failed or blocked
- [ ] Sign-off verdict rules are strictly applied: any S1/S2 bug open = NOT APPROVED; no exceptions
- [ ] Orchestrator-level Verdict: COMPLETE is distinct from the sign-off report's APPROVED/NOT APPROVED verdict

---

## Independent Drafting with Failed or Unexecuted Smoke

Required smoke results are actual FAIL, or required checks are NotRun/Blocked/Pending
and INCOMPLETE. Adequate Story/AC/plan inputs and covered delegation/write authority
permit independent Phase 3 plan or Phase 4 case drafts, explicitly labeled draft.
Do not run dependent QA or treat a user approval of cases as satisfied smoke entry
criteria. Keep case Actual Result/Pass-Fail blank, preserve actual smoke facts and
the original incomplete scope, and grant no original-scope APPROVED sign-off.
Insufficient inputs or missing authority stop the affected draft/effect instead
of inventing scope, runtime evidence or permission. No new phases or CLI flags.
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

**Input:** `/team-qa sprint` with each stated policy/evidence variant

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

**Input:** `/team-qa sprint` under the stated scope

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

**Input:** `/team-qa sprint` under the stated scope

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

- The "APPROVED WITH CONDITIONS" verdict path (S3/S4 bugs, PASS WITH NOTES) is covered implicitly by Case 5's PASS WITH NOTES story (Story B) — if no S1/S2 bugs existed, that case would produce APPROVED WITH CONDITIONS. A dedicated case is not required as the verdict logic is table-driven.
- The `feature: [system-name]` argument form is not separately tested — it follows the same Phase 1 logic as the sprint form, using glob instead of directory read. The no-argument inference path (Case 4) provides sufficient coverage of the detection logic.
- Logic stories with passing automated tests do not need manual QA — this is validated implicitly by Case 5 (Story A) where the Logic story receives no manual QA phase.
- Parallel qa-tester spawning in Phase 4 is validated implicitly by Case 1 (multiple Visual/Feel stories issued simultaneously); no dedicated parallelism case is required beyond the Static Assertions check.
