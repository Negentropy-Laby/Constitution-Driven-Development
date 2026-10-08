# Skill Quality Rubric

Used by `/skill-test category [name|all]` to evaluate skills beyond structural compliance.
Each category defines 4–5 binary PASS/FAIL metrics specific to the skill's job.

A metric is PASS when the skill's written instructions clearly satisfy the criterion.
A metric is FAIL when the instructions are absent, ambiguous, or contradictory.
A metric is WARN when the instructions partially address the criterion.

---

## Shared Evaluation Contract

Apply `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`, `standards/evidence-lifecycle.md`
and `standards/notes-adr-sync.md` across categories. Phrase/count presence is
structural evidence only; evaluate actual behavior and disclose unexecuted cases.
Named changeset authority persists across roles/files/retries. Report-only excludes
input/index/state; review-only invokes no write entrypoint. Separate content/write/
review/acceptance/publication/completion; required decisions block affected work.

## Skill Categories

### `gate`

**Skills**: gate-check

Gate skills control phase transitions. They must enforce correctness without
auto-advancing stage and must respect the three review modes.

| Metric | PASS criteria |
|---|---|
| **G1 — Review mode read** | Skill resolves the per-run review override, then `production/review-mode.txt`, then `lean` once per run and applies it before each director gate |
| **G2 — Full mode: all 4 directors spawn** | In `full` mode, all 4 Tier-1 directors (CD, TD, PR, AD) PHASE-GATE prompts are invoked in parallel |
| **G3 — Lean mode: PHASE-GATE only** | In `lean` mode, only `*-PHASE-GATE` gates run; inline gates (CD-PILLARS, TD-ARCHITECTURE, etc.) are skipped |
| **G4 — Solo mode: no directors** | In `solo` mode, no director gates spawn; each is noted as "skipped — Solo mode" |
| **G5 — No auto-advance** | Stage/current-state changes need explicit transition authority and required checks; report-write approval alone is insufficient |

---

### `review`

**Skills**: design-review, architecture-review, review-all-gdds

Review skills read documents and produce structured verdicts. They are primarily
read-only and must not trigger director gates during the analysis phase.

| Metric | PASS criteria |
|---|---|
| **R1 — Read-only enforcement** | Review-only invokes no write entrypoint. Report-only writes the new assigned report, excluding inputs/index/state. Input repair is a separate writer action with fresh review baseline |
| **R2 — Required owner/body check** | Skill resolves actual DocKind and required owners under `design/INSTRUCTIONS.md`. Module CDDs satisfy semantic eight through substantive bodies/valid aliases; concept/index/support docs and architecture use their own owner contract. Counts/headings alone are not PASS. |
| **R3 — Correct verdict vocabulary** | Verdict is exactly one of: APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED (design) or PASS / CONCERNS / FAIL (architecture) |
| **R4 — Actual review workflow** | Skill follows its selected workflow's actual gate/consultation definition, mode, scope and required reviewer independence. Never invent director gates, actor completion or a passing result; unavailable required review remains incomplete. |
| **R5 — Structured findings** | Output contains a per-section status table or checklist before the final verdict |

> **Exceptions:**
> - `design-review`: Has `Write, Edit` in allowed-tools to support an optional "Revise now" path (all writes gated behind user approval) and to write review logs. R1 is satisfied because the reviewed document is never silently modified.
> - `architecture-review`: Performs its actual traceability/disposition/technology audit
>   and configured technology specialist consultation. It has no TD-ARCHITECTURE or
>   LP-FEASIBILITY gate; those belong to `create-architecture`. Required independence
>   follows `standards/evidence-lifecycle.md`, not an invented global gate.

---

### `authoring`

**Skills**: design-system, quick-design, architecture-decision, ux-design, ux-review, art-bible, create-architecture

Authoring skills create or update design documents collaboratively. Full GDD/UX
authoring skills use a section-by-section cycle; lightweight authoring skills use
a single-draft pattern appropriate to their smaller scope.

| Metric | PASS criteria |
|---|---|
| **A1 — Scoped iterative drafting** | Full authoring skills (design-system, ux-design, art-bible) draft and verify sections incrementally within an approved document, batch or synchronization scope without repeated approval before the next section. Ask for material unresolved choices, new effects, or explicit per-section review preferences. Lightweight skills (quick-design, architecture-decision, create-architecture) may present one complete draft/summary for appropriate small scope; matching existing authority continues. |
| **A2 — Scoped authority** | Named document/changeset approval covers listed sections, skeletons and checkpoint effects. Ask only for material new scope; honor explicit per-section review preferences. |
| **A3 — Retrofit mode** | Skill detects if the target file already exists and offers to update specific sections rather than overwriting the whole document. Lightweight skills (quick-design) that always create new files are exempt. |
| **A4 — Director gate at correct tier** | If a director gate is defined for this skill (e.g., CD-GDD-ALIGN, TD-ADR), it runs at the correct mode threshold (full/lean) — NOT in solo |
| **A5 — Preserve progress and existing content** | For new full documents, create the authorized section skeleton before filling it. For retrofit/synchronization, preserve existing body, named sections and evidence, updating only approved scope; never replace it with an empty skeleton. Lightweight new documents may use a complete single draft. Checkpoint writes need their own effect in scope. |

