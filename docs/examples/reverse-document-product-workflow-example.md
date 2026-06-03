# Product Reverse Documentation Workflow Example

## Scenario

A CLI/API CSV import workflow already works, but the implementation grew before
CDD and architecture artifacts existed. Code lives in `src/cli/importer/`,
`src/api/imports/`, and `migrations/20260603_import_jobs.sql`. The team wants to
reverse-document the product behavior without inventing a separate product-only
command.

## Starting State

- `design/cdd/product-concept.md` exists and names the core promise: "safe import
  before mutation."
- `src/cli/importer/` contains dry-run, apply, and rejected-row export logic.
- `src/api/imports/` contains import job endpoints used by the CLI.
- `migrations/20260603_import_jobs.sql` defines `import_jobs` and
  `import_rejected_rows`.
- Missing: `design/cdd/csv-import.md`, import architecture notes, import ADR,
  and product validation evidence.

## Session Transcript

**User:**

```text
I have a working CSV import workflow in src/cli/importer and src/api/imports.
It works, but we never wrote the CDD or architecture docs. Can you reverse
document it?
```

**Agent via `/reverse-document design src/cli/importer`:**

```text
I found a product workflow, not a gameplay system. I will document observed
behavior first, then ask where intent is ambiguous.

Files read:
- design/cdd/product-concept.md
- src/cli/importer/dry_run.ts
- src/cli/importer/apply.ts
- src/cli/importer/rejected_rows.ts
- src/api/imports/jobs.ts
- migrations/20260603_import_jobs.sql

Observed behavior:
- dry-run validates headers, required columns, duplicate external IDs, and row
  limits before writing any domain records
- apply requires a previous dry-run job ID and refuses stale jobs
- rejected rows can be exported as CSV with row number, field, and reason
- API returns machine-readable error codes that the CLI maps to user-facing text
- import_jobs stores status, counts, source filename, and idempotency key

Questions before I draft the CDD:

1. Is dry-run mandatory for every apply, or only recommended for CLI users?
2. Should rejected rows block the whole import, or can valid rows apply while
   invalid rows are exported?
3. Is the idempotency key scoped to user, workspace, or uploaded file hash?
4. Which promise matters more: speed for large files or explainable rejection
   output?
```

**User:**

```text
Dry-run is mandatory. Rejected rows should block apply for now. Idempotency is
workspace + file hash + normalized options. Explainable rejection output matters
more than speed for MVP.
```

**Agent:**

```text
That clarifies intent. I will draft design/cdd/csv-import.md as a Product CDD.

Draft sections:
1. User Promise
2. Detailed Behavior
3. Contracts / Data Model
4. Edge Cases
5. Dependencies
6. Configuration Knobs
7. Acceptance Criteria
8. Workflow Validation

Key design decisions captured:
- apply requires a successful, non-stale dry-run job
- any rejected row blocks apply in MVP
- idempotency scope is workspace + file hash + normalized options
- error output optimizes explainability over throughput

May I write this to design/cdd/csv-import.md?
```

**User:**

```text
Yes. Also document that partial apply is explicitly out of scope for 0.1.0.
```

**Agent writes `design/cdd/csv-import.md`:**

```text
Status: Reverse Documented
Source: src/cli/importer, src/api/imports, migrations/20260603_import_jobs.sql

User Promise:
Users can understand exactly what will happen before any data is changed.

Acceptance Criteria:
- dry-run creates an import job without mutating domain records
- apply refuses missing, stale, failed, or rejected-row dry-run jobs
- rejected-row export includes source row number, field, code, and message
- repeated apply with the same idempotency key is safe
- partial apply is out of scope for 0.1.0 and must return a clear message
```

**Agent via `/reverse-document architecture src/api/imports`:**

```text
The implementation also contains architecture decisions. I will draft an ADR
instead of burying those decisions in the CDD.

Decision candidates:
- import job is the transaction boundary
- dry-run and apply are separate commands/endpoints
- idempotency key is persisted before mutation
- rejected rows are first-class records, not log-only output

May I draft docs/architecture/adr-0002-import-job-boundary.md?
```

**User:**

```text
Yes. Make import job the transaction boundary.
```

**Agent writes ADR draft:**

```text
ADR-0002: Import Job Boundary
Status: Accepted

Decision:
The import job is the durable transaction boundary for dry-run and apply.

Consequences:
- apply can refuse stale or failed dry-runs without re-reading the source file
- rejected-row export is stable after validation
- future partial apply support must amend this ADR and the CSV Import CDD
```

## Files Read

- `design/cdd/product-concept.md`
- `src/cli/importer/dry_run.ts`
- `src/cli/importer/apply.ts`
- `src/cli/importer/rejected_rows.ts`
- `src/api/imports/jobs.ts`
- `migrations/20260603_import_jobs.sql`

## Files Written

- `design/cdd/csv-import.md`
- `docs/architecture/adr-0002-import-job-boundary.md`

## Gate / Evidence Result

- Systems Design / Specification: CDD is marked `Reverse Documented`, not
  `Approved`; run `/design-review design/cdd/csv-import.md`.
- Technical Setup / Architecture: ADR is `Accepted`, but architecture review
  still needs to verify CDD linkage and migration safety.
- Product validation evidence remains missing until a user-test report is stored
  in `production/qa/evidence/user-tests/`.

## Next Step

1. Run `/design-review design/cdd/csv-import.md`.
2. Run `/architecture-review` after the ADR is added to the architecture set.
3. Create implementation stories under
   `production/epics/csv-import/story-NNN-[slug].md`.
4. Validate the workflow and store evidence in
   `production/qa/evidence/user-tests/validation-001-csv-import.md`.

## Key Observations

- The agent documented observed product behavior before asking about intent.
- Ambiguous implementation choices became explicit CDD or ADR decisions.
- Existing code was not treated as automatically correct; partial apply was
  captured as out of scope for `0.1.0`.
- The same `/reverse-document` command served product code without splitting a
  product-only command.
