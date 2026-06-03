# Example Session: Product UX Pipeline — API, CLI, and Web Import Review

**Context:** Pre-Implementation phase for a product with three user-facing surfaces: CLI import, API import endpoint, and a lightweight web review screen.

**Starting State:**
- `design/cdd/product-concept.md` — defines the core promise
- `design/cdd/csv-import.md` — CDD requires dry-run before write
- `docs/architecture/architecture.md` — API, CLI, and web adapter boundaries approved
- No `design/ux/interaction-patterns.md`
- No web screen spec

**Session Duration:** ~70 minutes
**Turns:** 12
**Outcome:** Product interaction patterns and web review screen spec created and reviewed

---

## Turn 1: User Starts UX Design

**User:**
> /ux-design interaction-patterns

## Turn 2: Agent Classifies Product Surfaces

**Agent (ux-designer):**
> I found three user-facing surfaces:
> - CLI: `cdd-import csv <path> --dry-run`
> - API: `POST /imports/csv:dry-run`
> - Web: import review screen for non-technical operators
>
> I will create `design/ux/interaction-patterns.md` instead of a UI-heavy design system because the first two surfaces are CLI/API contracts.
>
> Which interaction principle should govern all three surfaces?
> - Option A: "Explain before action" - always show what will happen before writes
> - Option B: "Fast path first" - optimize for repeat imports
> - Option C: "Error-first" - prioritize invalid rows and recovery guidance
>
> I recommend A for MVP because the product promise is confidence before write.

**User:**
> A, but make errors very visible.

---

## Turn 3: Agent Drafts Interaction Patterns

**Agent:**
> Drafting these patterns:
> - Dry-run is the default action
> - Write operations require explicit `--apply`, `apply=true`, or web confirmation
> - Every invalid row gets row number, field, code, and recovery text
> - CLI and API share JSON field names
> - Web screen mirrors CLI summary order
>
> May I write `design/ux/interaction-patterns.md`?

**User:**
> Yes.

**Agent writes:** `design/ux/interaction-patterns.md`

---

## Turn 4: Web Screen Spec

**User:**
> We also need the web review screen.

**Agent:**
> Run `/ux-design import-review-screen` under the same product UX pipeline. I will keep this as a screen spec, not a full `design/design-system.md`, because only one web screen is in MVP.

**User:**
> /ux-design import-review-screen

**Agent:**
> Proposed screen layout:
> - Header: file name, row counts, dry-run status
> - Summary band: valid rows, invalid rows, duplicate keys
> - Error table: row, column, code, message, suggested fix
> - Apply confirmation: disabled until user reviews errors
> - Export JSON link for support/debugging
>
> May I write `design/ux/screens/import-review.md`?

**User:**
> Yes.

**Agent writes:** `design/ux/screens/import-review.md`

---

## Turn 5: UX Review

**User:**
> /ux-review design/ux/

**Agent (via /ux-review):**
> **Review result: NEEDS REVISION**
>
> Blocking issue:
> - Web screen says "Apply" but does not define the confirmation copy. This could allow irreversible import mistakes.
>
> Advisory issue:
> - CLI output should include a short human-readable summary before JSON only when `--output text`.

**User:**
> Confirmation copy should say: "Import 184 rows into Workspace A. This cannot be undone from the CLI."

**Agent writes:** confirmation copy into `design/ux/screens/import-review.md`.

---

## Turn 6: Re-Review

**User:**
> /ux-review design/ux/

**Agent:**
> **Review result: APPROVED WITH ADVISORY**
>
> Blocking issue resolved. Advisory CLI text summary can be handled in story acceptance criteria.

---

## Files Read and Written

**Read:**
- `design/cdd/product-concept.md`
- `design/cdd/csv-import.md`
- `docs/architecture/architecture.md`

**Written:**
- `design/ux/interaction-patterns.md`
- `design/ux/screens/import-review.md`

---

## Gate and Evidence Result

- Product UX gate has interaction coverage for CLI, API, and Web.
- UI-heavy `design/design-system.md` is not required yet because MVP has one web screen and no reusable component system.
- Future evidence target: `production/qa/evidence/user-tests/import-review-screen.md`.

---

## Next Step

Run `/create-epics` and `/create-stories`; story acceptance criteria can now reference the interaction pattern and screen spec.
