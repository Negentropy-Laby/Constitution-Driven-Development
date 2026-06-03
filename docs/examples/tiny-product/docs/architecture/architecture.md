# Architecture: Tiny Importer

## Modules

- `CsvParser`: streams rows and preserves row numbers.
- `ImportValidator`: validates fields.
- `CliReporter`: owns stdout/stderr formatting.

## Deployment

Packaged as a CLI binary with no server dependency.
