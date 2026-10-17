# Extended RTM Formats

## Phase 3b: Display

Extended matrix format:

```
## Requirements Traceability Matrix (RTM)

| TR-ID | CDD | Requirement | ADR | Story | Test File | Test Status |
|-------|-----|-------------|-----|-------|-----------|-------------|
| TR-combat-001 | combat.md | Hitbox < 1 frame | ADR-0003 | story-001-hitbox.md | tests/unit/combat/hitbox_test.gd | LINKED / NOT RUN |
| TR-combat-002 | combat.md | Combo window | — | story-002-combo.md | — | NONE (Visual/Feel) |
| TR-inventory-001 | inventory.md | Persistent storage | ADR-0005 | — | — | NO STORY |
```

## Phase 8: Saved RTM

RTM file format:

```markdown
# Requirements Traceability Matrix (RTM)

> Last Updated: [date]
> Mode: /architecture-review rtm
> Coverage: [N]% full chain verified (CDD → justified disposition → Story → actual evidence)

## How to read this matrix

| Column | Meaning |
|--------|---------|
| TR-ID | Stable requirement ID from tr-registry.yaml |
| CDD | Source design document |
| ADR | Exact governing Accepted scope, or justified CDD/local disposition |
| Story | Story file that implements this requirement |
| Test File | Automated test file path |
| Test Status | LINKED / NOT RUN, actual PASS/FAIL, confirmed MISSING, INCOMPLETE, justified NONE or NO STORY |

## Full Traceability Matrix

| TR-ID | CDD | Requirement | ADR | Story | Test File | Status |
|-------|-----|-------------|-----|-------|-----------|--------|
[Full matrix rows from Phase 3b]

## Coverage Summary

| Status | Count | % |
|--------|-------|---|
| VERIFIED — full chain with actual required evidence | [N] | [%] |
| LINKED / NOT RUN — exact test available, execution not established | [N] | [%] |
| MISSING test — confirmed absent required test original | [N] | [%] |
| INCOMPLETE — required original or discovery unread, inaccessible or unresolved | [N] | [%] |
| NO STORY — ADR exists, not yet implemented | [N] | [%] |
| ADR REQUIRED — significant choice lacks Accepted scope | [N] | [%] |
| **Total requirements** | **[N]** | **100%** |

## Uncovered Requirements (Priority Fix List)

Requirements where the full chain is broken, prioritised by layer:

### Foundation layer gaps
[list with suggested action per gap]

### Core layer gaps
[list]

### Feature / Presentation layer gaps
[list — lower priority]

## History

| Date | Full Chain % | Notes |
|------|-------------|-------|
| [date] | [%] | Initial RTM |
```
