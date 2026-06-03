# Example Session: Product Brownfield Adoption — Existing Python CLI

**Context:** Developer has an existing Python CLI that imports CSV files, but no CDD artifacts, no ADRs, and no production tracking.

**Starting State:**
- `src/importer/` — existing Python package with parser and SQLite writer
- `tests/` — a few pytest files, no CDD traceability
- `README.md` — user-facing CLI examples
- No `design/cdd/product-concept.md`
- No `design/cdd/module-index.md`
- No `docs/architecture/`
- No `production/epics/`

**Session Duration:** ~35 minutes
**Turns:** 8
**Outcome:** Adoption plan created and the blocking module index gap fixed without overwriting source code

---

## Turn 1: User Runs Adopt

**User:**
> /adopt

## Turn 2: Agent Audits Current State

**Agent (technical-director, via /adopt):**
> I scanned the project:
>
> | Area | Found | Notes |
> |------|-------|-------|
> | Source | PASS | `src/importer/` has parser, validator, writer |
> | Tests | PARTIAL | pytest exists but does not map to CDD requirement IDs |
> | Concept | MISSING | no `product-concept.md` |
> | Module index | MISSING | no `design/cdd/module-index.md` |
> | Architecture | MISSING | no ADRs or control manifest |
> | Production tracking | MISSING | no epics, stories, or sprints |
>
> **Blocking gap:** module index is missing. Without it, `/design-system retrofit`, `/create-epics`, and `/gate-check systems-design` do not know the module boundaries.

---

## Turn 3: Agent Presents Migration Plan

**Agent:**
> Ordered migration plan:
> 1. Create `design/cdd/product-concept.md` from README and CLI behavior.
> 2. Create `design/cdd/module-index.md` from source modules.
> 3. Retrofit CDDs for `csv-import`, `validation-report`, and `sqlite-writer`.
> 4. Run `/review-all-gdds`.
> 5. Run `/setup-engine` to pin Python/Typer/SQLite versions.
> 6. Create architecture and ADRs.
> 7. Generate epics and stories under `production/epics/`.
>
> May I fix the blocking module index now by inferring modules from `src/importer/`?

**User:**
> Yes.

---

## Turn 4: Agent Writes Module Index

**Agent:**
> Inferred modules:
> - `csv-import` — reads file and maps rows
> - `validation-report` — classifies row-level errors
> - `sqlite-writer` — transaction and persistence ownership
> - `cli-shell` — command flags, output, exit codes
>
> Writing `design/cdd/module-index.md` with MVP priority and dependency order.

**Agent writes:** `design/cdd/module-index.md`

---

## Turn 5: Retrofit Recommendation

**User:**
> What should I do next?

**Agent:**
> Next safest command:
> `/design-system retrofit src/importer/csv_import.py`
>
> It will create or fill `design/cdd/csv-import.md` without overwriting source code. The goal is to capture current behavior first, then decide whether to amend it.

---

## Files Read and Written

**Read:**
- `README.md`
- `src/importer/`
- `tests/`

**Written:**
- `docs/adoption-plan-2026-06-03.md`
- `design/cdd/module-index.md`

---

## Gate and Evidence Result

- Brownfield state is not yet gate-ready.
- Blocking module-index gap is closed.
- Next gate target is Systems Design after product concept and MVP CDDs are retrofitted.
- Existing tests remain untouched and can later be mapped to CDD acceptance criteria.

---

## Next Step

Run `/design-system retrofit src/importer/csv_import.py`, then `/design-review design/cdd/csv-import.md`.
