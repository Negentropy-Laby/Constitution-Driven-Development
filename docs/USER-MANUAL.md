# User Manual

This manual is the practical operating guide for Constitution Driven
Development. It explains how to start a new game or product project, how to
bring an existing project under CDD governance, how to move through phase gates,
and where release evidence is recorded.

For the shortest first-step decision table, start with `docs/START-HERE.md`.
For the full phase-by-phase workflow, use `docs/WORKFLOW-GUIDE.md`.

## What CDD Provides

Constitution Driven Development turns an AI-agent workspace into a governed
development team:

- 53 specialized agents for design, engineering, QA, release, and operations.
- 74 slash-command skills for planning, implementation, review, and release.
- A 7-phase workflow catalog read by `/help`, `/cdd-status`, and gate checks.
- Templates for concepts, CDDs, ADRs, UX specs, test plans, release notes, and
  acceptance evidence.

CDD is collaborative rather than autonomous. The human owner makes binding
product and project decisions; agents ask questions, present options, draft
artifacts, and request approval before writing or committing work.

## The Project Brain: memory_bank/

`memory_bank/` is the project brain and governance control plane, not a
replacement for the working directories. Keep full CDDs in `design/`,
architecture in `docs/architecture/`, workflow contracts in `workflow/`,
reusable templates in `templates/`, shared standards in `standards/`, and
execution artifacts in `production/`. The memory bank indexes, mirrors, and
summarizes those sources.

The layers are:

| Layer | Purpose |
|-------|---------|
| `t0_core/` | Current laws, active state, release state, and amendments. |
| `t1_axioms/` | Supporting technical, architecture, UX, QA, behavior, and module context. |
| `t2_execution/` | Workflow contract, phase/gate mirrors, current roadmap, framework contract, and recorded adapter freshness. |
| `t3_archive/` | Historical indexes for QA, release, gate, review, story, sprint, milestone, and amendment evidence. |

Run `/constitute` to initialize or refresh the memory-bank skeleton. Run
`/constitute-check` to audit T0-T3 health. Run `/cdd-status` to update
`production/project-roadmap.md` and, when `memory_bank/` exists,
`memory_bank/t2_execution/current_roadmap.md`.

`/constitute` initializes `framework_contract.md` and an `uninitialized`
`adapter_state.yaml`. `/constitute-check` reads actual installed files without a maintenance kit.
Live Source freshness needs the designated external Source and an available
authorized checker; unavailable checks preserve the recorded state. A fresh or
stale state write requires the complete draft and its covered authority. `/cdd-status` displays that recorded state without
recomputing it or changing phase ordering.

T3 is the audit index layer. Gate decisions, review artifacts, QA validation,
smoke/team QA sign-off, story closure, sprint/milestone snapshots, and release
evidence stay in their normal working paths. T3 index changes require their own
covered named effects when `memory_bank/` exists.

Any high-impact workflow that produces a `PASS/FAIL`, `APPROVED/REJECTED`,
`GO/NO-GO`, `PROCEED/PIVOT/KILL`, `CUT/KEEP/DEFER`, or `RELEASE/HOLD` decision
may update only the exact T1, T0 or T3 effects covered by continuing authority.
Saving an artifact alone does not approve index/state changes or acceptance.

### Where Do I Look?

| Question | Look here |
|----------|-----------|
| What are the current project laws? | `memory_bank/t0_core/basic_law_index.md` |
| What phase are we in? | `memory_bank/t0_core/current_state.md` |
| Why did we choose this architecture? | `memory_bank/t1_axioms/architecture_context.md` and `docs/architecture/adr-*.md` |
| What should happen next? | `/help`, `/cdd-status`, `memory_bank/t2_execution/current_roadmap.md` |
| What does this phase require? | `memory_bank/t2_execution/phase_checklists.md` |
| Why did a gate pass or fail? | `memory_bank/t3_archive/gate_runs/` |
| What QA evidence exists? | `memory_bank/t3_archive/qa_evidence_index.md` |
| What reviews happened? | `memory_bank/t3_archive/reviews/review-index.md` |
| What story closure evidence exists? | `memory_bank/t3_archive/sprint_snapshots/story-closure-index.md` |
| What release proof exists? | `memory_bank/t3_archive/release_evidence/` |
| What tests CDD skills and agents? | `skill_testing/` |
| Where are skill-test and skill-improve results? | `memory_bank/t3_archive/skill_testing/` |

