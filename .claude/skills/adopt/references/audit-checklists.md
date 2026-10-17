# CDD, ADR and Module-Index Audit Checklists

### 2a: CDD Format Audit

Enter this subsection only for `cdds` or `full` with actual CDDs to audit.
Other subset modes do not enter it. Unknown mode or applicability stays
Unknown; a missing required owner in a selected CDD audit remains incomplete
and must not be used to infer that the audit is inapplicable.

Resolve DocKind/owners under `design/INSTRUCTIONS.md`. Module CDDs use semantic
eight in `rules/design-docs.md`; concept/index/support documents use their own
contract. Read substantive bodies and valid historical aliases. Heading scans
locate content, not compliance. Preserved Game/Product heading examples follow:

**[游戏专用]** Game CDD sections:

| Required Section | Heading pattern to look for |
|---|---|
| Overview | `## Overview` |
| Player Fantasy | `## Player Fantasy` |
| Detailed Rules / Design | `## Detailed` or `## Core Rules` or `## Detailed Design` |
| Formulas | `## Formulas` or `## Formula` |
| Edge Cases | `## Edge Cases` |
| Dependencies | `## Dependencies` or `## Depends` |
| Tuning Knobs | `## Tuning` |
| Acceptance Criteria | `## Acceptance` |

**[通用产品]** Product CDD sections:

| Required Section | Heading pattern to look for |
|---|---|
| Overview | `## Overview` |
| User Promise / JTBD | `## User Promise` or `## User Promise / JTBD` |
| Detailed Behavior | `## Detailed Behavior`, `## Detailed Design` or `## Core Specification` |
| Contracts / Data Model | `## Contracts / Data Model`, `## Data Model` or `## Data` |
| Edge Cases | `## Edge Cases` |
| Dependencies | `## Dependencies` or `## Depends` |
| Configuration Knobs | `## Configuration Knobs` or `## Configuration` |
| Acceptance Criteria | `## Acceptance` |

For each CDD, record:
- Which sections are present
- Which sections are missing
- Whether it has any content in present sections or just placeholder text
  (`[To be designed]` or equivalent)

Also check: does each CDD have a `**Status**:` field in its header block?
Valid values: `In Design`, `Designed`, `In Review`, `Approved`, `Needs Revision`.

### 2b: ADR Format Audit

For each ADR file found, check for these critical sections:

| Section | Impact if missing |
|---|---|
| `## Status` | **BLOCKING** for relied-on coverage — decision status/acceptance unverified |
| `## ADR Dependencies` | HIGH — dependency ordering in `/architecture-review` breaks |
| **[游戏专用]** `## Engine Compatibility` / **[通用产品]** `## Technology Compatibility` or `## Stack Compatibility` | HIGH — post-cutoff API risk is unknown |
| `## CDD Requirements Addressed` | MEDIUM — traceability matrix loses coverage |
| `## Performance Implications` | LOW — not pipeline-critical |

Read the actual applicable ADR template and substantive compatibility body.
Established translated/numbered aliases remain valid when they cover the same
required domain, pinned-version and contract roles; a heading or placeholder alone
is not coverage. Preserve the original heading rather than mechanically renaming it.

For each ADR, record: which sections present, which missing, current Status value
if the Status section exists.

### 2c: module-index.md Format Audit

If `design/cdd/module-index.md` exists, read its complete body and the actual
installed `/map-systems` owner with `templates/module-index.md`. Apply their
required roles and preserve valid historical formats; an index is not a module CDD.

1. **Status meaning and downstream use** — read actual row status and provenance.
   Current workflow labels include `Not Started`, `In Progress`, `In Review`,
   `Designed`, `Approved` and `Needs Revision`. Owner-defined historical labels
   such as `In Design` or `Implemented` remain readable observations; they do not
   establish design approval, passing evidence or stage/Story completion. An
   unknown label needs owner clarification. If parenthetical notes or a legacy
   label break a selected downstream workflow's exact comparison, record that
   affected use as incomplete and propose a separately scoped migration; do not
   silently rewrite history or infer the required completion state.

2. **Column and semantic roles** — `Module Name`, `System name` or a substantive
   equivalent identifies the module. Read category, priority and status, plus
   layer information where the actual generating workflow requires it. `Category`
   is not automatically a layer; an actual layer may be recorded in the body's
   category/priority mapping. Missing required roles remain gaps even when all
   column headings exist. Preserve extra columns and valid owner aliases.
