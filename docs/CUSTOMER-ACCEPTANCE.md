# Customer Acceptance Checklist

Use this page to validate that the template is ready for a customer pilot or
delivery review. Run these checks from a clean clone before marking a release as
accepted.

## 1. Repository Setup

```bash
git clone https://github.com/Negentropy-Laby/Constitution-Driven-Development.git
cd Constitution-Driven-Development
python --version
```

Expected result:
- Python 3.11+ is available (required for the adapter generator and consistency checks; `scripts/sync_adapters.py` and `scripts/workflow_consistency.py` use the stdlib `tomllib`).
- The repository opens without missing submodules or generated bootstrap steps.

## 2. Local Validation

```bash
python scripts/skill_lint.py --self-test
python -m unittest discover -s tests -p "*_test.py"
python scripts/skill_lint.py --strict skills
python scripts/sync_adapters.py --check
python scripts/sync_adapters.py --check --state-json
python scripts/runtime_smoke.py --structural
python scripts/workflow_consistency.py
git diff --check
```

Expected result:
- `skill_lint.py --self-test` passes.
- The unittest suite reports `OK` (a few tests skip on Windows; they run on Ubuntu/macOS CI).
- Strict canonical skill lint reports `0 error(s)` for `skills/`.
- `sync_adapters.py --check` reports `0 stale, 0 missing, 0 extra, 0 invalid`.
- State JSON parses as schema version 1 with `status: fresh` and 64-character digests.
- Credential-free runtime structural smoke reports `PASS`.
- Workflow consistency reports `0 error(s), 0 warning(s)`.
- `git diff --check` reports no whitespace errors.

Warnings about placeholder artifact paths are acceptable in strict skill lint
for a template repository, because consuming projects create those artifacts
later.

## 3. CI Validation

Confirm the `Template Consistency` workflow has passed on:
- `ubuntu-latest`
- `macos-latest`
- `windows-latest`

For the release commit being accepted, identify the matching workflow run:

```bash
git rev-parse HEAD
gh run list --workflow "Template Consistency" --branch main --limit 20 --json databaseId,headSha,status,conclusion,workflowName,createdAt
gh run view <run-id> --json jobs,headSha,conclusion
```

Expected result:
- The selected run's `headSha` matches the release commit.
- `consistency (ubuntu-latest)` is `success`.
- `consistency (macos-latest)` is `success`.
- `consistency (windows-latest)` is `success`.
- The final GitHub Release or annotated tag records the release commit SHA,
  workflow run ID, and PASS result for all three platforms.

Before a stable release, manually dispatch `Runtime Contract`. Both
credential-free CLI jobs must pass for the same `headSha`; record the run ID,
Claude/Codex CLI versions, validated help surfaces, and uploaded artifact names
in the GitHub Release or annotated tag. This gate installs the CLIs but makes no
model calls and requires no API keys.

This automated gate does not claim to validate model response quality. A
maintainer may run the New Project Smoke Path below with an existing local
interactive login, but that optional check is not a release blocker and does
not require repository-managed credentials.

## 4. New Project Smoke Path

In a fresh test project, run:

```text
Claude Code: /constitute -> /help -> /cdd-status --dry-run
Codex:      $constitute -> $help -> $cdd-status --dry-run
```

Expected result:
- `/constitute` establishes governing principles.
- `/help` identifies the next required catalog step.
- `/cdd-status --dry-run` produces a roadmap draft without writing files.
- The draft follows the structure shown in `docs/examples/project-roadmap.example.md`.

## 5. Brownfield Smoke Path

In a repository with existing `src/`, `tests/`, `design/`, or
`docs/architecture/` artifacts, run:

```text
/project-stage-detect
/adopt
```

Expected result:
- The current stage is detected from artifacts.
- Missing template-format artifacts are listed as migration work.
- Existing project files are not overwritten without approval.

## 6. Workflow Surface Checks

Review these customer-visible entry points:
- `README.md`
- `docs/START-HERE.md`
- `docs/USER-MANUAL.md`
- `docs/WORKFLOW-GUIDE.md`
- `docs/QUICK-START.md`
- `docs/reference/skills-reference.md`
- `SUPPORT.md`
- `RELEASE_NOTES.md`

Expected result:
- Platform support consistently says Template Consistency CI is configured for
  Ubuntu, macOS, and Windows.
- Runtime documentation distinguishes Claude `/skill` invocation from Codex
  `/skills` browsing and `$skill` explicit invocation.
- README links to the latest stable GitHub Release.
- Skill and template counts match the repository.
- Release order is `/release-checklist` -> `/launch-checklist` ->
  `/team-release`.
- Product surface N/A decisions point to `design/ux/surface-profile.md`.

## 7. Known Limits To Accept Explicitly

- This repository is a template and governance system, not an application build.
- Generated artifact path warnings can appear before a consuming project creates
  project-specific files.
- `/skill-test static all` is a skill workflow, not a CI-enforced command unless
  a project adds automation for it.
- Gate checks are governed advisory. A `FAIL` blocks normal advancement, but the
  user may explicitly override it with a documented risk note.
- Runtime Contract is intentionally manual to keep pinned CLI installation out
  of every PR; it is credential-free and incurs no model inference cost.
