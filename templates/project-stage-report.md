# Project Stage Analysis Report

**Generated**: [DATE]
**Stage Labels**: [Game: Concept/Systems Design/Technical Setup/Pre-Production/Production/Polish/Release; Product: Concept/Specification/Architecture/Pre-Implementation/Implementation/Verification/Release]
**Declared**: [actual source/value or absent]
**Observed**: [substantive artifacts/status and omissions]
**Candidate**: [advisory indicator and rationale]
**Qualified**: [exact verified governing scope/evidence or unverified]
**Analysis Scope**: [Full project | Specific role: programmer/designer/producer]

---

## Executive Summary

[1-2 paragraph overview of project state, primary gaps, and recommended priority]

**Current Focus**: [What the project is actively working on]
**Blocking Issues**: [Critical gaps preventing progress]
**Estimated Time to Next Stage**: [If applicable]

---

## Completeness Overview

### Design Documentation
- **Status**: [observed / required-owner checks verified or incomplete;
  percentage only with measured scope/numerator/denominator]
- **Files Found**: [N] documents in `design/`
  - CDD sections: [N] files in `design/cdd/`
  - Narrative docs: [N] files in `design/narrative/`
  - Level designs: [N] files in `design/levels/`
- **Key Gaps**:
  - [ ] [Missing doc 1 + why it matters]
  - [ ] [Missing doc 2 + why it matters]

### Source Code
- **Status**: [observed / required-owner checks verified or incomplete;
  percentage only with measured scope/numerator/denominator]
- **Files Found**: [N] source files in `src/`
- **Major Systems Identified**:
  - ✅ [System 1] (`src/path/`) — [brief status]
  - ✅ [System 2] (`src/path/`) — [brief status]
  - ⚠️  [System 3] (`src/path/`) — [issue or incomplete]
- **Key Gaps**:
  - [ ] [Missing system 1 + impact]
  - [ ] [Missing system 2 + impact]

### Architecture Documentation
- **Status**: [observed / required-owner checks verified or incomplete;
  percentage only with measured scope/numerator/denominator]
- **ADRs Found**: [N] decisions documented in `docs/architecture/`
- **Coverage**:
  - ✅ [Decision area 1] — documented
  - ⚠️  [Decision area 2] — undocumented but implemented
  - ❌ [Decision area 3] — neither documented nor decided
- **Key Gaps**:
  - [ ] [Missing ADR 1 + why it's needed]
  - [ ] [Missing ADR 2 + why it's needed]

### Production Management
- **Status**: [observed / required-owner checks verified or incomplete;
  percentage only with measured scope/numerator/denominator]
- **Found**:
  - Sprint plans: [N] in `production/sprints/`
  - Milestones: [N] in `production/milestones/`
  - Roadmap: [Exists | Missing]
- **Key Gaps**:
  - [ ] [Missing production artifact + impact]

### Testing
- **Status**: [actual measured coverage/execution scope and denominator, or unknown]
- **Test Files**: [N] in `tests/`
- **Coverage by System**:
  - [System 1]: [bound measured result or unknown]
  - [System 2]: [bound measured result or unknown]
- **Key Gaps**:
  - [ ] [Missing test area + risk]

### Prototypes
- **Active Prototypes**: [N] in `prototypes/`
  - ✅ [Prototype 1] — documented with README
  - ⚠️  [Prototype 2] — no README, unclear status
- **Archived**: [N] (experiments completed)
- **Key Gaps**:
  - [ ] [Undocumented prototype + why it matters]

---

## Stage Classification Rationale

**Why [Candidate], and what is actually qualified?**

[Explain candidate indicators separately from declared and qualified facts.
Counts locate work; they do not prove required checks or completion.]

**Indicators for this stage**:
- [Indicator 1 that matches this stage]
- [Indicator 2 that matches this stage]

**Next stage requirements**:
- [ ] [Requirement 1 to reach next stage]
- [ ] [Requirement 2 to reach next stage]
- [ ] [Requirement 3 to reach next stage]

---

## Gaps Identified (with Clarifying Questions)

### Critical Gaps (block progress)

1. **[Gap Name]**
   - **Impact**: [Why this blocks progress]
   - **Question**: [Clarifying question before assuming solution]
   - **Suggested Action**: [What could be done, pending clarification]

### Important Gaps (affect quality/velocity)

2. **[Gap Name]**
   - **Impact**: [Why this matters]
   - **Question**: [Clarifying question]
   - **Suggested Action**: [Proposed solution]

### Nice-to-Have Gaps (polish/best practices)

3. **[Gap Name]**
   - **Impact**: [Minor but valuable]
   - **Question**: [Clarifying question]
   - **Suggested Action**: [Optional improvement]

---

## Recommended Next Steps

### Immediate Priority (Do First)
1. **[Action 1]** — [Why it's priority 1]
   - Suggested skill: `/[skill-name]` or manual work
   - Estimated effort: [S/M/L]

2. **[Action 2]** — [Why it's priority 2]
   - Suggested skill: `/[skill-name]`
   - Estimated effort: [S/M/L]

### Short-Term (This Sprint/Week)
3. **[Action 3]** — [Why it's important soon]
4. **[Action 4]** — [Why it's important soon]

### Medium-Term (Next Milestone)
5. **[Action 5]** — [Future need]
6. **[Action 6]** — [Future need]

---

## Role-Specific Recommendations

[If role filter was used, provide role-specific guidance]

### For [Role]:
- **Focus areas**: [What this role should prioritize]
- **Blockers**: [What's blocking this role's work]
- **Next tasks**:
  1. [Task 1]
  2. [Task 2]

---

## Follow-Up Skills to Run

Based on gaps identified, consider running:

- `/reverse-document [type] [path]` — [For which gap]
- `/architecture-decision` — [For which gap]
- `/sprint-plan` — [If production planning missing]
- `/milestone-review` — [If approaching deadline]
- `/onboard [role]` — [If new contributor joining]

---

## Appendix: File Counts by Directory

```
design/
  cdd/           [N] files
  narrative/     [N] files [Game]
  levels/        [N] files [Game]
  ux/            [N] applicable artifacts [Product]

src/
  core/          [N] files
  gameplay/      [N] files
  ai/            [N] files
  networking/    [N] files
  ui/            [N] files
  api/cli/services/data/ [N] actual capability files [Product]

docs/
  architecture/  [N] ADRs

production/
  sprints/       [N] plans
  milestones/    [N] definitions

tests/           [N] test files
prototypes/      [N] directories
```

---

**End of Report**

*Generated by `/project-stage-detect` skill*

Use `standards/technical-preferences.md` domain/capability evidence and
`standards/evidence-lifecycle.md` for exact relied-on input/review claims.
If an actual project retains legacy `design/gdd/`, record that original path
separately; canonical CDD owner remains `design/cdd/`, without silently relocating
or copying content. Narrative/levels/gameplay examples remain Game-specific;
Product evidence covers
actual user promise/API/CLI/data/auth/workflow surfaces. A generated report is
not a gate pass, runtime activation or qualification.
