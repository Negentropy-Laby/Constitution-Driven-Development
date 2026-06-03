# Example Session: Product Scope Crisis — CLI Import vs. Web Dashboard

**Context:** Two weeks before MVP demo. The CLI import workflow is nearly ready, but a stakeholder asks for a web dashboard. The team must decide whether to add UI scope or protect the validated CLI/API workflow.

**Starting State:**
- `design/cdd/product-concept.md` — MVP promise: safe CSV import with dry-run confidence
- `design/cdd/csv-import.md` — accepted
- `docs/architecture/adr-0001-import-contract.md` — Accepted
- `production/epics/csv-import/` — two of three stories complete
- `production/qa/evidence/user-tests/csv-import-dry-run.md` — 3 internal sessions completed
- No `design/design-system.md`

**Session Duration:** ~25 minutes
**Turns:** 8
**Outcome:** Decision made to defer the dashboard and strengthen CLI/API demo evidence

---

## Turn 1: User Raises the Crisis

**User:**
> A stakeholder wants a web dashboard in the MVP demo. We have two weeks. What should we do?

## Turn 2: Agent Frames the Decision

**Agent (product lead):**
> I read the concept, current CDD, sprint plan, and user-test evidence.
>
> Decision criteria:
> 1. Does it support the core promise?
> 2. Can it be validated before demo?
> 3. Does it introduce unplanned architecture or design-system work?
> 4. Does it risk the existing CLI/API path?
>
> Options:
> - Option A: Add dashboard now.
> - Option B: Defer dashboard; polish CLI/API dry-run evidence.
> - Option C: Build a read-only static mock for demo only.
>
> I recommend B. The dashboard requires `design/design-system.md`, screen specs, new stories, and QA paths. That threatens the already validated workflow.

**User:**
> I am worried the demo feels too technical without UI.

---

## Turn 3: Agent Offers a Narrow Alternative

**Agent:**
> Then choose between B and C:
> - B: strongest delivery confidence, demo is CLI/API plus clear evidence
> - C: read-only mock, no data writes, explicitly labeled "future operator review screen"
>
> C is acceptable only if it does not become a production story and does not change MVP gate criteria.

**User:**
> Use C, but make it clear it is non-production.

---

## Turn 4: Agent Documents the Decision

**Agent:**
> I will write an ADR:
> `docs/architecture/adr-0002-dashboard-deferral.md`
>
> Decision:
> - MVP remains CLI/API dry-run import.
> - Dashboard is deferred.
> - Demo may include a read-only mock under `prototypes/dashboard-demo/`.
> - No `design/design-system.md` is required for MVP gate because no UI-heavy product surface ships.
>
> May I write the ADR?

**User:**
> Yes.

**Agent writes:** `docs/architecture/adr-0002-dashboard-deferral.md`

---

## Turn 5: Scope Check

**User:**
> /scope-check production/epics/csv-import/story-002-apply-transaction.md

**Agent:**
> **Verdict: CLEAR WITH NOTE**
>
> The apply transaction story stays in scope. Dashboard implementation is out of scope and must not be added to the sprint. The mock can live in `prototypes/dashboard-demo/` with a README that says it is throwaway.

---

## Files Read and Written

**Read:**
- `design/cdd/product-concept.md`
- `design/cdd/csv-import.md`
- `production/sprints/sprint-001.md`
- `production/qa/evidence/user-tests/csv-import-dry-run.md`

**Written:**
- `docs/architecture/adr-0002-dashboard-deferral.md`
- `prototypes/dashboard-demo/README.md`

---

## Gate and Evidence Result

- MVP gate remains focused on validated CLI/API workflow.
- UI-heavy `design/design-system.md` remains not required for MVP because no dashboard ships.
- Existing user-test evidence remains valid and should be strengthened before `/gate-check pre-production`.

---

## Next Step

Run `/release-checklist` only after the final apply-transaction story closes and `production/qa/evidence/user-tests/` contains a complete end-to-end validation run.
