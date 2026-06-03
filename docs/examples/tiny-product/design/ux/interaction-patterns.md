# Interaction Patterns: Tiny Importer

## CLI Error Output

- Blocking errors go to stderr.
- Successful dry-run summary goes to stdout.
- Every row-level error includes row number, field, and reason.

## Confirmation

Dry-run never asks for confirmation because it writes no data.
