---
name: retrospective
description: "Generates a sprint or milestone retrospective by analyzing completed work, velocity, blockers, and patterns. Produces actionable insights for the next iteration."
argument-hint: "[sprint-N|milestone-name]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
context: |
  !git log --oneline --since="2 weeks ago" 2>/dev/null
---

Read and apply `standards/evidence-lifecycle.md`, `standards/coordination-rules.md`
and `standards/notes-adr-sync.md` for scoped authority, exact evidence and decision
ownership. Review-only invokes no write entrypoint. Report-only writes only its
named report, excluding inputs, indexes, snapshots and state. Saving a report or
recommending an action does not authorize executing it.

## User Guide

- When to use: Generates a sprint or milestone retrospective by analyzing completed work, velocity, blockers, and patterns. Produces actionable insights for the next iteration.
- Inputs: Command arguments: `/retrospective [sprint-N|milestone-name]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: `memory_bank/t3_archive/sprint_snapshots/`, `memory_bank/t3_archive/sprint_snapshots/milestone-[name]-closeout-[YYYY-MM-DD].md`, `memory_bank/t3_archive/sprint_snapshots/sprint-[id]-closeout-[YYYY-MM-DD].md`.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

## Phase 0: Domain Routing

Detect the project domain before running the retrospective:
- `design/cdd/game-concept.md` -> **[Game]** reflect on player value, game feel, content progress, playtest learnings, engine/tooling friction, and team handoffs.
- `design/cdd/product-concept.md` -> **[Product]** reflect on user value, workflow completion, API/CLI quality, deployment/test reliability, observability, support feedback, and adoption risks.
- If unclear, run a domain-neutral retrospective and label unresolved domain assumptions.

Preserve game retrospective prompts. Product prompts are an additional section.
## Phase 1: Parse Arguments

Determine whether this is a sprint retrospective (`sprint-N`) or a milestone retrospective (`milestone-name`).

---

## Phase 1b: Check for Existing Retrospective

Before loading any data, glob for an existing retrospective file:

- For sprint retrospectives: `production/retrospectives/retro-[sprint-slug]-*.md`
  (also check `production/sprints/sprint-[N]-retrospective.md` as an alternate location)
- For milestone retrospectives: `production/retrospectives/retro-[milestone-name]-*.md`

If a matching file is found, present the user with:

```
An existing retrospective was found: [filename]

[A] Update existing retrospective — load it and add/revise sections
[B] Start fresh — generate a new retrospective, archiving the old one
```

Wait for user selection before continuing. If updating, read the existing file and
carry its content forward into the generation phase, revising sections with new data.

---

## Phase 2: Load Sprint or Milestone Data

Read the sprint or milestone plan from the appropriate location:

- Sprint plans: `production/sprints/`
- Milestone definitions: `production/milestones/`

**If the file does not exist or is empty**, output:

> "No sprint data found for [sprint/milestone]. Run `/sprint-status` to generate
> sprint data first, or provide the sprint details manually."

Then use `AskUserQuestion` to present two options:

- **[A] Provide data manually** — ask the user to paste or describe the sprint
  tasks, dates, and outcomes; use that as the source of truth for the retrospective.
- **[B] Stop** — abort the skill. Verdict: **BLOCKED** — no sprint data available.

If the user chooses [A], collect the data and continue to Phase 3 using what they provide.
If the user chooses [B], stop here.

Extract: planned tasks, estimated effort, owners, and goals.

Read the git log for the period covered by the sprint or milestone to understand what was actually committed and when.

---

## Phase 3: Analyze Completion and Trends

Scan for completed and incomplete tasks by comparing the plan against actual deliverables. Check for:

- Tasks completed as planned
- Tasks completed but modified from the plan
- Tasks carried over (not completed)
- Tasks added mid-sprint (unplanned work)
- Tasks removed or descoped

Scan the codebase for TODO/FIXME trends:

- Count current TODO/FIXME/HACK comments
- Compare to previous sprint counts if available (check previous retrospectives)
- Note whether technical debt is growing or shrinking

Read previous retrospectives (if any) from `production/sprints/` or `production/milestones/` to check:

- Were previous action items addressed?
- Are the same problems recurring?
- How has velocity trended?

---

## Phase 4: Generate the Retrospective

```markdown
## Retrospective: [Sprint N / Milestone Name]
Period: [Start Date] -- [End Date]
Generated: [Date]

### Metrics

| Metric | Planned | Actual | Delta |
|--------|---------|--------|-------|
| Tasks | [X] | [Y] | [+/- Z] |
| Completion Rate | -- | [Z%] | -- |
| Story Points / Effort Days | [X] | [Y] | [+/- Z] |
| Bugs Found | -- | [N] | -- |
| Bugs Fixed | -- | [N] | -- |
| Unplanned Tasks Added | -- | [N] | -- |
| Commits | -- | [N] | -- |

### Velocity Trend

| Sprint | Planned | Completed | Rate |
|--------|---------|-----------|------|
| [N-2] | [X] | [Y] | [Z%] |
| [N-1] | [X] | [Y] | [Z%] |
| [N] (current) | [X] | [Y] | [Z%] |

**Trend**: [Increasing / Stable / Decreasing]
[One sentence explaining the trend]

### What Went Well
- [Observation backed by specific data or examples]
- [Another positive observation]
- [Recognize specific contributions or decisions that paid off]

