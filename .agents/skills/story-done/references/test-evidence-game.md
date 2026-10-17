# Game Test Evidence by Story Type

**[游戏专用]** Game evidence table:
| Story Type | Required Evidence | Gate Level |
|---|---|---|
| **Logic** | Automated unit test in `tests/unit/[system]/` — must exist and pass | BLOCKING |
| **Integration** | Integration test in `tests/integration/[system]/` OR playtest/session log doc | BLOCKING |
| **Visual/Feel** | Screenshot + sign-off in `production/qa/evidence/` | ADVISORY |
| **UI** | Manual walkthrough doc OR interaction test in `production/qa/evidence/` | ADVISORY |
| **Config/Data** | Smoke check pass report in `production/qa/smoke-*.md` | ADVISORY |


## Type-specific exact evidence checks

**For game Logic stories**: first read the story's **Test Evidence** section to extract the
exact required file path. Use `Glob` to check that exact path. If the exact path is not
found, also search `tests/unit/[system]/` broadly (the file may have been placed at a
slightly different location). If no test file is found at either location:
- Flag as **BLOCKING**: "Logic story has no unit test file. Story requires it at
  `[exact-path-from-Test-Evidence-section]`. Create and run the test before marking
  this story Complete."

**For game Integration stories**: read the story's **Test Evidence** section for the exact
required path. Use `Glob` to check that exact path first, then search
`tests/integration/[system]/` broadly, then check `production/session-logs/`,
`production/qa/evidence/playtests/`, and `production/qa/evidence/` for a playtest or session
log record referencing this story.
If none found: flag as **BLOCKING** (same rule as Logic).

**For game Visual/Feel and game UI stories**: glob `production/qa/evidence/` for a file
referencing this story. If none: flag as **ADVISORY** —
"No manual test evidence found. Create `production/qa/evidence/[story-slug]-evidence.md`
using the test-evidence template and obtain sign-off before final closure."

**For game Config/Data stories**: check for any `production/qa/smoke-*.md` file.
If none: flag as **ADVISORY** — "No smoke check report found. Run `/smoke-check`."
