# Review and Traceability Report Formats

## Phase 7: Architecture review report

```
## Architecture Review Report
Date: [date]
Technology: [name + version]
CDDs Reviewed: [N]
ADRs Reviewed: [M]

---

### Traceability Summary
Total requirements: [N]
Dispositions: covered [N], cdd-layer [N], no-adr [N], documentation-update [N],
              adr-required [N], conflict [N]
Incomplete required inputs/evidence: [actual list]
Permitted advisory actions: [owner/due phase]
Affected blocked scope: [paths/dependencies; independent checks may continue]

### Required Decision Gaps (adr-required; missing link alone is not a gap)
For each gap:
  ❌ TR-[id]: [CDD] → [module] → [requirement]
     Suggested ADR: "/architecture-decision [suggested title]"
     Domain: [domain]
     Technology Risk: [LOW/MEDIUM/HIGH]

### Cross-ADR Conflicts
[List all conflicts from Phase 4]

### ADR Dependency Order
[Topologically sorted implementation order from Phase 4 — dependency ordering section]
[Unresolved dependencies and cycles if any]

### CDD Revision Flags
[CDD assumptions that conflict with verified technology behaviour — from Phase 5b]
[Or: "None — all CDD assumptions consistent with verified technology behaviour"]

### Technology Compatibility Issues
[List all issues from Phase 5]

### Architecture Document Coverage
[List missing systems and orphaned architecture from Phase 6]

---

### Verdict: [PASS / CONCERNS / FAIL]

PASS: Every in-scope requirement/choice has current justified disposition/evidence,
      no required unresolved decision/conflict, technology consistent
CONCERNS: Only permitted advisory repairs remain with owner/due phase
FAIL: Required adr-required/conflict or incomplete required evidence;
      name affected dependencies and continue independent checks

### Blocking Issues (must resolve before PASS)
[List items that must be resolved — FAIL verdict only]

### Required ADRs
[Prioritised list of ADRs to create, most foundational first]
```

## Phase 8: Traceability index

The traceability index format:

```markdown
# Architecture Traceability Index
Last Updated: [date]
Engine: [name + version]

## Coverage Summary
- Total requirements: [N]
- Covered: [X] ([%])
- Partial: [Y]
- Gaps: [Z]

## Full Matrix
[Complete traceability matrix from Phase 3]

## Known Gaps
[All ❌ items with suggested ADRs]

## Superseded Requirements
[Requirements whose CDD was changed after the ADR was written]
```
