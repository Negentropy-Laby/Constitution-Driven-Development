# CDD: CSV Import

## User Promise

The import command tells the user exactly which rows are invalid before writing data.

## Detailed Behavior

- `import --dry-run file.csv` parses the file and writes no data.
- Invalid rows report row number, field name, and reason.
- Valid rows produce a count summary.

## Contracts / Data Model

Input columns: `email`, `name`, `plan`.

## Edge Cases

- Empty file returns a non-zero exit code and a clear message.
- Unknown columns are warnings, not blockers.

## Acceptance Criteria

- Dry-run writes no records.
- Invalid rows include row number and field reason.
- Exit code is non-zero when blocking errors exist.
