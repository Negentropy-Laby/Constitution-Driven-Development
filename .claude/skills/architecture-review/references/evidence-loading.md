# Mode-Specific Evidence Loading

## Phase 1: Mode inventory

### Phase 1a — L0: Summary Scan (fast, low tokens)

Before reading any full document, use Grep to extract `## Summary` sections
from all CDDs and ADRs:

```
Grep pattern="## Summary" glob="design/cdd/*.md" output_mode="content" -A 4
Grep pattern="## Summary" glob="docs/architecture/adr-*.md" output_mode="content" -A 3
```

For `single-cdd [path]` mode: use the target CDD's summary to identify which
ADRs reference the same system (Grep ADRs for the system name), then full-read
only those ADRs. Skip full-reading unrelated CDDs entirely.

For `engine` mode: only full-read ADRs — CDDs are not needed for engine checks.

For `coverage` or `full` mode: proceed to full-read everything below.

### Phase 1b — L1/L2: Full Document Load

Read all inputs appropriate to the mode:

In no-argument, `full` and `coverage` reviews, read the Design Documents inventory
below. In `rtm` and other modes, read it when the actual review scope includes that
inventory; `engine` and other ADR-only scopes do not require it. If applicability
is undecided, retain Unknown and resolve that scope. A missing required input is
an incomplete check, not a reason to exclude the inventory.

### Design Documents
- All in-scope CDDs in `design/cdd/` — read every file completely
- `design/cdd/module-index.md` — the authoritative list of systems

### Architecture Documents
- All in-scope ADRs in `docs/architecture/` — read every file completely
- `docs/architecture/architecture.md` if it exists

### Technology Reference

**[游戏专用]** Engine reference:
- `docs/engine-reference/[engine]/VERSION.md`
- `docs/engine-reference/[engine]/breaking-changes.md`
- `docs/engine-reference/[engine]/deprecated-apis.md`
- All files in `docs/engine-reference/[engine]/modules/`

**[通用产品]** Stack reference:
- `docs/reference/[stack]/VERSION.md`
- `docs/reference/[stack]/breaking-changes.md`
- `docs/reference/[stack]/deprecated-apis.md`
- All files in `docs/reference/[stack]/modules/`

### Project Standards
- `standards/technical-preferences.md`

Report a count: "Loaded [N] CDDs, [M] ADRs, technology: [name + version]."

**Also read `docs/consistency-failures.md`** if it exists. Extract entries with
Domain matching the systems under review (Architecture, Engine, or any CDD domain
being covered). Surface recurring patterns as a "Known conflict-prone areas" note
at the top of the Phase 4 conflict detection output.

## Phase 3b: Story and test originals

### Step 3b-1 — Load stories

Glob `production/epics/**/*.md` (excluding EPIC.md index files). For each
story file:
- Extract `TR-ID` from the story's Context section
- Extract story file path, title, Status
- Extract `## Test Evidence` section — the stated test file path

### Step 3b-2 — Load test files

Read the actual configured test runner, include/exclude patterns and discovery
roots, including colocated tests outside `tests/` where applicable. Discover tests
using that configuration and build an index: system → [test file paths].

For every exact test path declared in Step 3b-1, Read the original directly even
if discovery or Glob did not return it. Confirm actual absence before recording
MISSING. An unread, inaccessible or unresolved original leaves the affected link
INCOMPLETE; an empty Glob or a runner exclusion alone does not prove absence.
Record whether the actual runner discovers each linked test. File presence or
runner discovery does not prove execution or PASS.
