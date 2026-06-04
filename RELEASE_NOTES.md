# Release Notes

## Customer Delivery Candidate

This hardening pass moves the template from technical preview toward a mature
customer delivery candidate.

### What Is Included

- Clear Start Here paths for new Game projects, new Product projects, and
  existing project adoption.
- A seven-phase workflow catalog used as the required-step source of truth.
- Governed advisory gates with `PASS`, `CONCERNS`, and `FAIL` outcomes.
- Game and Product branches inside the same command surface.
- Technical Setup baseline covering stack setup, architecture, ADRs,
  architecture review, control manifest, accessibility requirements, and tests.
- Canonical story paths under `production/epics/[epic-slug]/`.
- Canonical QA evidence under `production/qa/evidence/`.
- Full strict lint coverage for all skill files.

### Important Upgrade Notes

- Use `/constitute` as the unified entry command.
- Treat `workflow-catalog.yaml` as the required-step source of truth.
- Keep `/art-bible` as Concept optional for Game projects; it is not a Technical
  Setup blocker.
- Release now follows `/release-checklist` -> `/launch-checklist` ->
  `/team-release`.

### Current Limits

- CI currently verifies Ubuntu.
- Windows Git Bash is manually tested.
- macOS/Linux are designed to work with POSIX-compatible shell tools, but full
  matrix CI is not yet enabled.
