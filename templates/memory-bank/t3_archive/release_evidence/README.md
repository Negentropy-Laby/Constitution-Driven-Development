# Release Evidence

Store or index release evidence records here after `/team-release` or the
release manager records final proof.

Each release record should include:

- Release version or tag.
- Release commit SHA.
- Actual required project QA/release checks, commands, results and exact scope.
- Workflow run ID/URL and required job results when project CI applies.
- Results for each supported platform/environment required by the release contract.
- Acceptance authority, reviewed revision and any remaining action/owner/due phase.

Preserve historical records, including Ubuntu, macOS and Windows Template
Consistency results where that Source workflow applied. Such history does not
impose CDD Source maintenance CI on a business project or prove its current
release readiness. Missing required project evidence remains incomplete under
`standards/evidence-lifecycle.md`; use owner-justified N/A only for inapplicable
checks.
