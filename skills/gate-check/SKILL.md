---
name: gate-check
description: "Use this skill when deciding whether a project may advance to the next development phase and needs an evidence-backed PASS, CONCERNS, or FAIL verdict."
argument-hint: "[target-phase] [--review full|lean|solo]. Game phases: systems-design | technical-setup | pre-production | production | polish | release. Product phases: specification | architecture | pre-implementation | implementation | verification | release"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Write, Task, AskUserQuestion
model: opus
---

## User Guide

- When to use: Validate readiness to advance between development phases. Produces a PASS/CONCERNS/FAIL verdict with specific blockers and required artifacts. Supports both game and general product domains — auto-detects domain from the concept document.
- Inputs: Command arguments: `/gate-check [target-phase] [--review full|lean|solo]. Game phases: systems-design | technical-setup | pre-production | production | polish | release. Product phases: specification | architecture | pre-implementation | implementation | verification | release`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: `memory_bank/t0_core/current_state.md`, `memory_bank/t3_archive/gate_runs/`, `memory_bank/t3_archive/gate_runs/gate-[phase]-[YYYY-MM-DD].md`.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Phase Gate Validation

This skill validates whether the project is ready to advance to the next development
phase. It checks for required artifacts, quality standards, and blockers.

**Distinct from `/project-stage-detect`**: That skill is diagnostic ("where are we?").
This skill is prescriptive ("are we ready to advance?" with a formal verdict).

**Domain detection.** The concept document at `design/cdd/` reveals the domain:
- **游戏专用**: `game-concept.md` exists — game stage names and game-specific checks
- **通用产品**: `product-concept.md` exists — product stage names and product-specific checks

Sections below are marked **[通用场景]** (both domains), **[游戏专用]** (game-domain), or **[通用产品]** (product-domain).

## Production Stages (7)

**[通用场景]** The project progresses through these stages. Stage names vary by domain:

**[游戏专用]** Game stages:
1. **Concept** — Brainstorming, game concept document
2. **Systems Design** — Mapping systems, writing CDDs
3. **Technical Setup** — Engine config, architecture decisions
4. **Pre-Production** — Prototyping, vertical slice validation
5. **Production** — Feature development
6. **Polish** — Performance, playtesting, bug fixing
7. **Release** — Launch prep, certification

**[通用产品]** Product stages:
1. **Concept** — Ideation, product concept document, constitution
2. **Specification** — Mapping modules, writing CDDs
3. **Architecture** — Stack config, architecture decisions
4. **Pre-Implementation** — Prototyping, user validation
5. **Implementation** — Feature development
6. **Verification** — Performance, user testing, bug fixing
7. **Release** — Launch prep, deployment validation

**Gate policy**: governed advisory. The gate must run before normal
advancement; PASS may update `production/stage.txt` after user confirmation,
CONCERNS may update it only with a recorded risk note, and FAIL does not update
it unless the user explicitly overrides with a risk note.

**Required source of truth**: `workflow/workflow-catalog.yaml` is the only
source for normal-progression blockers. A `required: true` catalog step can be a
missing-artifact blocker. Optional steps, later-phase steps, and
`required_when` steps outside the active gate can only appear as CONCERNS or
follow-up actions unless a quality failure directly invalidates the current
phase goal.

**Boundary clarifications**:
- [Game] `design/art/art-bible.md` is a Concept optional artifact, not a
  Technical Setup blocker.
- [Product] `design/ux/interaction-patterns.md` is a Pre-Production
  `required_when` artifact, not an Architecture blocker.
- [Product] `design/ux/surface-profile.md` records N/A decisions for product
  surface artifacts when applicability is ambiguous.
- `/qa-plan` is optional during Production by default; missing QA plans or
  `/team-qa` sign-off become release-readiness concerns unless the project has
  explicitly opted into strict QA.
- [Product] one user-test/workflow validation is required before
  Implementation; three cumulative product validation sessions are required
  before Release during Polish / Verification.

---

## 1. Parse Arguments

**Target phase:** `$ARGUMENTS[0]` (blank = auto-detect current stage, then validate next transition)

Also resolve the review mode (once, store for all gate spawns this run):
1. If `--review [full|lean|solo]` was passed → use that
2. Else read `production/review-mode.txt` → use that value
3. Else → default to `lean`

