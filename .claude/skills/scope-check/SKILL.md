---
name: scope-check
description: "Assess a named feature, sprint or milestone against its original plan and delivery needs. Reviews baseline necessity, additions, removals and justified alternatives. Use when user says 'any scope creep', 'scope review', 'are we staying in scope'."
argument-hint: "[feature-name or sprint-N or milestone-name]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Write, Edit
model: haiku
---

Read and apply `standards/evidence-lifecycle.md`, `standards/coordination-rules.md`
and `standards/notes-adr-sync.md` for scoped authority, exact evidence and
decision ownership. Review-only invokes no write entrypoint; report-only excludes
input, index and state changes.

## User Guide

- When to use: Assess original and current scope, including whether the baseline itself imposes unnecessary work, for a named feature, sprint or milestone. Use when user says 'any scope creep', 'scope review', 'are we staying in scope'.
- Inputs: Command arguments: `/scope-check [feature-name or sprint-N or milestone-name]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: `memory_bank/t3_archive/reviews/review-index.md`.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Scope Check

Default behavior is read-only. Report findings in conversation. Reuse an existing
named report-write approval; ask only for missing or materially new effects after
showing the proposed report and its path. Report authority excludes indexing.

Compares the original plan and current state against actual delivery needs,
including unnecessary work already present in the baseline.

**Argument:** `$ARGUMENTS[0]` — feature name, sprint number, or milestone name.

---

## Phase 1: Find the Original Plan

If the argument is missing, request a named feature, sprint or milestone and stop
before target-dependent reads or comparison. Do not select an active sprint by
default or introduce a single-Story/parent-epic command interface.

Read the confirmed original feature baseline. For the CDD route below, use the actual governing CDD; if a different matching original design file is chosen, resolve and read that exact original file as the mandatory baseline. Choosing an alternate locator does not make the baseline optional. Missing or unresolved baseline still stops this comparison.

Locate the baseline scope document for the given argument:

- **Feature name** → read `design/cdd/[feature].md` or matching file in `design/`
- **Sprint number** (e.g., `sprint-3`) → read `production/sprints/sprint-03.md` or similar
- **Milestone** → read `production/milestones/[name].md`

Record the named target, actual baseline path/revision, relevant approval scope,
source commit and exact staged/unstaged differences. Bind relied-on untracked,
ignored or external inputs by full SHA-256 and byte size under the evidence
lifecycle standard. Distinguish the original baseline from any later accepted
scope change; do not silently replace the original to erase additions.
Review the baseline itself: for each blocking prerequisite or long-lived
artifact, identify its delivery consumer, the concrete failure if omitted,
applicable mandatory basis and a smaller sufficient alternative.
An item already present in the original plan is not thereby necessary.

An unresolved, missing or unreadable mandatory baseline stops this comparison:
report Assessment Status: Unknown and assign no Scope Verdict. Name the exact
required input and affected decision. Continue independent observations without
inventing a replacement baseline or a passing comparison.

---

## Phase 2: Read the Current State

Check what has actually been implemented or is in progress:

- Scan the codebase for files related to the feature/sprint
- Read git log for commits related to this work (`git log --oneline --since=[start-date]`)
- Check for TODO/FIXME comments that indicate unfinished scope additions
- Check active sprint plan if the feature is mid-sprint

Compare actual relevant content and required dependency context under
`standards/coordination-rules.md`; a changed commit alone does not invalidate
otherwise unchanged relevant inputs. An actual affected behavior/input change
needs its own impact assessment and evidence. Do not claim evidence transfer
from matching hashes, ancestry or counts alone.

---

## Phase 3: Compare Original vs Current Scope

Produce the comparison report:

```markdown
## Scope Check: [Feature/Sprint Name]
Generated: [Date]

### Original Scope
[List of items from the original plan]

### Current Scope
[List of items currently implemented or in progress]

### Scope Additions (not in original plan)
| Addition | Source | When | Justified? | Effort |
|----------|--------|------|------------|--------|
| [item] | [commit/person] | [date] | [Yes/No/Unclear] | [S/M/L] |

