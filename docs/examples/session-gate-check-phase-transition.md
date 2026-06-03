# Example Session: /gate-check Phase Transition — Systems Design → Technical Setup

**Context:** Solo indie dev, end of week 5. The Systems Design phase feels complete — 6 MVP CDDs written and cross-review done. The engine is not configured yet because `/setup-engine` belongs to Technical Setup. User wants to formally advance to Technical Setup.

**Starting State:**
- `production/stage.txt` — currently `systems-design`
- `design/cdd/module-index.md` — 6 MVP systems listed, all marked `Status: CDD Complete`
- `design/cdd/` — 6 CDD files present
- `design/cdd/cross-review-2026-03-10.md` — cross-review report, verdict: CONCERNS (1 low-priority note)
- No configured engine yet; `/setup-engine` is the first required Technical Setup step

**Session Duration:** ~20 minutes
**Turns:** 7
**Outcome:** Gate passed, `stage.txt` updated to `technical-setup`, clear list of what comes next

---

## Turn 1: User Initiates Gate Check

**User:**
> /gate-check

## Turn 2: Agent Detects Current Phase and Runs the Check

**Agent (via /gate-check):**
> Reading `production/stage.txt` — current phase: **systems-design**
>
> Running gate: **Systems Design → Technical Setup**
>
> ---
> **Required Artifacts Checklist:**
>
> | Artifact | Requirement | Status |
> |----------|-------------|--------|
> | `design/cdd/module-index.md` | Exists, all MVP systems listed | ✅ |
> | Per-system CDDs | All MVP systems have a CDD | ✅ (6/6) |
> | `/design-review` per CDD | Each CDD reviewed | ✅ (6/6 review comments found) |
> | Cross-CDD review report | `design/cdd/cross-review-*.md` exists | ✅ |
> | Cross-review verdict | PASS or CONCERNS (not FAIL) | ✅ CONCERNS |
>
> ---
> **Content Scan:**
>
> Checking CDD completeness (8 required sections each)...
>
> | CDD | Missing Sections |
> |-----|-----------------|
> | movement-system.md | None ✅ |
> | stamina-system.md | None ✅ |
> | combat-system.md | None ✅ |
> | inventory-system.md | None ✅ |
> | crafting-system.md | None ✅ |
> | exploration-system.md | None ✅ |
>
> ---
> **Cross-Review Concerns (from `cross-review-2026-03-10.md`):**
>
> 1. ⚠️ LOW — Crafting and inventory both define "item stack size" independently with different defaults (crafting: 99, inventory: 64). One system should be the authority; the other should reference it. Not blocking — can resolve in ADR.
>
> ---
> **Verdict: PASS**
>
> All required artifacts present. Cross-review concern is LOW severity and can be resolved during Technical Setup via an ADR. This is a normal finding at this stage.
>
> **May I advance `production/stage.txt` to `technical-setup`?**

## Turn 3: User Confirms

**User:**
> Yes, advance it.

## Turn 4: Agent Updates Stage and Presents Next Steps

**Agent:**
> Updated `production/stage.txt` → `technical-setup`
>
> ---
> **You are now in: Technical Setup**
>
> This phase establishes the technical foundation before production coding starts. Your goal is a configured engine or stack, a complete and approved architecture, and the required test baseline so that every story written in Pre-Production has clear, unambiguous technical guidance.
>
> **Required steps this phase (in order):**
>
> 1. **`/setup-engine`** — Configure the engine and version, then populate `.claude/docs/technical-preferences.md` and reference docs.
>
> 2. **`/create-architecture`** — Author the master architecture document. Covers system decomposition, data flow, layer boundaries, and module responsibilities.
>
> 3. **`/architecture-decision` (one per significant technical choice)** — At minimum:
>    - Rendering approach (2D camera, viewport, etc.)
>    - Save/load strategy
>    - Audio bus architecture
>    - The "item stack size authority" issue from cross-review (crafting vs inventory)
>
> 4. **`/architecture-review`** — Validates all ADRs for completeness, dependency ordering, and CDD traceability. Produces the TR-registry.
>
> 5. **`/create-control-manifest`** — Converts Accepted ADRs into a flat programmer rules sheet. This is what implementation agents will consult during coding.
>
> 6. **Accessibility requirements** — Create `design/accessibility-requirements.md` from `.claude/docs/templates/accessibility-requirements.md`, choose the project accessibility tier, and record the feature matrix so implementation stories inherit it.
>
> 7. **`/test-setup`** — Create the required baseline: `tests/unit/`, `tests/integration/`, `.github/workflows/tests.yml`, and one example test file. `/test-helpers` is optional later.
>
> 8. **`/gate-check technical-setup`** — Technical Setup → Pre-Production gate. Requires: configured engine/stack, architecture doc, Accepted ADRs, control manifest, accessibility requirements, and the test baseline.
>
> **Optional but recommended:**
> - `/tech-debt` scan if you have any prototype code you plan to carry forward
> - `/test-helpers` after the baseline exists, if fixtures, factories, mocks, or engine helpers would reduce sprint friction
>
> **Tip:** Start with `/setup-engine` so architecture decisions can reference the actual Godot version and API surface. Then create the ADR for the item stack size conflict before writing implementation stories.

## Turn 5: User Asks About the Cross-Review Concern

**User:**
> What do I actually write in the ADR for the stack size conflict?

## Turn 6: Agent Advises

**Agent:**
> The ADR decision is: **which system owns the canonical `max_stack_size` value?**
>
> Two options to consider:
>
> **Option A: Inventory owns it**
> - `ItemData` resource (owned by inventory) gets `max_stack_size: int = 64`
> - Crafting system reads from `ItemData`, never sets its own value
> - Pros: inventory is the source of truth for all item properties
> - Cons: crafting team needs to know to look at inventory data
>
> **Option B: Item data resource owns it (shared resource)**
> - `ItemData.max_stack_size` is the authority for both systems
> - Both crafting and inventory import from `ItemData`
> - Pros: single source, no coupling between crafting and inventory modules
> - Cons: one more thing in the shared data layer
>
> Most studios go with B (shared resource) once they have >2 systems touching item data. But either is valid for a solo project.
>
> After `/setup-engine` pins the engine version, run `/architecture-decision` and it will guide you through the ADR format, including the Dependencies section that links this ADR back to the two CDDs.

## Turn 7: User Wraps Up

**User:**
> Got it. I'll start with /setup-engine, then create the ADR for this.

**Agent:**
> Good starting point. The engine setup will make the architecture work concrete, and the ADR will document the decision, the reasoning, and the CDD requirements it addresses — so when you write code months from now, the rationale is preserved.
>
> Your phase gate is logged. Run `/help` at any time during Technical Setup to see your current progress against the required checklist.

---

## What This Example Demonstrates

- **Gate check is automated, not manual**: agent reads artifacts and checks them — user doesn't fill out a form
- **CONCERNS ≠ FAIL**: the cross-review concern is LOW severity and passes the gate. A FAIL would require resolution before advancing.
- **Stage.txt is the authority**: the status line, `/help`, and all skills read from `production/stage.txt` — updating it here changes what every subsequent skill sees
- **Next steps are phase-specific**: the agent doesn't give a generic "good luck" — it gives the ordered Technical Setup checklist, starting with `/setup-engine`
- **Gate check surfaces carry-forward work**: the stack size conflict was a cross-review note; the gate check ensures it becomes a concrete ADR rather than getting lost
- **One advance per gate**: the user confirmed advancement explicitly. The gate doesn't auto-advance; human confirmation is required.