Note: in `solo` mode, director spawns (CD-PHASE-GATE, TD-PHASE-GATE, PR-PHASE-GATE, AD-PHASE-GATE) are skipped — gate-check becomes artifact-existence checks only. In `lean` mode, all four directors still run (phase gates are the purpose of lean mode).

- **With argument**: `/gate-check production` — validate readiness for that specific phase. Supports both game phase names (systems-design, technical-setup, pre-production, production, polish, release) and product phase names (specification, architecture, pre-implementation, implementation, verification, release). The skill auto-detects the domain from the concept document at `design/cdd/`.
- **No argument**: Auto-detect current stage using the same heuristics as
  `/project-stage-detect`, then **confirm with the user before running**:

  Use `AskUserQuestion`:
  - Prompt: "Detected stage: **[current stage]** ([domain]). Running gate for [Current] → [Next] transition. Is this correct?"
  - Options:
    - `[A] Yes — run this gate`
    - `[B] No — pick a different gate` (if selected, show a second widget listing all gate options appropriate to the detected domain: [游戏专用] Concept → Systems Design, Systems Design → Technical Setup, Technical Setup → Pre-Production, Pre-Production → Production, Production → Polish, Polish → Release. [通用产品] Concept → Specification, Specification → Architecture, Architecture → Pre-Implementation, Pre-Implementation → Implementation, Implementation → Verification, Verification → Release)

  Do not skip this confirmation step when no argument is provided.

---

## 2. Phase Gate Definitions

After resolving the requested transition, read only that transition in [gate definitions](references/gate-definitions.md). Treat its artifacts, checks, blockers, and domain branches as the authoritative requirements for the current gate.

## 3. Run the Gate Check

**Before running artifact checks**, read `docs/consistency-failures.md` if it exists.
Extract entries whose Domain matches the target phase (e.g., if checking
Systems Design → Technical Setup, pull entries in Economy, Combat, or any CDD domain;
if checking Technical Setup → Pre-Production, pull entries in Architecture, Engine).
Carry these as context — recurring conflict patterns in the target domain warrant
increased scrutiny on those specific checks.

Then read `workflow/generated/gate-required-artifacts.md` and select the
section matching the target transition and detected domain. Treat that generated
section as the authoritative Required Artifacts / Required Step Evidence list.

For each item in the target gate:

### Artifact Checks
- Use `Glob` and `Read` to verify files exist and have meaningful content
- Don't just check existence — verify the file has real content (not just a template header)
- For code checks, verify directory structure and file counts

**Systems Design → Technical Setup gate — cross-CDD review check**:
Use `Glob('design/cdd/cross-review-*.md')` to find the `/review-all-gdds` report.
If no file matches, mark the "cross-CDD review report exists" artifact as **FAIL** and
surface it prominently: "No `/review-all-gdds` report found in `design/cdd/`. Run
`/review-all-gdds` before advancing to Technical Setup."
If a file is found, read it and check the verdict line: a FAIL verdict means the
cross-CDD consistency check failed and must be resolved before advancing.

### Quality Checks
- For test checks: Run the test suite via `Bash` if a test runner is configured
- For design review checks: `Read` the CDD and check for the 8 required sections
- For performance checks: `Read` technical-preferences.md and compare against any
  profiling data in `tests/performance/` or recent `/perf-profile` output
- For localization checks: `Grep` for hardcoded strings in `src/`

### Cross-Reference Checks
- Compare `design/cdd/` documents against `src/` implementations
- Check that every system referenced in architecture docs has corresponding code
- Verify sprint plans reference real work items

---

## 4. Collaborative Assessment

For items that can't be automatically verified, **ask the user**:

- "I can't automatically verify that the core loop plays well. Has it been playtested?"
- "No playtest report found. Has informal testing been done?"
- "Performance profiling data isn't available. Would you like to run `/perf-profile`?"

**Never assume PASS for unverifiable items.** Mark them as MANUAL CHECK NEEDED.

---

## 4b. Director Panel Assessment

Before generating the final verdict, spawn all four directors as **parallel subagents** via Task using the parallel gate protocol from `standards/director-gates.md`. Issue all four Task calls simultaneously — do not wait for one before starting the next.

**Spawn in parallel:**

1. **`creative-director`** — gate **CD-PHASE-GATE** (`standards/director-gates.md`)
2. **`technical-director`** — gate **TD-PHASE-GATE** (`standards/director-gates.md`)
3. **`producer`** — gate **PR-PHASE-GATE** (`standards/director-gates.md`)
4. **`art-director`** — gate **AD-PHASE-GATE** (`standards/director-gates.md`)
   **[通用产品]** skip if the project has no visual/UI component — CLI tools and backend services may not benefit from art director review

