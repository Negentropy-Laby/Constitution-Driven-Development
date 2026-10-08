# Workflow Contract

## Canonical Source

- Workflow catalog: `workflow/workflow-catalog.yaml`
- Gate policy: governed advisory
- Generated phase checklist: `docs/PHASE-CHECKLISTS.md`
- Generated gate artifacts: `workflow/generated/gate-required-artifacts.md`
- Shared authority/evidence: `standards/evidence-lifecycle.md`
- Decision disposition: `standards/notes-adr-sync.md`
- Collaboration: `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`

## Project Activation

- Domain: [Game / Product / Unknown]
- Review mode: [full / lean / solo]
- Strict QA mode: [enabled / disabled / not decided]
- Current workflow catalog checksum: [optional complete SHA-256]

This template does not activate memory. Optional absence uses the existing
Story/report/conversation fallback.

## Authorization and Closure

Record original instruction/approval, authority, paths/effects, exclusions and
pending choices. Matching scope persists across roles/files/sections/retries/
recovery; ask only for material new authority. Separate content/write/independent
review/ADR acceptance/publication/completion.

Review-only invokes no write entrypoint. Report-only writes only its new assigned
report, excluding input/index/state. Use `covered`, `cdd-layer`, `no-adr`,
`documentation-update`, `adr-required` or `conflict` with named requirement owner
and exact evidence. Required ADRs are Accepted before affected implementation,
or have valid scoped exception. Block affected dependencies, continue independent work.

Closure points to required checks/review, exact revisions, relevant acceptance/
transition authority and remaining action/owner/due phase. Document synchronization
or evidence writing alone does not complete a Story or advance a phase.

## Conditional Requirements

| Requirement | Current decision | Source |
|-------------|------------------|--------|
| Product surface profile | [required / N/A / unknown] | `design/ux/surface-profile.md` |