> **Full authoring skills** (must pass all 5 metrics): `design-system`, `ux-design`, `art-bible`
> **Lightweight authoring skills** (A1, A2, A5 use single-draft pattern; A3 exempt for new-file-only skills): `quick-design`, `architecture-decision`, `create-architecture`
> **Review-mode skill** (evaluated against review metrics): `ux-review`

---

### `readiness`

**Skills**: story-readiness, story-done

Readiness skills validate stories before or after implementation. They must produce
multi-dimensional verdicts and integrate correctly with director gate mode.

| Metric | PASS criteria |
|---|---|
| **RD1 — Multi-dimensional check** | Skill checks ≥3 independent dimensions (e.g., Design, Architecture, Scope, DoD) and reports each separately |
| **RD2 — Three verdict levels** | Readiness READY/NEEDS WORK/BLOCKED; closure COMPLETE/COMPLETE WITH NOTES/BLOCKED. Both closure completion levels require every required AC/evidence/review/authority satisfied. Legacy RISKS aliases NOTES only with those same facts. |
| **RD3 — Required gaps retain truth** | Readiness distinguishes remediable NEEDS WORK from external/decision BLOCKED. Closure is BLOCKED for any required FAIL/NotRun/Blocked/Pending/Unknown or missing required decision/review/authority, even if author can repair. Optional orchestration/risk acceptance waives no required AC or test truth. |
| **RD4 — Director gate at correct mode** | QL-STORY-READY or LP-CODE-REVIEW gate spawns in `full` mode, skips in `lean`/`solo` with a noted skip message |
| **RD5 — Next-story handoff** | After completion, skill surfaces the next READY story from the active sprint |

---

### `pipeline`

**Skills**: create-epics, create-stories, dev-story, create-control-manifest, propagate-design-change, map-systems

Pipeline skills produce artifacts that other skills consume. They must write files
with correct schema, respect layer/priority ordering, and gate before writing.

| Metric | PASS criteria |
|---|---|
| **P1 — Correct output schema** | Each produced file follows the project template (EPIC.md, story frontmatter, etc.); skill references the template path |
| **P2 — Layer/priority ordering** | Skills that produce epics or stories respect layer ordering (core → extended → meta) and priority fields |
| **P3 — Named changeset approval** | Present draft/summary plus paths/effects before new authority. One named batch may cover all listed artifacts; scope continues across roles/files/retries, asking only for material new effects |
| **P4 — Director gate at correct tier** | In-scope gates (PR-EPIC, QL-STORY-READY, LP-CODE-REVIEW, etc.) run in `full`, skip in `lean`/`solo` with noted skip |
| **P5 — Reads before writes** | Skill reads the relevant GDD/ADR/manifest before producing artifacts to ensure alignment |

---

### `analysis`

**Skills**: consistency-check, balance-check, content-audit, code-review, tech-debt,
scope-check, estimate, perf-profile, asset-audit, security-audit, test-evidence-review, test-flakiness

Analysis skills scan the project and surface findings. They are read-only during
analysis and must ask before recommending any file writes.

| Metric | PASS criteria |
|---|---|
| **AN1 — Read-only scan** | Analysis phase uses only Read/Glob/Grep tools; no Write or Edit during the scan itself |
| **AN2 — Structured findings table** | Output includes a findings table or checklist (not prose only) with severity/priority per finding |
| **AN3 — No auto-write** | New effects require scope after draft/summary; existing authority continues. Report-only does not authorize repair/index/state |
| **AN4 — No director gates during analysis** | Analysis skills do not spawn director gates; they produce findings for human review |

---

### `team`

**Skills**: team-combat, team-narrative, team-audio, team-level, team-ui, team-qa,
team-release, team-polish, team-live-ops

Team skills orchestrate multiple specialist agents for a department. They must
spawn the right agents, run independent ones in parallel, and surface blocks immediately.

| Metric | PASS criteria |
|---|---|
| **T1 — Named agent list** | Skill explicitly names which agents it spawns and in what order |
| **T2 — Parallel where independent** | Agents whose inputs don't depend on each other are spawned in parallel (single message, multiple Task calls) |
| **T3 — BLOCKED surfacing** | If any spawned agent returns BLOCKED or fails, skill surfaces it immediately and halts dependent work — never silently skips |
| **T4 — Collect all verdicts before proceeding** | Dependent phases wait for all parallel agents to complete before proceeding |
| **T5 — Usage error on no argument** | If required argument (e.g., feature name) is missing, skill outputs usage hint and stops without spawning agents |

---

### `sprint`

**Skills**: sprint-plan, sprint-status, milestone-review, retrospective, changelog, patch-notes

Sprint skills read production state and produce reports or planning artifacts.
They have a PR-SPRINT or PR-MILESTONE gate at specific mode thresholds.