Pass to each: target phase name, list of artifacts present, and the context fields listed in that gate's definition.

**Collect all four responses, then present the Director Panel summary:**

```
## Director Panel Assessment

Creative Director:  [READY / CONCERNS / NOT READY]
  [feedback]

Technical Director: [READY / CONCERNS / NOT READY]
  [feedback]

Producer:           [READY / CONCERNS / NOT READY]
  [feedback]

Art Director:       [READY / CONCERNS / NOT READY]
  [feedback]
```

**Apply to the verdict:**
- Any director returns NOT READY → verdict is minimum FAIL (user may override with explicit acknowledgement)
- Any director returns CONCERNS → verdict is minimum CONCERNS
- All four READY → eligible for PASS (still subject to artifact and quality checks from Section 3)

---

## 5. Output the Verdict

```
## Gate Check: [Current Phase] → [Target Phase]

**Date**: [date]
**Checked by**: gate-check skill

### Required Artifacts: [X/Y present]
- [x] design/cdd/game-concept.md — exists, 2.4KB
- [ ] docs/architecture/ — MISSING (no ADRs found)
- [x] production/sprints/ — exists, 1 sprint plan

### Quality Checks: [X/Y passing]
- [x] CDD has 8/8 required sections
- [ ] Tests — FAILED (3 failures in tests/unit/)
- [?] Core loop playtested — MANUAL CHECK NEEDED

### Blockers
1. **No Architecture Decision Records** — Run `/architecture-decision` to create one
   covering core system architecture before entering production.
2. **3 test failures** — Fix failing tests in tests/unit/ before advancing.

### Recommendations
- [Priority actions to resolve blockers]
- [Optional improvements that aren't blocking]

### Verdict: [PASS / CONCERNS / FAIL]
- **PASS**: All required artifacts present, all quality checks passing; normal stage update allowed after user confirmation
- **CONCERNS**: Minor gaps exist but can be addressed during the next phase; stage update allowed only with a risk note
- **FAIL**: Critical blockers exist; no stage update unless the user explicitly overrides with a risk note
```

---

## 5a. Chain-of-Verification

After drafting the verdict in Phase 5, challenge it before finalising.

**Step 1 — Generate 5 challenge questions** designed to disprove the verdict:

For a **PASS** draft:
- "Which quality checks did I verify by actually reading a file, vs. inferring they passed?"
- "Are there MANUAL CHECK NEEDED items I marked PASS without user confirmation?"
- "Did I confirm all listed artifacts have real content, not just empty headers?"
- "Could any blocker I dismissed as minor actually prevent the phase from succeeding?"
- "Which single check am I least confident in, and why?"

For a **CONCERNS** draft:
- "Could any listed CONCERN be elevated to a blocker given the project's current state?"
- "Is the concern resolvable within the next phase, or does it compound over time?"
- "Did I soften any FAIL condition into a CONCERN to avoid a harder verdict?"
- "Are there artifacts I didn't check that could reveal additional blockers?"
- "Do all the CONCERNS together create a blocking problem even if each is minor alone?"

For a **FAIL** draft:
- "Have I accurately separated hard blockers from strong recommendations?"
- "Are there any PASS items I was too lenient about?"
- "Am I missing any additional blockers the user should know about?"
- "Can I provide a minimal path to PASS — the specific 3 things that must change?"
- "Is the fail condition resolvable, or does it indicate a deeper design problem?"

**Step 2 — Answer each question** independently.
Do NOT reference the draft verdict text — re-check specific files or ask the user.

**Step 3 — Revise if needed:**
- If any answer reveals a missed blocker → upgrade verdict (PASS→CONCERNS or CONCERNS→FAIL)
- If any answer reveals an over-stated blocker → downgrade only if citing specific evidence
- If answers are consistent → confirm verdict unchanged

**Step 4 — Note the verification** in the final report output:
`Chain-of-Verification: [N] questions checked — verdict [unchanged | revised from X to Y]`

---

## 6. Update Stage Under Governed Advisory Policy

When the verdict is **PASS** and the user confirms they want to advance:

1. Write the new stage name to `production/stage.txt` (single line, no trailing newline)
2. This immediately updates the status line for all future sessions

Example: if passing the "Pre-Production → Production" gate:
```bash
echo -n "Production" > production/stage.txt
```

