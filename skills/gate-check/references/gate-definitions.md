# Phase Gate Definitions

> Loaded on demand from `gate-check/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

## 2. Phase Gate Definitions

For every gate below, normal-progression required artifacts are generated from
`workflow/workflow-catalog.yaml` into
`workflow/generated/gate-required-artifacts.md`.

Before checking a gate, read the generated file and use the section matching the
active transition and domain. Do not add hand-written required artifact rows in
this skill; hand-authored content belongs under Quality / Risk Checks.

### Gate: Concept → Systems Design / Specification

**[通用场景]** This gate validates readiness to move from concept exploration to structured design.

**[游戏专用] Game: Concept → Systems Design**

**Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Game: Concept -> Systems Design`.

**Quality Checks:**
- [ ] Game concept has been reviewed (`/design-review` verdict not MAJOR REVISION NEEDED)
- [ ] Core loop is described and understood
- [ ] Target audience is identified
- [ ] Core thesis captures what the game IS and is NOT

**[通用产品] Product: Concept → Specification**

**Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Product: Concept -> Specification`.

**Quality Checks:**
- [ ] Product concept has been reviewed (`/design-review` verdict not MAJOR REVISION NEEDED)
- [ ] User journey is described and understood
- [ ] Target audience is identified (primary user persona + JTBD statement)
- [ ] Core thesis captures what the product IS and is NOT

---

### Gate: Systems Design → Technical Setup / Specification → Architecture

**[通用场景]** This gate validates readiness to move from design to architecture. Checks are shared across both game and product domains.

**Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Game: Systems Design -> Technical Setup` or
`Product: Specification -> Architecture`.

**Quality Checks:**
- [ ] All MVP CDDs pass individual design review (8 required sections, no MAJOR REVISION NEEDED verdict)
- [ ] `/review-all-gdds` verdict is not FAIL (cross-CDD consistency and design theory checks pass)
- [ ] All cross-CDD consistency issues flagged by `/review-all-gdds` are resolved or explicitly accepted
- [ ] System dependencies are mapped in the module index and are bidirectionally consistent
- [ ] MVP priority tier is defined
- [ ] No stale CDD references flagged (older CDDs updated to reflect decisions made in later CDDs)

---

### Gate: Technical Setup → Pre-Production / Architecture → Pre-Implementation

**[通用场景]** This gate validates readiness to move from architecture to the build phase. Domain-specific checks apply for game vs product projects.

**[游戏专用] Game: Technical Setup → Pre-Production**

**Catalog Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Game: Technical Setup -> Pre-Production`.

**Quality / Risk Checks:**
- [ ] Architecture decisions cover core systems (rendering, input, state management)
- [ ] Technical preferences have naming conventions and performance budgets set
- [ ] Accessibility tier is defined and documented (even "Basic" is acceptable — undefined is not)
- [ ] Game art bible status is recorded as optional Concept follow-up if `design/art/art-bible.md` is missing
- [ ] All ADRs have an **Engine Compatibility section** with engine version stamped
- [ ] All ADRs have a **CDD Requirements Addressed section** with explicit CDD linkage
- [ ] No ADR references APIs listed in the engine deprecated APIs reference under `docs/engine-reference/[engine]/`
- [ ] All HIGH RISK engine domains (per VERSION.md) have been explicitly addressed
      in the architecture document or flagged as open questions
- [ ] Architecture traceability gaps are recorded as CONCERNS unless they make a
      Foundation ADR impossible to implement safely

**ADR Circular Dependency Check**: For all ADRs in `docs/architecture/`, read each ADR's
"ADR Dependencies" / "Depends On" section. Build a dependency graph (ADR-A → ADR-B means
A depends on B). If any cycle is detected (e.g. A→B→A, or A→B→C→A):
- Flag as **FAIL**: "Circular ADR dependency: [ADR-X] → [ADR-Y] → [ADR-X].
  Neither can reach Accepted while the cycle exists. Remove one 'Depends On' edge to
  break the cycle."

**Engine Validation** (read `docs/engine-reference/[engine]/VERSION.md` first):
- [ ] ADRs that touch post-cutoff engine APIs are flagged with Knowledge Risk: HIGH/MEDIUM
- [ ] `/architecture-review` engine audit shows no deprecated API usage
- [ ] All ADRs agree on the same engine version (no stale version references)

---

**[通用产品] Product: Architecture → Pre-Implementation**

Before checking design artifacts, classify the product surface from
`design/cdd/product-concept.md` and `standards/technical-preferences.md`:
API-only, CLI-only, SDK/library, Web UI, desktop/mobile/admin UI, internal
headless service, or multi-surface product. Apply the conditional artifact rules
below. Do not fail an API-only, CLI-only, SDK/library, or internal headless
product for missing `design/design-system.md`.

**Catalog Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Product: Architecture -> Pre-Implementation`.

