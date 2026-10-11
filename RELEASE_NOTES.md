# Release Notes

## v0.2.0 — Runtime-Neutral CDD Governance

This release establishes Claude Code and Codex as first-class runtime peers over
one neutral CDD governance source, with explicit adapter ownership and governed evidence.

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
- Manifest-v2 canonical-to-runtime adapter generation with root and nested
  instructions, skills, agents, hooks, and path-policy ownership boundaries.
- Memory Bank adapter-state initialization, approved recording, and read-only
  status display.

### Important Upgrade Notes

- Use `/constitute` as the unified entry command.
- Treat `workflow-catalog.yaml` as the required-step source of truth.
- Keep `/art-bible` as Concept optional for Game projects; it is not a Technical
  Setup blocker.
- Release now follows `/release-checklist` -> `/launch-checklist` ->
  `/team-release`.
- Claude Code invokes CDD skills as `/skill-name`; Codex uses `/skills` to
  browse or `$skill-name` for explicit and non-interactive invocation.

### Acceptance

Use `docs/CUSTOMER-ACCEPTANCE.md` and the project's actual configured tests/QA.
Validate applicable installed inputs, platform behavior and exact execution evidence
within existing authority. Historical runs do not qualify newer or uncommitted inputs.
Unavailable live checks remain NotRun.