**Always ask before writing**: "Gate passed. May I update `production/stage.txt` to 'Production'?"

When the verdict is **CONCERNS**:

1. Ask whether the user wants to advance with acknowledged risk.
2. If yes, capture a short risk note in the gate report before updating `production/stage.txt`.
3. If no, leave `production/stage.txt` unchanged and list the smallest remediation path.

When the verdict is **FAIL**:

1. Leave `production/stage.txt` unchanged by default.
2. Ask whether the user wants to override the FAIL verdict.
3. If the user overrides, capture the override decision and risk note in the gate report before updating `production/stage.txt`.
4. If the user does not override, leave `production/stage.txt` unchanged and list the blockers.

### Memory Bank Audit Record

After presenting the verdict, ask:

`May I write this gate result to memory_bank/t3_archive/gate_runs/gate-[phase]-[YYYY-MM-DD].md?`

When `memory_bank/` exists and the user approves, write a T3 audit record under
`memory_bank/t3_archive/gate_runs/`.

- Use `gate-[phase]-[YYYY-MM-DD].md`.
- If that file exists, use `gate-[phase]-[YYYY-MM-DD]-[NN].md`.
- Include gate name, domain, date, verdict, required artifact source,
  missing artifacts, quality concerns, director panel summary,
  Chain-of-Verification result, stage update decision, and any override or risk
  note.
- The required artifact source is
  `workflow/generated/gate-required-artifacts.md`.

When a PASS verdict, acknowledged CONCERNS advance, or explicit FAIL override
updates `production/stage.txt`, also update
`memory_bank/t0_core/current_state.md` when `memory_bank/` exists. The current
state update should record current phase, stage source, latest gate evidence
path, current blocker, next command, and any risk/override note.

If `memory_bank/` does not exist, do not create it from `/gate-check`. Keep the
existing `production/stage.txt` behavior and say: "Run `/constitute` to
establish the memory_bank governance control plane."

---

## 7. Closing Next-Step Widget

After the verdict is presented and any stage.txt update is complete, close with a structured next-step prompt using `AskUserQuestion`.

**Tailor the options to the gate that just ran:**

For **systems-design PASS**:
```
Gate passed. What would you like to do next?
[A] Run /create-architecture — produce your master architecture blueprint and ADR work plan (recommended next step)
[B] Design more CDDs first — return here when all MVP systems are complete
[C] Stop here for this session
```

> **Note for systems-design PASS**: `/create-architecture` is the required next step before writing any ADRs. It produces the master architecture document and a prioritized list of ADRs to write. Running `/architecture-decision` without this step means writing ADRs without a blueprint — skip it at your own risk.

For **technical-setup PASS**:
```
Gate passed. What would you like to do next?
[A] Start Pre-Production — begin prototyping the Vertical Slice
[B] Write more ADRs first — run /architecture-decision [next-system]
[C] Stop here for this session
```

For all other gates, offer the two most logical next steps for that phase plus "Stop here".

---

## 8. Follow-Up Actions

Based on the verdict, suggest specific next steps from the domain-appropriate list:

**[游戏专用]** Game-specific follow-up actions:

