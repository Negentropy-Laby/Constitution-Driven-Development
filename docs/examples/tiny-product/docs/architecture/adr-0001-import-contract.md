# ADR-0001: Dry-Run Import Contract

## Status

Accepted

## Decision

Dry-run validation must use the same parser and validator as real import, but must not call the writer.

## CDD Requirements Addressed

- `csv-import.md`: dry-run writes no records.
- `csv-import.md`: invalid rows include row number and reason.