## Prerequisites

Install these tools before using the template:

- Git.
- An AI agent runtime — Claude Code (`npm install -g @anthropic-ai/claude-code`),
  Codex, or both. Both runtimes share the same canonical sources.
- The actual project's configured language/runtime, build and test tools.
- Python 3.11+ only when separately supplied local maintenance diagnostics are
  actually available and authorized; it is not a normal-use prerequisite.
- `jq`, recommended for hook validation (hooks fall back to `grep` when absent).

Clone the designated Source library to inspect its delivered templates.
Apply the purpose rule to skills, independent agent/role definitions, native
configuration containing instruction bodies and their exclusive references/overlays.
A Target's development-only role stays local-only even without invoking a skill;
TOML, developer_instructions fields and native loading give no exception. Real
product-use agents follow actual product rules. Independent configuration must be
independent of development instructions/role packages and carry no such body;
a native loader of developer roles is not an independent configuration consumer.

For a Target, first classify complete skills under `standards/skill-purpose.md`:
using delivered functions differs from developing this project. Development-only
bodies/exclusive references/overlays stay local-only, including bespoke projections.
Split mixed packages; product-use skills may be project product capabilities. Review
minimal adaptation/independent-configuration Git candidates apart from local inputs
in `adapters/README.md`; these categories cannot carry development-instruction bodies. Install required
neutral templates/specs and generic standards/workflow originals as readable
local-only inputs; do not add them or general Source mirrors to Target Git delivery.
A fresh Target clone may need those inputs and complete development-instruction packages/references
installed separately before affected CDD development use.
Preserve project-specific inputs and
customizations before import or update.

```bash
git clone https://github.com/Negentropy-Laby/Constitution-Driven-Development.git my-cdd-project
cd my-cdd-project
claude   # or: codex  (run from the repo root so your runtime finds CLAUDE.md / AGENTS.md)
```

This manual uses slash-prefixed names as logical CDD notation. Claude Code
invokes skills with that form. In Codex, use `/skills` to browse or `$name`
syntax for an explicit invocation; for example, start with `$constitute`.

`jq` is optional where a configured hook provides a fallback. Core collaborative
workflows read installed files directly; local maintenance scripts and historical
Source CI are excluded from the delivered-template prerequisites.

## First Command

Use this decision table for the first command in a new session:

| Situation | First command | What happens |
|-----------|---------------|--------------|
| New game project | `/constitute` | Creates or refreshes `memory_bank/` T0-T3 governance, ratifies project laws, sets review mode, and routes concept work. |
| New product, API, CLI, web app, SDK, or data pipeline | `/constitute` | Creates or refreshes `memory_bank/` T0-T3 governance, ratifies product principles, sets review mode, and routes workflow planning. |
| Existing project adoption | `/project-stage-detect` | Reads current artifacts and recommends the next missing CDD step. |
| Unsure what to do next | `/help` | Reads workflow evidence and reports the next required step. |
| Need a saved status report | `/cdd-status` | Writes `production/project-roadmap.md` and the T2 roadmap mirror when `memory_bank/` exists. |

Run `/help` whenever the next step is unclear. Run `/cdd-status` when you need a
persisted dashboard for handoff, review, or planning.

Every slash command includes a local `User Guide` block that states when to use
it, required inputs, expected outputs, memory-bank writes, and recommended next
steps. Those next steps are guidance only; they do not auto-run without an
explicit command and approval.

For Codex, “slash command” in the workflow tables means the logical CDD command;
invoke the matching skill with `$name` or choose it from `/skills`.

## New Game Path

1. Run `/constitute` to create `memory_bank/`, ratify T0 laws, initialize T1
   context, T2 mirrors, and T3 audit indexes.
2. If the idea is still open, run `/brainstorm game ideas`.
3. Review the concept with `/design-review`.
4. Run `/gate-check concept` before moving to systems design.
5. Run `/map-systems`, then `/design-system [system-name]` for each MVP system.
6. Run `/review-all-gdds` and `/gate-check systems-design`.
7. Run `/setup-engine [engine] [version]`, then architecture and test setup.
8. Build through `/create-epics`, `/create-stories`, `/sprint-plan`,
   `/story-readiness`, `/dev-story`, and `/story-done`.
