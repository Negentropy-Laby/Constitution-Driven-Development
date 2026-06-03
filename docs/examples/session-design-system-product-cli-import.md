# Example Session: Product CDD Authoring — CLI CSV Import Module

**Context:** Solo developer, Systems Design phase for a CLI product that imports CSV files into a normalized local database. `/map-systems` has already produced a product module index.

**Starting State:**
- `design/cdd/product-concept.md` — complete, focused on "safe bulk import with dry-run confidence"
- `design/cdd/module-index.md` — lists `csv-import` as Foundation / MVP
- `.claude/docs/technical-preferences.md` — Python 3.13, Typer CLI, SQLite
- No `design/cdd/csv-import.md` yet

**Session Duration:** ~50 minutes
**Turns:** 10
**Outcome:** Complete product CDD at `design/cdd/csv-import.md`, ready for `/design-review`

---

## Turn 1: User Invokes the Skill

**User:**
> /design-system csv-import

## Turn 2: Agent Loads Context and Presents the Plan

**Agent (product designer, via /design-system):**
> I loaded:
> - `design/cdd/product-concept.md` — primary user job: inspect messy CSV before committing changes
> - `design/cdd/module-index.md` — `csv-import` is Foundation / MVP, upstream: file access, downstream: validation report and persistence
> - `.claude/docs/technical-preferences.md` — Python 3.13, Typer, SQLite
>
> **Technical feasibility pre-check:**
>
> | Domain | Signal |
> |--------|--------|
> | CLI contract | Typer supports typed flags for `--dry-run`, `--schema`, and `--output json` |
> | Data safety | SQLite transaction can rollback entire import |
> | Evidence | pytest can cover parser, validator, and dry-run summary |
>
> We will author the Product CDD sections: User Promise, Detailed Behavior, Contracts/Data Model, Edge Cases, Dependencies, Configuration Knobs, Acceptance Criteria, and Workflow Validation.
>
> May I create `design/cdd/csv-import.md` with those section headings?

**User:**
> Yes.

**Agent writes:** `design/cdd/csv-import.md`

---

## Turn 3: User Promise

**Agent:**
> **Draft User Promise:**
>
> "A user can point the CLI at a CSV, see exactly what would be imported, identify invalid rows, and commit only when the dry-run summary matches expectations."
>
> This makes dry-run the default confidence loop. Should commit require an explicit `--apply` flag?

**User:**
> Yes. No writes unless `--apply` is present.

**Agent:**
> Updating the promise and acceptance criteria to treat write behavior as opt-in. May I write this section?

**User:**
> Yes.

**Agent writes:** User Promise section.

---

## Turn 4: Detailed Behavior and Contracts

**Agent:**
> **Behavior options for invalid rows:**
> - Option A: fail fast on the first invalid row
> - Option B: collect all invalid rows and return a report
> - Option C: import valid rows and quarantine invalid rows
>
> I recommend B for MVP. It supports trust without partial writes.

**User:**
> B. Also output JSON so another tool can read it.

**Agent:**
> I will define:
> - CLI: `cdd-import csv <path> --dry-run --output json`
> - Exit codes: `0` valid, `2` validation failed, `3` file/read error
> - JSON fields: `rows_seen`, `rows_valid`, `rows_invalid`, `errors[]`, `would_write`
>
> May I write Detailed Behavior and Contracts/Data Model?

**User:**
> Yes.

**Agent writes:** Detailed Behavior and Contracts/Data Model sections.

---

## Turn 5: Edge Cases and Dependencies

**Agent:**
> Edge cases I will include:
> - Missing headers
> - Extra unknown columns
> - Empty file
> - Mixed newline formats
> - Duplicate primary keys
> - Invalid encoding
>
> Dependencies:
> - File access module provides readable path checks
> - Validation report module formats user-facing errors
> - Persistence module owns transaction boundaries
>
> Any missing product behavior?

**User:**
> Add `--max-errors` so huge bad files do not flood the terminal.

**Agent writes:** Edge Cases, Dependencies, and Configuration Knobs.

---

## Turn 6: Acceptance Criteria and Workflow Validation

**Agent:**
> **Acceptance criteria draft:**
> 1. Dry-run never writes to SQLite.
> 2. `--apply` wraps all writes in one transaction.
> 3. Invalid rows produce row number, column, code, and message.
> 4. JSON output is stable enough for contract tests.
> 5. `--max-errors` truncates error collection and marks the report as truncated.
>
> **Workflow validation:** run a user-test where a user imports a mixed-validity CSV and decides whether to apply based only on CLI output.
>
> May I write the final sections?

**User:**
> Yes.

**Agent writes:** Acceptance Criteria and Workflow Validation.

---

## Files Read and Written

**Read:**
- `design/cdd/product-concept.md`
- `design/cdd/module-index.md`
- `.claude/docs/technical-preferences.md`

**Written:**
- `design/cdd/csv-import.md`

---

## Gate and Evidence Result

- CDD is ready for `/design-review design/cdd/csv-import.md`.
- No story files are created yet; those come from `/create-epics` and `/create-stories`.
- Workflow evidence target is `production/qa/evidence/user-tests/csv-import-dry-run.md`.

---

## Next Step

Run `/design-review design/cdd/csv-import.md`, then `/review-all-gdds` once all MVP modules are complete.