**Quality / Risk Checks:**
- [ ] Architecture decisions cover core modules (auth, data access, API framework, logging)
- [ ] Technical preferences have naming conventions and performance budgets set
- [ ] Accessibility tier is defined and documented
- [ ] Product surface profile is recorded in the gate report (API-only, CLI-only, SDK/library, UI-heavy, internal headless, or multi-surface)
- [ ] Product interaction patterns are recorded as a Pre-Production `required_when`
      follow-up for API, CLI, SDK/library, UI, docs-driven, or other consumer surfaces
- [ ] UI-heavy products record `design/design-system.md` as a Pre-Production or
      UX handoff concern, not an Architecture blocker
- [ ] Product style guide remains optional unless public brand, docs imagery,
      screenshots, diagrams, marketing/release visuals, or visual tone are in scope
- [ ] All ADRs have a **Technology Compatibility section** with stack version stamped
- [ ] All ADRs have a **CDD Requirements Addressed section** with explicit CDD linkage
- [ ] No ADR references APIs listed in the stack deprecated APIs reference under `docs/reference/[stack]/`
- [ ] All HIGH RISK stack domains (per VERSION.md) have been explicitly addressed in the architecture document or flagged as open questions
- [ ] Architecture traceability gaps are recorded as CONCERNS unless they make a
      Foundation ADR impossible to implement safely

**ADR Circular Dependency Check**: For all ADRs in `docs/architecture/`, build a dependency graph. If any cycle is detected, flag as **FAIL**.

**Stack Validation** (read `docs/reference/[stack]/VERSION.md` first):
- [ ] ADRs that touch post-cutoff APIs are flagged with Knowledge Risk: HIGH/MEDIUM
- [ ] `/architecture-review` audit shows no deprecated API usage
- [ ] All ADRs agree on the same stack version (no stale version references)

### Gate: Pre-Production → Production / Pre-Implementation → Implementation

**[通用场景]** This gate validates readiness to begin full-scale feature development. Game projects require Vertical Slice validation; product projects require MVP validation.

**[游戏专用] Game: Pre-Production → Production**

**Catalog Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Game: Pre-Production -> Production`.

**Quality / Risk Checks:**
- [ ] **Core loop fun is validated** — playtest data confirms the central mechanic is enjoyable, not just functional. Explicitly check the Vertical Slice playtest report.
- [ ] UX specs cover key screens such as main menu, core gameplay HUD, and pause menu when those surfaces are in the current CDD scope
- [ ] UX specs cover all UI Requirements sections from MVP-tier CDDs
- [ ] Interaction pattern library documents patterns used in key screens
- [ ] Accessibility tier from `design/accessibility-requirements.md` is addressed in all key screen UX specs
- [ ] Game art bible, character visual profiles, and HUD-specific docs are recorded as optional or feature-specific follow-up unless the current CDDs require them
- [ ] Epics cover Foundation and Core layers when those layers are in the current CDD/architecture scope
- [ ] Sprint plan references real story file paths from `production/epics/`
      (not just CDDs — stories must embed CDD req ID + ADR reference)
- [ ] **Vertical Slice is COMPLETE**, not just scoped — the build demonstrates the full core loop end-to-end. At least one complete [start → challenge → resolution] cycle works.
- [ ] Architecture document has no unresolved open questions in Foundation or Core layers
- [ ] All ADRs have Engine Compatibility sections stamped with the engine version
- [ ] All ADRs have ADR Dependencies sections (even if all fields are "None")
- [ ] Manual validation confirms CDDs + architecture + epics are coherent
      (run `/review-all-gdds` and `/architecture-review` if not done recently)
- [ ] **Core fantasy is delivered** — at least one playtester independently described an experience that matches the Player Fantasy section of the core system CDDs (without being prompted).

**Vertical Slice Validation** (FAIL if any item is NO):
- [ ] A human has played through the core loop without developer guidance
- [ ] The game communicates what to do within the first 2 minutes of play
- [ ] No critical "fun blocker" bugs exist in the Vertical Slice build
- [ ] The core mechanic feels good to interact with (this is a subjective check — ask the user)

> **Note**: If any Vertical Slice Validation item is FAIL, the verdict is automatically FAIL
> regardless of other checks. Advancing without a validated Vertical Slice creates high
> rework risk because later features are built on an unproven core loop.

---

**[通用产品] Product: Pre-Implementation → Implementation**

Apply `design/ux/surface-profile.md` when a product surface requirement is
ambiguous or when any product UX artifact is marked N/A. API-only, CLI-only,
SDK/library, and internal headless products are not blocked by missing
`design/design-system.md`; UI-heavy and multi-surface UI products are.

**Catalog Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Product: Pre-Implementation -> Implementation`.

