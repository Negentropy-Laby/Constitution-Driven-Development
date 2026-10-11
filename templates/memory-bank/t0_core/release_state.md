# Release State

## Current Release Readiness

- Release target: [version / milestone / not set]
- Release phase: [not started / candidate / stable / post-release]
- Latest release evidence: `memory_bank/t3_archive/release_evidence/`
- Latest hotfix evidence: `memory_bank/t3_archive/release_evidence/`
- Required release/QA workflow: [actual project-configured workflow and owner / unconfigured]
- Required platforms/environments: [actual release targets / unconfigured]
- Evidence scope/baseline: [exact release revision and governing project requirements]

## Acceptance Evidence

| Evidence | Required | Current status |
|----------|----------|----------------|
| Release commit SHA | Yes | [missing / recorded] |
| Required project QA/release checks | Yes; from actual release requirements | [missing / pass / fail / not run] |
| CI run ID/URL and required job results | When CI is required by this project's release contract | [missing / recorded / owner-justified N/A] |
| Supported platform/environment results | For each actual required release target | [missing / pass / fail / not run] |
| Release acceptance authority and exact scope | Yes; under governing project release rules | [pending / recorded] |

An unconfigured workflow/target leaves affected release readiness unverified.
Keep real production CI, QA and historical evidence. CDD Source maintenance CI
is not a default business-project release requirement; record it only where the
actual release contract requires it.