### What Went Poorly
- [Specific issue with measurable impact -- e.g., "Feature X took 5 days
  instead of estimated 2, blocking tasks Y and Z"]
- [Another issue with impact]
- [Do not assign blame -- focus on systemic causes]

### Blockers Encountered

| Blocker | Duration | Resolution | Prevention |
|---------|----------|------------|------------|
| [What blocked progress] | [How long] | [How it was resolved] | [How to prevent recurrence] |

### Estimation Accuracy

| Task | Estimated | Actual | Variance | Likely Cause |
|------|-----------|--------|----------|--------------|
| [Most overestimated task] | [X] | [Y] | [+Z] | [Why] |
| [Most underestimated task] | [X] | [Y] | [-Z] | [Why] |

**Overall estimation accuracy**: [X%] of tasks within +/- 20% of estimate

[Analysis: Are we consistently over- or under-estimating? For which types of
tasks? What adjustment should we apply?]

### Carryover Analysis

| Task | Original Sprint | Times Carried | Reason | Action |
|------|----------------|---------------|--------|--------|
| [Task that was not completed] | [Sprint N-X] | [N] | [Why] | [Complete / Descope / Redesign] |

### Technical Debt Status
- Current TODO count: [N] (previous: [N])
- Current FIXME count: [N] (previous: [N])
- Current HACK count: [N] (previous: [N])
- Trend: [Growing / Stable / Shrinking]
- [Note any areas of concern]

### Previous Action Items Follow-Up

| Action Item (from Sprint N-1) | Status | Notes |
|-------------------------------|--------|-------|
| [Previous action] | [Done / In Progress / Not Started] | [Context] |

### Action Items for Next Iteration

| # | Action | Proposed owner path / section | Responsible owner | Priority | Due date / phase | Observable acceptance or counterexample | Status |
|---|---|---|---|---|---|---|---|
| 1 | [Specific, measurable action] | [existing owner path/section, or unresolved] | [Who] | [High/Med/Low] | [When] | [input/action and observable expected result] | [Open/In Progress/Done] |
| 2 | [Another action] | [existing owner path/section, or unresolved] | [Who] | [Priority] | [When] | [acceptance or falsifying counterexample] | [Open/In Progress/Done] |

Name the existing paragraph/template/tool owner that would change, the responsible
owner and due date/phase, and an observable acceptance or counterexample. A
retrospective recommendation does not authorize that edit or create a new owner.
For auxiliary work, define an objective- and risk-based stop/simplify condition
when useful: the signal to stop repeating, new diagnosis needed for a retry, a
smaller route preserving the same delivery assertion and mandatory constraints,
and the original evidence that must remain. Use the existing task/report to
record it. Do not impose a universal second-failure threshold or skip a real
delivery defect, security requirement or governing verification gate.

### Process Improvements
- [Specific change to how we work, with expected benefit]
- [Another improvement -- keep it to 2-3 actionable items, not a wish list]

### Summary
[2-3 sentence overall assessment: Was this a good sprint/milestone? What is
the single most important thing to change going forward?]
```

---

## Phase 5: Save Retrospective

Present the retrospective and top findings to the user (completion rate, velocity trend, top blocker, most important action item).

Reuse existing named report path/create-or-update authority. Only if it is
missing or materially new, show the concrete draft and effects, then ask:
"May I write this to `production/sprints/sprint-[N]-retrospective.md`?"
(or the resolved milestone path if applicable). Existing-file updates preserve
recoverable prior revisions and follow the same exact authority.

When saving the report, do not execute proposed action items or update any
input/index/state. Those effects need their own named authority and applicable
decision/review requirements.

When the report effect is covered, write the file, creating its directory if needed. Verdict: **COMPLETE** — the authorized retrospective was saved; this completes no sprint, action item, QA check or stage.

When `memory_bank/` exists, propose the actual T3 snapshot path and contents under
`memory_bank/t3_archive/sprint_snapshots/` as a separate effect or part of the named
changeset. Write it only when that snapshot is covered by existing scoped authority
or the user approves the concrete report-and-snapshot changeset. Approval to save
the retrospective alone does not authorize the snapshot; an unapproved snapshot
remains pending while the authorized retrospective can be saved.

- Sprint retrospective path: `memory_bank/t3_archive/sprint_snapshots/sprint-[id]-closeout-[YYYY-MM-DD].md`
- Milestone retrospective path: `memory_bank/t3_archive/sprint_snapshots/milestone-[name]-closeout-[YYYY-MM-DD].md`
- Include completed work, carryover, QA/release links, top blockers, and action
  items.
- If optional `memory_bank/` does not exist, retain the authorized report/conversation fallback and disclose absent optional snapshots; do not initialize it.

If report writing is declined, stop that write. Verdict: **BLOCKED** — user declined the report write. Independent conversational findings remain available.

---

## Phase 6: Next Steps

- Run `/sprint-plan` to incorporate the action items and velocity data into the next sprint.
- If this was a milestone retrospective, run `/gate-check` to formally assess readiness for the next phase.

### Guidelines

- Be honest and specific. Vague retrospectives ("communication could be better") produce vague improvements. Use data and examples.
- Focus on systemic issues, not individual blame.
- Limit action items to 3-5. More than that dilutes focus.
- Every action item names its proposed existing owner path/section, responsible owner, due date/phase and observable acceptance or counterexample, retaining priority and actual status. Unresolved owners stay explicit, not invented.
- Check whether previous action items were completed. Recurring unaddressed items are a process smell.
- If this is a milestone retrospective, also evaluate whether the milestone goals were achieved and what that means for the overall project timeline.
