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

### Historical Release Context

The v0.2.0 release recorded structural compatibility for Windows, Ubuntu and
macOS, with Claude Code 2.1.207 and Codex CLI 0.144.1 as its historical CLI
baselines. That coverage was credential-free CLI contract/discovery validation;
it did not establish authenticated, model-backed runtime sessions. See the
[immutable v0.2.0 notes](https://github.com/Negentropy-Laby/Constitution-Driven-Development/blob/bac9e4da71c5694825723f9a7790d27b589a6c71/RELEASE_NOTES.md).

The [pre-separation notes](https://github.com/Negentropy-Laby/Constitution-Driven-Development/blob/2dfbe67e67a01ee70e8da74ab13523c7cd40785a/RELEASE_NOTES.md)
also retained `v0.1.0` and `v0.1.0-rc.1` as historical release evidence. Those
older labels are not the current acceptance target. Neither those records nor
the historical CLI versions qualify newer or uncommitted inputs.

### Acceptance

Use `docs/CUSTOMER-ACCEPTANCE.md` and the project's actual configured tests/QA.
Validate applicable installed inputs, platform behavior and exact execution evidence
within existing authority. Historical runs do not qualify newer or uncommitted inputs.
Unavailable live checks remain NotRun.
