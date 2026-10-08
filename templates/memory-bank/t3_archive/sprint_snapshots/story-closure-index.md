# Story Closure Index

T3 index of approved story closure records. Keep full stories, sprint status,
session state, and retrospective artifacts in their original `production/`
paths.

Use `Story Path` as the current-pointer key. New closure revisions may update the
row with authority while retaining immutable historical links. Story path alone
does not identify approved inputs; decision synchronization does not complete a Story.

| Date | Story Path | Epic / Module | Completion Verdict | Evidence Paths | Review Path | Remaining Risks |
|------|------------|---------------|--------------------|----------------|-------------|-----------------|

## Evidence Record Extensions

Use the project-root owner `standards/evidence-lifecycle.md`, section
"Evidence record metadata", for companion fields and historical pointers.
Keep this template's existing columns and link the owning records.

## Canonical Closure Projection

Completion Verdict is COMPLETE / COMPLETE WITH NOTES / BLOCKED. Both completed
levels require every required AC/check's adequate actual PASS evidence, required
decision/review and relevant completion authority. Advisory actions need owner/due
phase. Legacy COMPLETE WITH RISKS preserves its original historical label and
aliases NOTES only when those same required facts are verified; otherwise project
BLOCKED with actual FAIL/NotRun/Blocked/Pending/Unknown. Risk acceptance is separate.

Story Complete, sprint done, session and this T3 pointer bind the same exact eligible
closure revision/input manifest, not keywords/mutable rows. Each path/effect needs
covered named scope; report-only excludes every projection. Blocked Must Have is
never completed. Preserve existing columns/historical links and disclose pending
or unverified projections without silently repairing them.