**Quality / Risk Checks:**
- [ ] **Core interaction validated** — user testing data confirms the central workflow solves the user's job, not just functional
- [ ] UX specs cover key product surfaces such as onboarding, core workflow, settings, API consumer journey, CLI flow, SDK integration path, or operator workflow when those surfaces are in scope
- [ ] UX specs cover all product surface requirements from MVP-tier CDDs: API consumer journeys, CLI flows, SDK integration paths, web/UI screens, or internal operator workflows as applicable
- [ ] Interaction pattern library documents patterns used in key screens, commands, endpoint examples, SDK snippets, or workflow handoffs as applicable
- [ ] UI-heavy products have design-system coverage for reusable components and states; API-only, CLI-only, SDK/library, and internal headless products record this as N/A rather than FAIL
- [ ] Product N/A decisions include surface evidence, reason, accepted-by, and date in `design/ux/surface-profile.md`
- [ ] Product brand/style guide is recorded as optional follow-up unless public brand, documentation imagery, screenshots, diagrams, marketing/release visuals, or visual tone are explicitly in scope
- [ ] Accessibility tier is addressed in all key screen UX specs
- [ ] Sprint plan references real story file paths from `production/epics/` (not just CDDs — stories must embed CDD req ID + ADR reference)
- [ ] Epics cover Foundation and Core layers when those layers are in the current CDD/architecture scope
- [ ] **MVP is COMPLETE**, not just scoped — the build demonstrates the full core user journey end-to-end. At least one complete [task → completion → value] cycle works.
- [ ] Architecture document has no unresolved open questions in Foundation or Core layers
- [ ] All ADRs have Technology Compatibility sections stamped with the stack version
- [ ] All ADRs have ADR Dependencies sections (even if all fields are "None")
- [ ] Manual validation confirms CDDs + architecture + epics are coherent (run `/review-all-gdds` and `/architecture-review` if not done recently)
- [ ] **Core promise is delivered** — at least one user independently described an experience that matches the User Promise section of the core module CDDs (without being prompted).

**MVP Validation** (FAIL if any item is NO):
- [ ] A human has completed the core workflow without developer guidance
- [ ] The product communicates what to do within the first 2 minutes of use
- [ ] No critical "workflow blocker" bugs exist in the MVP build
- [ ] The core interaction feels satisfying to use (this is a subjective check — ask the user)

> **Note**: If any MVP Validation item is FAIL, the verdict is automatically FAIL regardless of other checks. Advancing without a validated MVP creates high implementation risk because later features are built on an unproven core workflow and rework grows with each dependent feature.

### Gate: Production → Polish / Implementation → Verification

**[通用场景]** This gate validates readiness to move from active development to quality assurance and polish.

**[游戏专用] Game: Production → Polish**

**Catalog Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Game: Production -> Polish`.

**Quality / Risk Checks:**
- [ ] Tests are passing (run test suite via Bash)
- [ ] No critical/blocker bugs in any bug tracker or known issues
- [ ] Core loop plays as designed (compare to CDD acceptance criteria)
- [ ] Fun hypothesis from Game Concept has been explicitly validated or revised
- [ ] Performance is within budget (check technical-preferences.md targets)
- [ ] Playtest findings have been reviewed and critical fun issues addressed (not just documented)
- [ ] Smoke check, `/qa-plan`, `/team-qa`, and additional playtest sessions are recorded as Production or Polish follow-up unless strict QA is explicitly enabled
- [ ] No "confusion loops" identified — no point in the game where >50% of playtesters got stuck without knowing why
- [ ] Difficulty curve matches the Difficulty Curve design doc (if one exists at `design/difficulty-curve.md`)
- [ ] All implemented screens have corresponding UX specs (no "designed in-code" screens)
- [ ] Interaction pattern library is up-to-date with all patterns used in implementation
- [ ] Accessibility compliance verified against committed tier in `design/accessibility-requirements.md`

---

**[通用产品] Product: Implementation → Verification**

**Catalog Required Artifacts:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Product: Implementation -> Verification`.

