---
name: test-evidence-review
description: "Quality review of test files and manual evidence documents. Goes beyond existence checks — evaluates assertion coverage, edge case handling, naming conventions, and evidence completeness. Produces ADEQUATE/INCOMPLETE/MISSING verdict per story. Run before QA sign-off or on demand."
argument-hint: "[story-path | sprint | system-name]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---

## QA policy, facts and authority

Apply `standards/evidence-lifecycle.md`, `standards/notes-adr-sync.md` and existing
collaboration authority. Read actual `workflow/workflow-catalog.yaml`, domain,
current transition and established project QA scope, including initialized
`memory_bank/t1_axioms/qa_context.md` or the existing owning Story/plan/decision.
QA orchestration is optional by default; strict obligations need explicit source,
authority and exact checks/scope. Review mode does not select strict QA. Absent
optional Memory Bank/QA Context with no actual strict selection uses the catalog's
default optional orchestration; disclose absence without requiring initialization.
Unknown applies to unresolved actual required applicability or conflicting policy,
not optional context absence. Resolve that affected scope before dependent claims;
Honor actual user-specified per-effect approval conditions when determining coverage;
do not invent strict obligations or passing results.
Optional orchestration never waives required Story AC, governing DoD, decisions,
evidence or required review. Type tables are starting points; actual owners decide
requirements. Each required check retains PASS/FAIL/NotRun/Blocked/Pending; N/A
needs a governing applicability reason and cannot erase a failure.

Separate sufficiency, actual execution, independence, acceptance and completion.
Files/keywords/counts, planning cases and self-checks prove none of the other facts.
Read relied-on bodies and minimum required direct/indirect dependency closure;
retain full SHA-256/byte sizes, recoverable originals and original-path witnesses.
Disclose reading omissions. Exact bound historical results may be reused only
where selected workflow permits, labeled historical with original runtime/observer,
inputs and scope; never call them this run's execution. Missing required originals
or observations leave affected checks incomplete. Risk acceptance is a separate
scoped record; it cannot change FAIL/NotRun/Blocked/Pending to PASS or completion.

Reuse named paths/effects authority across roles/retries; before new authority show
draft and complete effect set, asking only for material new scope. Review-only
invokes no write entrypoint. Report-only writes its new report, excluding inputs,
indexes, session/sprint/stage state and closure. Existing report paths require a
new revision with prior evidence preserved; index effects need their own covered
scope and historical links. Optional Memory Bank absence uses Story/report/
conversation fallback without initialization, publication or activation.

## User Guide

- When to use: Quality review of test files and manual evidence documents. Goes beyond existence checks — evaluates assertion coverage, edge case handling, naming conventions, and evidence completeness. Produces ADEQUATE/INCOMPLETE/MISSING verdict per story. Run before QA sign-off or on demand.
- Inputs: Command arguments: `/test-evidence-review [story-path | sprint | system-name]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: Only when Memory Bank is initialized and each named write effect is covered: `memory_bank/t3_archive/qa_evidence_index.md`, `memory_bank/t3_archive/reviews/review-index.md`.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

## Phase 0: Domain Routing

Resolve actual domain from substantive concept bodies, configured fields and
explicit project decisions under `standards/technical-preferences.md` before
reviewing evidence. Populated legacy Product configuration can establish Product
without a concept; filenames/placeholders alone cannot. Conflicts or absent actual
evidence leave the affected route Unknown while neutral checks continue.

For the resolved domain:
- `design/cdd/game-concept.md` -> **[Game]** review unit/integration tests, smoke checks, manual playtest records, session logs, screenshots, input/platform evidence, and CDD acceptance coverage.
- `design/cdd/product-concept.md` -> **[Product]** review contract tests, CLI smoke output, migration evidence, auth/permission checks, integration traces, deployment smoke logs, screenshots, user-test notes, and CDD acceptance coverage.
- If still unresolved after reading those owners, ask whether evidence should
  prove game playability or product workflow/API/CLI correctness.

Preserve playtest evidence lookup. Product evidence lookup is a parallel branch.

## Dual-Domain Parity Contract

| Area | Game branch | Product branch |
|------|-------------|----------------|
| Context reads | Story files, CDD acceptance, unit/integration tests, playtest/session logs, screenshots, smoke reports | Story files, CDD acceptance/contracts, contract/API tests, CLI smoke output, migration dry-run logs, auth/permission evidence, integration traces, deployment smoke, user-test notes |
| Steps | Locate evidence by story type, read tests/docs, assess assertions, edge cases, naming, manual evidence completeness, sign-off | Locate evidence by product story type, read tests/logs/docs, assess contract coverage, CLI outputs, migration safety, permission matrix, observability/deployment evidence, sign-off |
| Outputs | In-conversation verdicts and optional `production/qa/evidence-review-[date].md` with ADEQUATE/INCOMPLETE/MISSING per story | Same report path with product-specific ADEQUATE/INCOMPLETE/MISSING verdicts and evidence gaps by contract/workflow/ops category |
| Next steps | Add missing tests/evidence, rerun `/smoke-check`, coordinate `/team-qa` | Add missing contract/CLI/migration/auth/deployment/user-test evidence, rerun `/smoke-check`, coordinate `/team-qa` |

# Test Evidence Review

`/smoke-check` verifies that test files **exist** and **pass**. This skill
goes further — it reviews the **quality** of those tests and evidence documents.
A test file that exists and passes may still leave critical behaviour uncovered.
A manual evidence doc that exists may lack the sign-offs required for closure.

**Output:** Summary report (in conversation) + optional `production/qa/evidence-review-[date].md`

**When to run:**
- Before QA hand-off sign-off (`/team-qa` Phase 5)
- On any story where test quality is in question
- As part of milestone review for Logic and Integration story quality audit

---

## 1. Parse Arguments

**Modes:**
- `/test-evidence-review [story-path]` — review a single story's evidence
- `/test-evidence-review sprint` — review all stories in the current sprint
- `/test-evidence-review [system-name]` — review all stories in an epic/system
- No argument — ask which scope: "Single story", "Current sprint", "A system"

---

## 2. Load Stories in Scope

Based on the argument:

**Single story**: Read the story file directly. Extract: Story Type, Test
Evidence section, story slug, system name.

**Sprint**: Read the most recently modified file in `production/sprints/`.
Extract the list of story file paths from the sprint plan. Read each story file.

**System**: Glob story files under the matching system directory in `production/epics/`. Read each.

For each story, collect:
- Actual Game/Product domain/type, required AC/DoD and selected sign-offs
- `## Test Evidence` section — the stated expected test file path or evidence doc
- Story slug (from file name)
- System name (from directory path)
- Acceptance Criteria list (all checkbox items)