9. Validate with `/playtest-report`, `/team-polish`, and `/gate-check polish`.
10. Release through `/release-checklist`, `/launch-checklist`, and
    `/team-release`.

Game projects should choose exactly one engine track during setup: Godot, Unity,
or Unreal. Use the corresponding engine reference under `docs/engine-reference/`
after `/setup-engine` records the selected stack.

## New Product Path

1. Run `/constitute` to create `memory_bank/`, ratify T0 laws, initialize T1
   context, T2 mirrors, and T3 audit indexes.
2. If the problem or workflow is still open, run `/brainstorm product ideas`.
3. Review the concept with `/design-review`.
4. Run `/gate-check concept` before moving to specification.
5. Run `/map-systems`, then `/design-system [module-name]` for each MVP module.
6. Run `/review-all-gdds` and `/gate-check systems-design`.
7. Run `/setup-engine [language] [framework]`, for example
   `/setup-engine python 3.13 fastapi`.
8. Create architecture, ADRs, accessibility requirements, and test setup.
9. Design the core UX with `/ux-design`, review it with `/ux-review`, and
   validate the workflow with `/prototype` and `/playtest-report`.
10. Build through epics, stories, sprint planning, implementation, and
    `/story-done`.
11. Release through `/release-checklist`, `/launch-checklist`, and
    `/team-release`.

Product projects should use the language-specialist agents that match the
chosen stack. Python, TypeScript, Rust, and Go specialists are included.

## Technical Setup

Technical Setup has two tracks. Complete both before moving to production work.

### Architecture Track

Use this track to record the technology foundation and implementation rules:

1. Run `/setup-engine` with the selected engine or product stack.
2. Run `/create-architecture` to produce the master architecture.
3. Run `/architecture-decision` for significant technical decisions.
4. Run `/architecture-review` to validate ADR coverage and dependency order.
5. Run `/create-control-manifest` to extract implementation rules for
   programmers.

### Readiness Track

Use this track to make implementation testable and reviewable:

1. Create `design/accessibility-requirements.md` from the accessibility
   template when the project needs an explicit accessibility baseline.
2. Run `/test-setup` to establish the required test baseline for the selected
   engine or product stack.
3. Run `/gate-check technical-setup` after the architecture and readiness
   artifacts exist.

After Technical Setup passes, continue to UX, prototype, epics, stories, sprint
planning, and implementation.

## Existing Project Adoption

For a brownfield project, do not start by writing new CDDs blindly:

1. Run `/project-stage-detect`.
2. Review the detected phase, missing artifacts, and risks.
3. Run `/adopt` when the project needs a migration plan.
4. Run `/constitute` in existing-project mode when governing principles are
   missing or stale.
5. Retrofit only the missing artifacts required for the detected phase.
6. Run the relevant `/gate-check` before advancing to later phases.

The goal is to align the project with the CDD workflow without overwriting
working code or inventing documentation that contradicts the current system.

## Gates And Overrides

CDD phase gates are governed advisory checks:

- A normal phase advance requires the matching `/gate-check`.
- A `PASS` allows normal advancement.
- `CONCERNS` may advance with documented risk notes.
- `FAIL` does not advance `production/stage.txt` unless the user explicitly
  overrides it and records the risk.

The authoritative workflow sequence is `workflow/workflow-catalog.yaml`.
The generated phase artifact map is `docs/PHASE-CHECKLISTS.md`.

## Generated Artifacts

Common generated or maintained artifacts include:

