# Changelog

All notable template changes should be recorded here.

## Unreleased

No changes recorded after `v0.2.0`.

## [0.2.0] - 2026-07-11

### Cross-Runtime Architecture

- Promoted neutral `skills/`, `agents/`, `hooks/`, `rules/`, and instructions
  to canonical sources with generated first-class Claude Code and Codex adapters.
- Added manifest-v2 runtime targets, nested instruction parity, cross-runtime
  hooks, mixed-root ownership guards, and deterministic adapter freshness.
- Added schema-v1 adapter state JSON with manifest/source digests and wired its
  approved Memory Bank lifecycle through `/constitute`, `/constitute-check`,
  and `/cdd-status`.
- Added credential-free structural smoke to Template Consistency and a manually
  triggered, pinned Claude/Codex live-smoke release gate.
- Documented Claude `/skill` invocation and Codex `/skills`/`$skill` invocation.

### Customer Delivery Hardening

- Enforced full strict lint across all 74 skills.
- Repaired customer-visible Markdown errors in required workflow skills.
- Aligned `UPGRADING.md` with the current workflow catalog and evidence paths.
- Made `/team-release` a required Release phase step after `/release-checklist`
  and `/launch-checklist`.
- Synchronized the documented template count with the actual template tree.
- Added support, security, contribution, changelog, and release-note documents.
- Strengthened workflow consistency checks for phase boundaries, release order,
  evidence paths, art bible phase status, and template counts.