---

## 3. Locate Evidence Files

Read exact named Story evidence first; fallback discovery uses actual domain/type.
Game: unit/integration, playtest/session, Visual/Feel/UI manual and Config/Data
smoke. Product: API contract, CLI output/exit codes, migration, auth/permission,
workflow/integration, UI walkthrough/E2E, deployment smoke and config validation.
Support actual configured paths/naming rather than imposing one framework directory.
Read required originals/attachments and exact input bindings; fallback evidence
must prove the same requirement/implementation scope. Missing evidence is MISSING;
unreadable required dependencies INCOMPLETE. Current pointers/filenames/report
keywords do not prove historical evidence or behavioral coverage.

---

## 4. Review Automated Test Quality (Logic / Integration)

For each test file found, read it and evaluate:

### Assertion and edge-case coverage

Map each required AC to actual setup/stimulus/behavioral oracle and result. Read
relevant helpers/fixtures, CDD bounds/contracts/edge cases and exact execution
outputs. One decisive assertion can suffice; multiple vacuous assertions or edge
keywords cannot prove coverage. No meaningful oracle leaves affected AC unverified.
Apply actual `standards/coding-standards.md` and `rules/test-standards.md` naming,
arrange/act/assert, determinism and isolation. Integration/environment checks use
their declared scope, not blanket unit-only assumptions.

Sufficiency ADEQUATE/INCOMPLETE/MISSING, runtime PASS/FAIL/NotRun/Blocked/Pending and
required independent review are separate. This analysis executes no tests; runtime
results come from actual matching current or permitted historical records.

### Naming quality

Test function names should describe: the scenario + the expected result.
Pattern: `test_[scenario]_[expected_outcome]`

Flag functions named generically (`test_1`, `test_run`, `testBasic`) as
**naming issues** — they make failures harder to diagnose.

### Formula traceability

For Logic stories where the CDD has a Formulas section: check that the test
file contains at least one test whose name or comment references the formula
name or a formula value. A test that exercises a formula without mentioning
it by name is harder to maintain when the formula changes.

---

## 5. Review Manual Evidence Quality (Visual/Feel / UI)

For each evidence document found, read it and evaluate:

### Criterion linkage

The evidence doc should reference each acceptance criterion from the story.
Check: does the evidence doc contain each criterion (or a clear rephrasing)?
Missing criteria mean a criterion was never verified.

### Sign-off completeness

Resolve required sign-offs from selected workflow/Story/explicit QA scope.
Verify actual role/independence, exact inputs/scope, outcome and authority; signature
keywords do not prove approval. Game designer/art and Product owner/QA roles apply
when required. Optional QA orchestration creates no unconditional three-role gate.
Missing required sign-off is INCOMPLETE/Pending. Skips establish no approval or
independence; author self-review cannot satisfy a required independent reviewer.

