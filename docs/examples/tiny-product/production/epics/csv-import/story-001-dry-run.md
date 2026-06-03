# Story 001: Dry-Run Validation

## Type

CLI

## CDD Trace

- `design/cdd/csv-import.md` Acceptance Criteria 1-3

## ADR Trace

- `docs/architecture/adr-0001-import-contract.md`

## Acceptance Criteria

- [ ] `import --dry-run bad.csv` exits non-zero.
- [ ] stdout contains a valid row count.
- [ ] stderr contains row-level errors.

## Test Evidence

- `production/qa/evidence/smoke/story-001-dry-run.md`
