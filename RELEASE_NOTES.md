# Release Notes

## Customer Delivery Ready Candidate

This hardening pass moves the template from technical preview toward a mature
customer delivery baseline.

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

- Template Consistency CI is configured for Ubuntu, macOS, and Windows runners.
- Windows local hook execution requires Git Bash; Windows toast notifications
  are optional and fall back to plain hook output when unavailable.
- Validation status: PASS for commit `b6939c0c26ecf904094833680868a89d7baf669e` in GitHub Actions run
  `26954895153` (`ubuntu-latest`, `macos-latest`, and `windows-latest`).
- Customer acceptance checklist: `docs/CUSTOMER-ACCEPTANCE.md`.