### Screenshot / artefact completeness

For Visual/Feel stories: check whether screenshot file paths are referenced
in the evidence doc. If referenced, Glob for them to confirm they exist.

For UI stories: check whether a walkthrough sequence (step-by-step interaction
log) is present.

### Date coverage

Compare complete evidence/build/config input identities and scope with current
implementation. Date/sprint start/mtime are hints, not freshness proof. Permitted
exact matching historical results remain labeled historical; mismatched/missing
required originals make affected evidence INCOMPLETE.

---

## 6. Build the Review Report

For each story, assign a verdict:

| Verdict | Meaning |
|---------|---------|
| **ADEQUATE** | Exact evidence sufficiently addresses required AC/DoD and sign-offs; execution result is separate |
| **INCOMPLETE** | Required behavioral/input/original/reading/sign-off gaps; counts alone do not decide |
| **MISSING** | No test or evidence found for a story type that requires it |

The overall sprint/system verdict is the worst story verdict present.

```markdown
## Test Evidence Review

> **Date**: [date]
> **Scope**: [single story path | Sprint [N] | [system name]]
> **Stories reviewed**: [N]
> **Overall verdict**: ADEQUATE / INCOMPLETE / MISSING

---

### Story-by-Story Results

#### [Story Title] — [Type] — [ADEQUATE/INCOMPLETE/MISSING]

**Test/evidence path**: `[path]` (found) / (not found)

**Automated test quality** *(Logic/Integration only)*:
- Required AC behavioral oracle: [AC → setup/stimulus/assertion/result mapping; adequate / partial / missing]
- Edge cases: [covered / partial / not found]
- Naming: [consistent / [N] generic names flagged]
- Formula traceability: [yes / no — formula names not referenced in tests]

**Manual evidence quality** *(Visual/Feel/UI only)*:
- Criterion linkage: [N/M criteria referenced]
- Required sign-offs: [actual role / exact input/scope / outcome / Pending / justified N/A]
- Artefacts: [screenshots present / missing / N/A]
- Freshness: [dated [date] — current / potentially stale]

**Issues**:
- BLOCKING: [description] *(prevents story-done)*
- ADVISORY: [description] *(should fix before release)*

---

### Summary

| Story | Type | Verdict | Issues |
|-------|------|---------|--------|
| [title] | Logic | ADEQUATE | None |
| [title] | Integration | INCOMPLETE | Thin assertions (avg 1.2/function) |
| [title] | Visual/Feel | INCOMPLETE | QA lead sign-off missing |
| [title] | Logic | MISSING | No test file found |

**BLOCKING items** (must resolve before story can be closed): [N]
**ADVISORY items** (should address before release): [N]
```

---

## 7. Write Output (Optional)

Present the report in conversation.

Reuse existing named authority for this new report path/effect. Only if missing or materially new ask: "May I write this test evidence review to
`production/qa/evidence-review-[date].md`?"

This is optional — the report is useful standalone. Write only if the user
wants a persistent record.

Only when initialized and both separate pointer effects are covered, update:
- `memory_bank/t3_archive/reviews/review-index.md`
- `memory_bank/t3_archive/qa_evidence_index.md`

Use Review Type `test-evidence-review` and Type `test-evidence-review` with exact
new report revision, manifest and actual sufficiency/runtime/review states. Dedupe
authorized current pointers by source/evidence path, preserving historical links.
Report-only excludes these updates. Without Memory Bank retain Story/report/
conversation fallback and disclose absent optional indexes without initialization.

After the report:

- For BLOCKING items: "These must be resolved before `/story-done` can mark the
  story Complete. Would you like to address any of them now?"
- For thin assertions: "Consider running `/test-helpers [system]` to see
  scaffolded assertion patterns for common cases."
- For missing sign-offs: "Manual sign-off is required from [role]. Share
  `[evidence-path]` with them to complete sign-off."

Review operation: finished/partial; sufficiency ADEQUATE/INCOMPLETE/MISSING, runtime/review states separate. Finished analysis marks no Story Complete and qualifies no product.

---

## Collaborative Protocol

- **Report quality issues, do not fix them** — this skill reads and evaluates;
  it does not modify test files or evidence documents
- **ADEQUATE is scoped evidence sufficiency** — no runtime PASS, ship approval, publication or Story closure is granted
- **BLOCKING vs. ADVISORY distinction is important** — only flag BLOCKING when
  the gap leaves a story criterion genuinely unverified
- **Resolve optional report-write authority**: reuse covered named path/effect authorization; only missing authority or materially new scope requires confirmation. Report-only does not authorize inputs/index/state changes.
