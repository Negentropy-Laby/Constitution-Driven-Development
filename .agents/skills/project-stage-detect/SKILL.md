---
name: project-stage-detect
description: "Automatically analyze project state, detect stage, identify gaps, and recommend next steps based on existing artifacts. Use when user asks 'where are we in development', 'what stage are we in', 'full project audit'."
argument-hint: "[optional: role filter like 'programmer' or 'designer']"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Write
model: haiku
# Read-only diagnostic skill — no specialist agent delegation needed
---
Read and apply `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`,
`standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md` for scoped
authority, exact evidence and decision ownership. Existing named authority
continues; analysis is read-only and report-only excludes input/index/state writes.


## User Guide

- When to use: Automatically analyze project state, detect stage, identify gaps, and recommend next steps based on existing artifacts. Use when user asks 'where are we in development', 'what stage are we in', 'full project audit'.
- Inputs: Command arguments: `/project-stage-detect [optional: role filter like 'programmer' or 'designer']`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Project Stage Detection

This skill scans your project to determine its current development stage, completeness
of artifacts, and gaps that need attention. It's especially useful when:
- Starting with an existing project
- Onboarding to a codebase
- Checking what's missing before a milestone
- Understanding "where are we?"

---

## Workflow

### 1. Scan Key Directories

Analyze project structure and content:

**Design Documentation** (`design/`):
- Count CDD files in `design/cdd/*.md`
- Check for game-concept.md or product-concept.md, principles.md, module-index.md
- If module-index.md exists, count total systems vs. designed systems
- Analyze completeness (Overview, Detailed Design, Edge Cases, etc.)
- [Game] Locate narrative and level docs in their existing paths.
- [Product] Read actual user promises/API/CLI/data/auth/workflow contracts and
  surface profile; locate modules from the actual layout.

**Source Code** (`src/`):
- Count source files (language-agnostic)
- Identify major systems (directories with 5+ files)
- [Game] Locate actual core/gameplay/AI/networking/UI systems.
- [Product] Locate actual API/CLI/services/data/jobs/workers/app/web systems;
  established alternative paths remain valid.
- Estimate lines of code (rough scale)

**Production Artifacts** (`production/`):
- Read `stage.txt` directly before classifying the declared stage. Discovery
  filters, file-extension lists and ignore-aware searches can omit existing
  files. Preserve its actual body/value even when observed work disagrees.
  Claim absence only from a direct path-specific check; an unperformed or
  inaccessible read remains unverified, never "no explicit stage found".
- Check for active sprint plans
- Look for milestone definitions
- Find roadmap documents

**Prototypes** (`prototypes/`):
- Count prototype directories
- Check for READMEs (documented vs undocumented)
- Assess if prototypes are archived or active

**Architecture Docs** (`docs/architecture/`):
- Count ADRs (Architecture Decision Records)
- Check for overview/index documents

**Tests** (`tests/`):
- Count test files
- Read measured execution/coverage evidence with exact scope/denominator;
  unavailable measurement stays unknown, never inferred from test-file count.

### 2. Classify Project Stage

Apply `standards/technical-preferences.md` actual domain/capability evidence;
missing concepts never default Game. Separate **declared** stage/owner statement,
**observed** bodies/artifacts, **candidate** advisory ongoing-work stage, and
**qualified** transition only with exact required checks, decisions/reviews and
transition authority. Preserve discrepant declarations and report gaps; never
write stage/current state. Indicators below suggest candidates only:

**[游戏专用] Game stage indicators:**
| Stage | Indicators |
|-------|-----------|
| **Concept** | No concept doc, brainstorming phase |
| **Systems Design** | Game concept exists, module index missing or incomplete |
| **Technical Setup** | Module index exists, engine not configured |
| **Pre-Production** | Configured Game setup and observed implementation planning |
| **Production** | Actual ongoing Game implementation; counts describe scale only |
| **Polish** | Explicit only (set by `/gate-check` Production → Polish gate) |
| **Release** | Explicit only (set by `/gate-check` Polish → Release gate) |

**[通用产品] Product stage indicators:**
| Stage | Indicators |
|-------|-----------|
| **Concept** | No concept doc, discovery phase |
| **Specification** | Product concept exists, module index missing |
| **Architecture** | Module index exists, technology stack not configured |
| **Pre-Implementation** | Configured Product setup and implementation planning |
| **Implementation** | Actual ongoing Product implementation; counts describe scale only |
| **Verification** | Explicit only (set by `/gate-check` Implementation → Verification gate) |
| **Release** | Explicit only (set by `/gate-check` Verification → Release gate) |

