# Story, Infrastructure and Preferences Audit Checklists

### 2d: Story Format Audit

For each story file found:

- Read actual governing requirements/AC, status and linked decisions, not patterns
  alone. Resolve assigned TR-IDs against the registry without manufacturing IDs.
- Bind manifest raw bytes/full digest/size; absent legacy identity needs current
  LegacyRecheck, not auto-pass from dates or missing fields.
- Apply `standards/notes-adr-sync.md`: Accepted ADR where required, named
  `cdd-layer` or justified `no-adr` where valid. Not every Story needs an ADR.
- Preserve in-progress/done Story content/history. Audit required evidence and
  authority separately; never regenerate or grant completion from format alone.

### 2e: Infrastructure Audit

| Artifact | Path | Impact if missing |
|---|---|---|
| TR registry | `docs/architecture/tr-registry.yaml` | HIGH — no stable requirement IDs |
| Control manifest | `docs/architecture/control-manifest.md` | HIGH — no layer rules for stories |
| Manifest version stamp | In manifest header: `Manifest Version:` | MEDIUM — staleness checks blind |
| Sprint status | `production/sprint-status.yaml` | MEDIUM — `/sprint-status` falls back to markdown |
| Stage file | `production/stage.txt` | MEDIUM — phase auto-detect unreliable |
| **[游戏专用]** Engine reference | `docs/engine-reference/[engine]/VERSION.md` | HIGH — ADR engine checks blind |
| **[通用产品]** Stack reference | `docs/reference/[stack]/VERSION.md` | HIGH — ADR stack checks blind |
| Architecture traceability | `docs/architecture/architecture-traceability.md` | MEDIUM — no persistent matrix |

### 2f: Technical Preferences Audit

Read `standards/technical-preferences.md`. Check each field for `[TO BE CONFIGURED]`:
- **[游戏专用]** Engine, Language, Rendering, Physics → HIGH if unconfigured (ADR skills fail)
- **[通用产品]** Language, Framework, Runtime, Database → HIGH if unconfigured (ADR skills fail)
- Naming conventions → MEDIUM
- Performance budgets → MEDIUM
- Forbidden Patterns, Allowed Libraries → LOW (starts empty by design)