**Quality / Risk Checks:**
- [ ] Tests are passing (run test suite via Bash)
- [ ] No critical/blocker bugs in any bug tracker or known issues
- [ ] Core workflow functions as designed (compare to CDD acceptance criteria)
- [ ] Core promise from Product Concept has been explicitly validated or revised
- [ ] Performance is within budget (check technical-preferences.md targets — latency, memory, throughput)
- [ ] User testing findings have been reviewed and critical UX issues addressed
- [ ] Smoke check, `/qa-plan`, `/team-qa`, and cumulative product validation sessions are recorded as Production or Polish follow-up unless strict QA is explicitly enabled
- [ ] No "confusion loops" identified — no point where >50% of users got stuck without knowing why
- [ ] All implemented screens have corresponding UX specs (no "designed in-code" screens)
- [ ] Interaction pattern library is up-to-date with all patterns used in implementation
- [ ] Accessibility compliance verified against committed tier in `design/accessibility-requirements.md`
- [ ] No hardcoded configuration values — all environment-specific settings externalized

### Gate: Polish → Release / Verification → Release

**[通用场景]** This gate validates readiness to ship. Final quality, content, and legal checks.

**[游戏专用] Game: Polish → Release**

**Catalog Required Step Evidence:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Game: Polish -> Release`.

**Quality / Risk Checks:**
- [ ] All features from the milestone plan are implemented or explicitly deferred
- [ ] Content is complete (all levels, assets, dialogue referenced in design docs exist) or explicitly deferred
- [ ] Localization strings are externalized (no hardcoded player-facing text in `src/`)
- [ ] All Must Have story test evidence is present (Logic/Integration: test files pass; Visual/Feel/UI: sign-off docs in `production/qa/evidence/`)
- [ ] No test regressions from previous sprint (test suite passes fully)
- [ ] QA plan, `/team-qa` sign-off, smoke check, balance review, store metadata, changelog, and patch notes are recorded as Release-phase follow-up or CONCERNS unless strict QA is explicitly enabled
- [ ] If strict QA is explicitly enabled, missing QA plan, missing QA sign-off, or failing smoke check is a blocker
- [ ] Next Release-phase step is `/release-checklist`, followed by `/launch-checklist` and `/team-release`
- [ ] Performance targets met across all target platforms
- [ ] No known critical, high, or medium-severity bugs
- [ ] Accessibility basics covered (remapping, text scaling if applicable)
- [ ] Localization verified for all target languages
- [ ] Legal requirements met (EULA, privacy policy, age ratings if applicable)
- [ ] Build compiles and packages cleanly

---

**[通用产品] Product: Verification → Release**

**Catalog Required Step Evidence:**
Use `workflow/generated/gate-required-artifacts.md`, section
`Product: Verification -> Release`.

**Quality / Risk Checks:**
- [ ] All features from the milestone plan are implemented or explicitly deferred
- [ ] Content is complete (all integrations, APIs, screens referenced in design docs exist) or explicitly deferred
- [ ] Localization strings are externalized (no hardcoded user-facing text in `src/`)
- [ ] All Must Have story test evidence is present (Logic/Integration: test files pass; Visual/UI: sign-off docs in `production/qa/evidence/`)
- [ ] No test regressions from previous sprint (test suite passes fully)
- [ ] QA plan, `/team-qa` sign-off, smoke check, deployment strategy, changelog, release notes, and rollback plan are recorded as Release-phase follow-up or CONCERNS unless strict QA is explicitly enabled
- [ ] If strict QA is explicitly enabled, missing QA plan, missing QA sign-off, or failing smoke check is a blocker
- [ ] Next Release-phase step is `/release-checklist`, followed by `/launch-checklist` and `/team-release`
- [ ] Performance targets met across all target platforms
- [ ] No known critical, high, or medium-severity bugs
- [ ] Accessibility basics covered (keyboard navigation, text scaling, screen reader support if applicable)
- [ ] Localization verified for all target languages (if applicable)
- [ ] Legal requirements met (privacy policy, terms of service, GDPR if applicable)
- [ ] Build compiles and packages cleanly
- [ ] Database migrations run cleanly against a fresh instance