### Scope Removals (in original but dropped)
| Removed Item | Reason | Impact |
|-------------|--------|--------|
| [item] | [why removed] | [what's affected] |

### Baseline and Delivery Necessity
Baseline: [original path/revision and exact input identity]
Accepted scope changes: [source and scope, or none/Unknown]

| Dimension | Baseline / current facts | Necessity or concern and evidence | Keep / Cut / Defer / Resolve |
|---|---|---|---|
| Business scope | [user/player outcome and retained assumptions] | [direct goal/constraint] | [action] |
| Deliverables | [long-lived artifact and actual consumer] | [failure without it; smaller representation] | [action] |
| Dependencies | [actual consumer path, mandatory basis] | [failure without it; smaller alternative; false cycle] | [action] |
| Validation | [assertion, layer, required scope and actual status] | [what the check can and cannot prove] | [action] |
| Cost | [measured/estimated time, bytes or complexity; Unknown if unmeasured] | [declared set and assumptions] | [action] |
| Changes from baseline | [added/removed scope and authority] | [impact and evidence] | [action] |

### Descriptive Scope Counts
Original/current/added/removed counts and net change: [values and counting unit].
Use percentages only when the baseline denominator is meaningful and nonzero;
otherwise report NotApplicable with the reason. Counts are descriptive and do
not independently determine PASS, CONCERNS or FAIL. Do not invent cost measures.

### Risk Assessment
- **Schedule Risk**: [Low/Medium/High] — [explanation]
- **Quality Risk**: [Low/Medium/High] — [explanation]
- **Integration Risk**: [Low/Medium/High] — [explanation]

### Recommendations
1. **Cut**: [Items that should be removed to stay on schedule]
2. **Defer**: [Items that can move to a future sprint/version]
3. **Keep**: [Additions that are genuinely necessary]
4. **Flag**: [Items that need a decision from producer/creative-director]
```

---

## Phase 4: Verdict

Assign a Scope Verdict from the assessed delivery scope and necessity evidence,
not from a percentage threshold. First resolve required baseline/applicability
facts. If those facts remain Unknown, report Assessment Status: Unknown, name the
affected decision and assign no Scope Verdict. A known defect may still be
reported as a finding; do not certify an incomplete comparison.

- **PASS**: The assessed original and current scope is justified by the stated
  delivery, actual consumers and applicable requirements; blocking dependencies
  are necessary and no material scope or necessity concern remains unresolved.
- **CONCERNS**: A specific bounded scope/necessity concern needs clarification or
  a targeted cut/defer decision; describe its impact, evidence, owner and next action.
- **FAIL**: Evidence establishes material unnecessary blocking work, an unsupported
  expansion, a false dependency cycle, or a conflict with governing scope/requirements.

Unchanged size can FAIL; a justified large change can PASS. Neither is automatic.

```text
Assessment Status: [Assessed / Unknown]
Scope Verdict: [PASS / CONCERNS / FAIL, only when assigned]
Assessed scope and rationale: [dimensions, findings and evidence]
Unresolved facts / affected dependants: [Unknown or none]
Descriptive net change: [value and unit / NotApplicable, with reason]
```

When Assessment Status is Unknown, omit the Scope Verdict field rather than
filling it with Unknown or a passing placeholder. Unknown is an assessment state,
not a fourth canonical verdict. NotApplicable requires an actual applicability
reason for that item, never an erased failure.

Required AC/DoD, security, Accepted decisions, required review and execution
checks retain their actual PASS/FAIL/NotRun/Blocked/Pending states. A scope
recommendation, smaller alternative or risk acceptance cannot turn them into PASS.

---

## Phase 5: Next Steps

After presenting the report, offer concrete follow-up:

- **PASS** → no unresolved scope/necessity concern in this assessed target; this grants no other qualification. Suggest re-running before the next milestone.
- **CONCERNS** → offer to identify the 2–3 additions with best cut ratio. Reference `/sprint-plan update` to formally re-scope.
- **FAIL** → recommend escalating the specific finding to producer. Reference `/sprint-plan update` for re-planning or `/estimate` for a proposed timeline change. Do not stop unrelated project work.
- **Unknown assessment** → name the missing baseline/applicability fact, owner and affected dependent decision; continue independent observations without assigning a verdict.

Always end with:
> "After any authorized scope or evidence change, re-run `/scope-check [name]` for the affected target; do not assume the next verdict must improve."

---

## Phase 5b: Optional Scope Decision Evidence

After presenting the report, reuse covered named authority. Only for a missing
or materially new report effect, ask:

> "May I write this scope check to `production/scope/scope-check-[target]-[YYYY-MM-DD].md`?"

Write the report when its named effect is authorized. Update initialized
`memory_bank/t3_archive/reviews/review-index.md` only when its separate named
index effect is also authorized.

Update the Memory Bank index only when this run enters its separately named, authorized effect after saving the actual report. Initialized Memory Bank alone is insufficient; read-only and report-only scopes exclude indexing. If the intended effect or initialization is unresolved, retain Unknown. Before indexing, read the saved immutable report and exact input/evidence identities; a proposed output or INFO is insufficient. This effect does not initialize Memory Bank.

Review index row:

- Review Type: `scope-check`
- Source Artifact: `production/scope/scope-check-[target]-[YYYY-MM-DD].md`
- Verdict: `PASS`, `CONCERNS`, or `FAIL`, only when assigned

Unknown/no-verdict assessments stay in the report/conversation. Do not add an
index row with a fabricated verdict or introduce a new index enum.
- Scope: feature, sprint, or milestone target

Use `Source Artifact` as the dedupe key. If optional Memory Bank does not exist,
use the authorized report/conversation fallback and disclose the absent index.
Do not initialize Memory Bank or treat its optional absence as Unknown baseline.

---

### Rules

- Cuts, unchanged item counts or timeline extensions do not by themselves justify scope. Assess original and added work against actual delivery and governing constraints.
- Not all additions are bad — some are discovered requirements. But they must be acknowledged and accounted for
- **[Game]** When recommending cuts, prioritize preserving the core player experience over nice-to-haves. **[Product]** When recommending cuts, prioritize preserving the core user workflow and data integrity over nice-to-haves.
- Quantify relevant changes where units and evidence support it; disclose Unknown instead of inventing counts or treating unlike items as equal effort.
- Recommendations do not amend approved scope or waive required gates. Use justified N/A only for actual inapplicability.
