# Release Notes

## v0.2.0 — Runtime-Neutral CDD Governance

This release establishes Claude Code and Codex as first-class runtime peers over
one neutral CDD governance source, with recorded adapter freshness and
credential-free release evidence.

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
- Manifest-v2 canonical-to-runtime adapter generation with root and nested
  instructions, skills, agents, hooks, and path-policy ownership boundaries.
- `sync_adapters.py --check --state-json` with deterministic manifest and
  canonical-source digests.
- Memory Bank adapter-state initialization, approved recording, and read-only
  status display.
- Credential-free structural runtime smoke on every Template Consistency run.
- Manually triggered Runtime Contract for pinned Claude Code 2.1.207 and Codex
  CLI 0.144.1, validating CLI flags and disposable discovery fixtures without
  credentials or model calls.

### Important Upgrade Notes

- Use `/constitute` as the unified entry command.
- Treat `workflow-catalog.yaml` as the required-step source of truth.
- Keep `/art-bible` as Concept optional for Game projects; it is not a Technical
  Setup blocker.
- Release now follows `/release-checklist` -> `/launch-checklist` ->
  `/team-release`.
- Claude Code invokes CDD skills as `/skill-name`; Codex uses `/skills` to
  browse or `$skill-name` for explicit and non-interactive invocation.

### Validation Model

- Template Consistency CI is configured for Ubuntu, macOS, and Windows runners.
- Windows local hook execution requires Git Bash; Windows toast notifications
  are optional and fall back to plain hook output when unavailable.
- Validation status: recorded on the GitHub Release or annotated tag for the
  immutable release commit, not self-referenced from this committed Markdown file.
- Required workflow: `Template Consistency`.
- Required release evidence: release commit SHA, GitHub Actions run ID, and PASS
  result for `ubuntu-latest`, `macos-latest`, and `windows-latest`.
- Required runtime evidence: a manually triggered `Runtime Contract` run for
  the same release commit, successful Claude/Codex jobs, pinned CLI versions,
  validated help surfaces, and uploaded text evidence artifacts.
- Customer acceptance checklist: `docs/CUSTOMER-ACCEPTANCE.md`.
- `v0.1.0` and `v0.1.0-rc.1` remain available as historical release evidence.