- **No art bible?** -> `/art-bible` to create the visual identity specification.
- **Art bible exists but no asset specs?** -> `/asset-spec system:[name]` to generate per-asset visual specs and generation prompts from approved CDDs.
- **No concept document?** -> `/brainstorm` to create one.
- **No module index?** -> `/map-systems` to decompose the concept into systems.
- **Missing design docs?** -> `/reverse-document` or delegate to `game-designer`.
- **Small design change needed?** -> `/quick-design` for changes under about 4 hours.
- **No UX specs?** -> `/ux-design [screen name]` to author specs, or `/team-ui [feature]` for the full pipeline.
- **UX specs not reviewed?** -> `/ux-review [file]` or `/ux-review all` to validate.
- **No accessibility requirements doc?** -> Use `AskUserQuestion` to offer `design/accessibility-requirements.md` from `templates/accessibility-requirements.md`, then ask for the tier before writing.
- **No interaction pattern library?** -> `/ux-design patterns` to initialize it.
- **CDDs not cross-reviewed?** -> `/review-all-gdds` after all MVP CDDs are individually approved.
- **Cross-CDD consistency issues?** -> Fix flagged CDDs, then re-run `/review-all-gdds`.
- **No test framework or example baseline test?** -> `/test-setup` to scaffold the required framework, CI workflow, and example test for your engine. `/test-helpers` is optional after that baseline exists.
- **No QA plan for current sprint?** -> `/qa-plan sprint` before implementation begins.
- **Missing ADRs?** -> `/architecture-decision` for individual decisions.
- **No master architecture doc?** -> `/create-architecture` for the full blueprint.
- **ADRs missing technology compatibility sections?** -> Re-run `/architecture-decision` or manually add Technology Compatibility sections to existing ADRs.
- **Missing control manifest?** -> `/create-control-manifest` after the governing ADRs are Accepted.
- **Missing epics?** -> `/create-epics layer: foundation`, then `/create-epics layer: core`.
- **Missing stories for an epic?** -> `/create-stories [epic-slug]`.
- **Stories not implementation-ready?** -> `/story-readiness` before developers pick them up.
- **Tests failing?** -> Delegate to `lead-programmer` or `qa-tester`.
- **No playtest data?** -> `/playtest-report`.
- **Less than 3 playtest sessions?** -> Run more playtests before advancing, using `/playtest-report` to structure findings.
- **No Difficulty Curve doc?** -> Consider `design/difficulty-curve.md` before polish.
- **No player journey document?** -> Create `design/player-journey.md` using the player journey template.
- **Need a quick sprint check?** -> `/sprint-status`.
- **Performance unknown?** -> `/perf-profile`.
- **Not localized?** -> `/localize`.
- **Ready for release?** -> `/launch-checklist`.

**[通用产品]** Product-specific follow-up actions:

- **No product concept?** -> `/brainstorm` to create one.
- **No constitution?** -> `/constitute` to establish governing principles.
- **No module index?** -> `/map-systems` to decompose the concept into modules.
- **Missing design docs?** -> `/reverse-document src/[module]` to generate specs from existing code.
- **Small design change needed?** -> `/quick-design` for changes under about 4 hours.
- **No UX specs?** -> `/ux-design [screen name]` for UI projects, or `/ux-design interaction-patterns` for API/CLI/SDK surfaces.
- **UX specs not reviewed?** -> `/ux-review [file]` or `/ux-review all` to validate.
- **CDDs not cross-reviewed?** -> `/review-all-gdds` after all MVP CDDs are individually approved.
- **No test framework or example baseline test?** -> `/test-setup` to scaffold the required framework, CI workflow, and example test for your stack. `/test-helpers` is optional after that baseline exists.
- **No QA plan?** -> `/qa-plan sprint` before implementation.
- **Missing ADRs?** -> `/architecture-decision` for individual decisions.
- **No master architecture doc?** -> `/create-architecture` for the full blueprint.
- **ADRs missing technology compatibility sections?** -> Run `/architecture-decision` to add Technology Compatibility sections.
- **Missing control manifest?** -> `/create-control-manifest` after the governing ADRs are Accepted.
- **Missing epics?** -> `/create-epics layer: foundation`, then `/create-epics layer: core`.
- **Missing stories?** -> `/create-stories [epic-slug]`.
- **Tests failing?** -> Delegate to `lead-programmer` or `qa-tester`.
- **No user testing data?** -> Run user testing sessions and document findings in `production/qa/evidence/user-tests/`.
- **Performance unknown?** -> `/perf-profile`.
- **Not localized?** -> `/localize`.
- **Missing product design artifact?** -> API/CLI/SDK products need `design/ux/interaction-patterns.md`; UI-heavy products also need `design/design-system.md`; brand/docs visuals use `design/brand/style-guide.md`.
- **No deployment strategy?** -> Document deployment and rollback plan.
- **Missing database migrations?** -> Run migrations against a fresh instance.
- **Integration contracts undefined?** -> `/architecture-decision [integration-name]`.
- **Ready for release?** -> `/launch-checklist`.

---

## Collaborative Protocol

This skill follows the collaborative design principle:

1. **Scan first**: Check all artifacts and quality gates
2. **Ask about unknowns**: Don't assume PASS for things you can't verify
3. **Present findings**: Show the full checklist with status
4. **User decides**: The verdict guides the stage decision; user override is allowed only when risks are recorded
5. **Get approval**: "May I write this gate check report to production/gate-checks/?"

Do not silently advance on CONCERNS or FAIL. Document the risks, capture an
explicit override when needed, and leave `production/stage.txt` unchanged unless
the governed advisory policy allows the stage update.