| Artifact | How it is created |
|----------|-------------------|
| `memory_bank/t0_core/basic_law_index.md` | `/constitute` |
| `memory_bank/t0_core/current_state.md` | `/constitute`, `/gate-check` |
| `memory_bank/t0_core/release_state.md` | `/constitute`, `/team-release`, `/hotfix` |
| `memory_bank/t0_core/amendment_log.md` | `/constitute` amendment workflow |
| `memory_bank/t1_axioms/tech_context.md` | `/constitute`, `/setup-engine` |
| `memory_bank/t1_axioms/*` | `/constitute`, architecture, UX, QA, and design workflows |
| `memory_bank/t2_execution/phase_checklists.md` | `/constitute` copies the delivered `docs/PHASE-CHECKLISTS.md` after reading the governing catalog |
| `memory_bank/t2_execution/gate_required_artifacts.md` | `/constitute` copies the delivered `workflow/generated/gate-required-artifacts.md` |
| `memory_bank/t2_execution/current_roadmap.md` | `/cdd-status` |
| `memory_bank/t2_execution/framework_contract.md` | Initialized from its template by `/constitute` |
| `memory_bank/t2_execution/adapter_state.yaml` | Initialized by `/constitute`; recorded only by approved `/constitute-check`; read by `/cdd-status` |
| `skill_testing/catalog.yaml` | Cross-project registry for `/skill-test` and `/skill-improve` |
| `skill_testing/quality-rubric.md` | Cross-project rubric for `/skill-test category` and `/skill-improve` |
| `skill_testing/specs/` | Reusable skill/agent behavioral specs |
| `memory_bank/t2_execution/skill_testing/README.md` | `/constitute`; memory-bank T2 mount contract for the canonical `skill_testing/` assets |
| `memory_bank/t3_archive/gate_runs/` | `/gate-check` |
| `memory_bank/t3_archive/reviews/review-index.md` | Review workflows, `/prototype`, `/code-review`, `/scope-check` |
| `memory_bank/t3_archive/qa_evidence_index.md` | `/playtest-report`, `/smoke-check`, `/team-qa`, `/test-evidence-review`, `/bug-triage` |
| `memory_bank/t3_archive/sprint_snapshots/story-closure-index.md` | `/story-done` |
| `memory_bank/t3_archive/release_evidence/` | `/team-release`, `/hotfix` |
| `memory_bank/t3_archive/amendments/` | `/constitute` amendment workflow |
| `memory_bank/t3_archive/skill_testing/coverage-index.yaml` | `/skill-test` approved evidence updates |
| `memory_bank/t3_archive/skill_testing/results/` | `/skill-test` approved static/spec/category/audit reports |
| `memory_bank/t3_archive/skill_testing/improvements/` | `/skill-improve` approved improvement records |
| `production/review-mode.txt` | `/constitute` |
| `production/project-roadmap.md` | `/cdd-status` |
| `docs/PHASE-CHECKLISTS.md` | Delivered catalog-derived view; update its Source owner within authorized scope |
| `design/ux/surface-profile.md` | Surface-profile template or UX workflow |
| `production/qa/evidence/` | QA, smoke, manual, and validation evidence workflows |

Delivered views and T2 mirrors must remain consistent with their catalog owner.
Read complete required originals and use `/constitute` for authorized ordinary
mirror copies. Changed Source views need scoped Source-authoring review; missing
inputs remain incomplete rather than triggering an absent local generator.

## Release And Acceptance

The release path is:

```text
/release-checklist -> /launch-checklist -> /team-release
```

Before publishing a release candidate, perform the applicable delivery checks in
`docs/CUSTOMER-ACCEPTANCE.md` and the actual project's configured tests, QA and
release workflows. Preserve the exact revision/input identities and observed
results; required missing evidence remains unresolved.

Historical Source release records may include `Template Consistency` on Ubuntu,
macOS and Windows or a credential-free `Runtime Contract` trial. Cite such a
record only for its matching run ID and `headSha`; those local-only workflows are
not required files in current template delivery and do not certify a changed
delivery or live agent behavior. Evidence publication, release acceptance and
project completion each require their own covered authority.

## Troubleshooting

| Symptom | What to check |
|---------|---------------|
| `/help` suggests a surprising step | Run `/cdd-status` and inspect missing required artifacts. |
| A gate fails unexpectedly | Read the gate output, then compare it with `workflow/workflow-catalog.yaml` and `docs/PHASE-CHECKLISTS.md`. |
| A supplied local diagnostic fails | Inspect its exact output and required inputs; repair the owning source within scope and keep the result separate from project QA. |
| Workflow consistency fails | Read the reported contract drift and update the source document or generated artifact that owns the contract. |
| Project CI fails on one platform | Inspect the actual configured job; retain failed results and do not relabel historical evidence. |
| Existing project docs conflict with implementation | Run `/project-stage-detect` and `/adopt`; do not assume the docs are more current than the code. |

When in doubt, stop at the current phase, run `/help`, then make the smallest
documented change needed to satisfy the next gate.
