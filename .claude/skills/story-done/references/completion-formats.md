# Story Completion and Handoff Formats

## Phase 6: Completion report

```markdown
## Story Done: [Story Name]
**Story**: [file path]
**Date**: [today]

### Acceptance Criteria: [X/Y passing]
- [x] [Criterion 1] — auto-verified (test passes)
- [x] [Criterion 2] — confirmed
- [ ] [Criterion 3] — FAILS: [reason]
- [?] [Criterion 4] — DEFERRED: requires playtest/user test/deployment session

### Test-Criterion Traceability
| Criterion | Test | Status |
|-----------|------|--------|
| AC-1: [text] | [test file::test name] | COVERED |
| AC-2: [text] | Manual confirmation | COVERED |
| AC-3: [text] | — | UNTESTED |

### Test Evidence
**Story Type**: [Game: Logic | Integration | Visual/Feel | UI | Config/Data] OR [Product: API | CLI | Data/Migration | Auth/Permission | Workflow | UI | Integration | Ops/Deployment | Config] OR [Not declared]
**Required evidence**: [domain-specific required evidence from the game/product table]
**Evidence found**: [YES — `[path]` | NO — BLOCKING | NO — ADVISORY]

### Deviations
[NONE] OR:
- BLOCKING: [description] — [CDD/ADR reference]
- ADVISORY: [description] — user accepted / flagged for tech debt

### Scope
[All changes within stated scope] OR:
- Extra files touched: [list] — [note whether valid or scope creep]

### Verdict: COMPLETE / COMPLETE WITH NOTES / BLOCKED
```

## Phase 8: Next ready stories

```
### Next Up
The following stories are ready to pick up:
1. [Story name] — [1-line description] — Est: [X hrs]
2. [Story name] — [1-line description] — Est: [X hrs]

Run `/story-readiness [path]` to confirm a story is implementation-ready
before starting.
```

## Phase 8: Sprint close-out

```
### Sprint Close-Out Sequence
Every required Must Have closure condition passes.
1. `/smoke-check sprint` — recommended critical-path evidence collection
2. `/team-qa sprint` — optional default orchestration when useful
3. `/gate-check` — assess actual transition, no automatic advancement
```