### 3. Collaborative Gap Identification

**DO NOT** just list missing files. Instead, **ask clarifying questions**:

**[游戏专用]** Game gap questions:
- "I see combat code (`src/gameplay/combat/`) but no `design/cdd/combat-system.md`. Was this prototyped first, or should we reverse-document?"

**[通用产品]** Product gap questions:
- "I see API code (`src/api/`) but no `design/cdd/api-service.md`. Was this built ad-hoc, or should we reverse-document?"

**[通用场景]** Shared gap questions:
- "You have 15 ADRs but no architecture overview. Should I create one to help new contributors?"
- "No sprint plans in `production/`. Are you tracking work elsewhere (Jira, Trello, etc.)?"
- "I found a concept document but no module index. Have you decomposed the concept into individual modules yet, or should we run `/map-systems`?"
- "Prototypes directory has 3 projects with no READMEs. Were these experiments, or do they need documentation?"

### 4. Generate Stage Report

Use template: `templates/project-stage-report.md`

**Report structure**:
```markdown
# Project Stage Analysis

**Date**: [date]
**Stage**: [Concept / Systems Design or Specification / Technical Setup or Architecture / Pre-Production or Pre-Implementation / Production or Implementation / Polish or Verification / Release]
**Declared / Observed / Candidate / Qualified**: [separate values/exact sources;
qualified unverified until governing evidence checked]
**Diagnostic Confidence**: [HIGH/MEDIUM/LOW with actual evidence/omissions;
file existence does not establish HIGH qualification]

## Completeness Overview
- Design: [observed substantive bodies and required-owner gaps]
- Code: [observed files/systems; count is not completion percentage]
- Architecture: [observed decisions and exact acceptance/coverage evidence]
- Production: [recorded planning/status and verified evidence separately]
- Tests: [measured coverage/execution scope or unknown; counts only locate files]

## Gaps Identified
1. [Gap description + clarifying question]
2. [Gap description + clarifying question]

## Recommended Next Steps
[Priority-ordered list based on stage and role]
```

### 5. Role-Filtered Recommendations (Optional)

If user provided a role argument (e.g., `/project-stage-detect programmer`):

**Programmer**:
- Focus on architecture docs, test coverage, missing ADRs
- Code-to-docs gaps

**Designer**:
- Focus on CDD completeness, missing design sections
- Prototype documentation

**Producer**:
- Focus on sprint plans, milestone tracking, roadmap
- Cross-team coordination docs

**General** (no role):
- Holistic view of all gaps
- Highest-priority items across domains

### 6. Request Approval Before Writing

**Collaborative protocol**:
```
I've analyzed your project. Here's what I found:

[Show summary]

Gaps identified:
1. [Gap 1 + question]
2. [Gap 2 + question]

Recommended next steps:
- [Priority 1]
- [Priority 2]
- [Priority 3]

May I write the full stage analysis to production/project-stage-report.md?
```

Default output is conversational. Reuse exact report-write authority; ask after
summary only for missing/new effects. Preserve prior revisions; report-only
excludes stage/index/checkpoint. Review-only/declined saving invokes no write entrypoint.

---

## Example Usage

```bash
# General project analysis
/project-stage-detect

# Programmer-focused analysis
/project-stage-detect programmer

# Designer-focused analysis
/project-stage-detect designer
```

---

## Follow-Up Actions

After generating the report, suggest relevant next steps:

- **Concept exists but no module index?** → `/map-systems` to decompose into modules
- **Missing design docs?** → `/reverse-document design src/[system]`
- **Missing architecture docs?** → `/architecture-decision` or `/reverse-document architecture`
- **Prototypes need documentation?** → `/reverse-document concept prototypes/[name]`
- **No sprint plan?** → `/sprint-plan`
- **Approaching milestone?** → `/milestone-review`

---

## Collaborative Protocol

This skill follows the collaborative design principle:

1. **Question First**: Ask about gaps, don't assume
2. **Present Options**: "Should I create X, or is it tracked elsewhere?"
3. **User Decides**: Wait for direction
4. **Show Draft**: Display report summary
5. **Scoped report write**: reuse named authority, asking "May I write to
   production/project-stage-report.md?" only for missing/new effects.

Never silently expand scope. Show findings before new authority; covered scope
continues. Definitions/metadata cannot certify autoload, agent execution, spec/
category qualification or installed versions. Read `adapters/README.md` and actual
supported runtime evidence.
