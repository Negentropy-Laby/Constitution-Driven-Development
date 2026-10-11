# Changelog

All notable template changes should be recorded here.

## Unreleased

### Skill Package References

- Skill packages may ship on-demand reference Markdown under
  `skills/<name>/references/`. Every Markdown file in a package is mirrored to
  the `.claude/skills/` and `.agents/skills/` adapters, the package root
  `SKILL.md` stays the only entrypoint, and `expected_count` continues to count
  the 74 skill packages rather than Markdown files.

### Template Use and Submission Boundaries

- Clarified the Source and consumer Git delivery boundaries independently of
  local file placement, while preserving project-owned configuration and inputs.
- Kept installed adapters and required neutral templates usable without a local
  template-maintenance reader or lock.
- Updated `/adopt`, `/constitute`, `/constitute-check`, `/setup-engine` and
  `/skill-improve`, with matching installed platform copies and safe missing-input
  behavior.
- Kept adapter-state initialization deterministic and `uninitialized`; current
  freshness still requires an applicable comparison and separate write authority.
- Clarified deterministic projection limits, canonical ownership, project-binding
  fallbacks and the prohibition on inventing interfaces or editing derived copies
  independently.

## [0.2.0] - 2026-07-11

### Cross-Runtime Architecture

- Promoted neutral `skills/`, `agents/`, `hooks/`, `rules/`, and instructions
  to canonical sources with generated first-class Claude Code and Codex adapters.
- Added manifest-v2 runtime targets, nested instruction parity, cross-runtime
  hooks, mixed-root ownership guards, and deterministic adapter freshness.
- Added schema-v1 adapter state JSON with manifest/source digests and wired its
  approved Memory Bank lifecycle through `/constitute`, `/constitute-check`,
  and `/cdd-status`.
- Made Codex apply-patch hook header parsing portable across GNU and BSD `sed`.
- Documented Claude `/skill` invocation and Codex `/skills`/`$skill` invocation.

### Historical Compatibility Scope

- Documented credential-free structural and CLI contract coverage for the
  released Claude Code and Codex surfaces.
- Documented package structure and metadata consistency across the 74 released
  skill entries.
- Documented consistency between required workflow steps and published
  checklist/gate views.

These are historical release statements from the
[v0.2.0 release tree](https://github.com/Negentropy-Laby/Constitution-Driven-Development/blob/bac9e4da71c5694825723f9a7790d27b589a6c71/CHANGELOG.md).
They do not qualify later inputs or authenticated, model-backed sessions.

### Customer Delivery Hardening

- Repaired customer-visible Markdown errors in required workflow skills.
- Aligned `UPGRADING.md` with the current workflow catalog and evidence paths.
- Made `/team-release` a required Release phase step after `/release-checklist`
  and `/launch-checklist`.
- Synchronized the documented template count with the actual template tree.
- Added support, security, contribution, changelog, and release-note documents.