| Metric | PASS criteria |
|---|---|
| **SP1 — Reads sprint/milestone state** | Skill reads `production/sprints/` or `production/milestones/` before producing output |
| **SP2 — Correct sprint gate** | PR-SPRINT (for planning) or PR-MILESTONE (for milestone review) gate runs in `full` mode, skips in `lean`/`solo` |
| **SP3 — Structured output** | Output uses a consistent structure (velocity table, risk list, action items) rather than free prose |
| **SP4 — No auto-commit** | Sprint/milestone writes and transitions have relevant scoped authority; report writing alone does not complete/advance state |

---

### `utility`

**Skills**: start, help, brainstorm, onboard, adopt, hotfix, prototype, localize,
launch-checklist, release-checklist, smoke-check, soak-test, test-setup, test-helpers,
regression-suite, qa-plan, bug-triage, bug-report, playtest-report, asset-spec,
reverse-document, project-stage-detect, setup-engine, skill-test, skill-improve,
day-one-patch, and any other skills not in categories above

Utility skills pass the current structural/parity check set declared by `/skill-test`. If they happen to spawn director
gates, the gate mode logic must also be correct.

| Metric | PASS criteria |
|---|---|
| **U1 — Passes current static checks** | `/skill-test static [name]` returns COMPLIANT with 0 FAILs |
| **U2 — Gate mode correct (if applicable)** | If the skill spawns any director gate, it reads review-mode and applies full/lean/solo logic correctly |

---

## Agent Categories

Used to validate canonical agent specs in `skill_testing/specs/agents/`.

### `director`

**Agents**: creative-director, technical-director, art-director, producer

| Metric | PASS criteria |
|---|---|
| **D1 — Correct verdict vocabulary** | Returns APPROVE / CONCERNS / REJECT (or domain equivalent: REALISTIC/CONCERNS/UNREALISTIC for producer) |
| **D2 — Domain boundary respected** | Does not make binding decisions outside its declared domain |
| **D3 — Conflict escalation** | When two departments conflict, escalates to correct parent (creative-director or technical-director) rather than unilaterally deciding |
| **D4 — Opus model tier** | Agent is assigned Opus model per coordination-rules.md |

### `lead`

**Agents**: lead-programmer, qa-lead, narrative-director, audio-director, game-designer,
systems-designer, level-designer

| Metric | PASS criteria |
|---|---|
| **L1 — Domain verdict** | Returns a domain-specific verdict (e.g., FEASIBLE/INFEASIBLE for lead-programmer, PASS/FAIL for qa-lead) |
| **L2 — Escalates to shared parent** | Out-of-domain conflicts escalate to creative-director (design) or technical-director (tech) |
| **L3 — Sonnet model tier** | Agent is assigned Sonnet model (default) per coordination-rules.md |

### `specialist`

**Agents**: gameplay-programmer, ai-programmer, technical-artist, sound-designer,
engine-programmer, tools-programmer, network-programmer, security-engineer,
accessibility-specialist, ux-designer, ui-programmer, performance-analyst, prototyper,
qa-tester, writer, world-builder

| Metric | PASS criteria |
|---|---|
| **S1 — Stays in domain** | Explicitly scopes itself to its declared domain; defers out-of-domain requests |
| **S2 — No binding cross-domain decisions** | Does not unilaterally decide matters owned by another specialist |
| **S3 — Defers correctly** | Out-of-domain requests are redirected to the correct agent, not refused silently |

### `engine`

**Agents**: godot-specialist, godot-gdscript-specialist, godot-csharp-specialist,
godot-shader-specialist, godot-gdextension-specialist, unity-specialist, unity-ui-specialist,
unity-shader-specialist, unity-dots-specialist, unity-addressables-specialist,
unreal-specialist, ue-blueprint-specialist, ue-gas-specialist, ue-umg-specialist,
ue-replication-specialist

| Metric | PASS criteria |
|---|---|
| **E1 — Version-aware** | References engine version from `docs/engine-reference/` before suggesting API calls; flags post-cutoff risk |
| **E2 — File routing** | Routes file types to the correct sub-specialist (e.g., `.gdshader` → godot-shader-specialist, not godot-gdscript-specialist) |
| **E3 — Engine-specific patterns** | Enforces engine-specific idioms (e.g., GDScript static typing, C# attribute exports, Blueprint function libraries) |

### `qa`

**Agents**: qa-tester, qa-lead, security-engineer, accessibility-specialist

| Metric | PASS criteria |
|---|---|
| **Q1 — Produces artifacts not code** | Primary output is test cases, bug reports, or coverage gaps — not implementation code |
| **Q2 — Evidence format** | Test cases follow the project's test evidence format (unit/integration/visual/UI per coding-standards.md) |
| **Q3 — No scope creep** | Does not propose new features; flags gaps for humans to decide |

### `operations`

**Agents**: devops-engineer, release-manager, live-ops-designer, community-manager,
analytics-engineer, economy-designer, localization-lead

| Metric | PASS criteria |
|---|---|
| **O1 — Domain ownership clear** | Agent description clearly states what it owns (pipeline, releases, economy, etc.) |
| **O2 — Defers implementation** | Does not write game logic or engine code; delegates to appropriate specialist |
| **O3 — Toolset matches role** | `allowed-tools` in frontmatter matches the operational (not coding) nature of the role |
