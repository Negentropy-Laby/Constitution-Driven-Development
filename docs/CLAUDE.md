# Docs Directory

When authoring or editing files in this directory, follow these standards.

## Architecture Decision Records (`docs/architecture/`)

Use the ADR template: `templates/architecture-decision-record.md`

**Required sections:** Title, Status, Context, Decision, Consequences,
ADR Dependencies, Engine/Stack Compatibility, CDD Requirements Addressed.

- **Game ADRs** must record engine compatibility, platform/runtime constraints,
  asset or scene implications, performance budget, and CDD/Game Feel impact.
- **Product ADRs** must record language/framework/package compatibility, API/CLI
  contract impact, data/migration impact, deployment/rollback implications,
  observability, security/privacy, and CDD/Product workflow impact.

**Status lifecycle:** `Proposed` → `Accepted` → `Superseded`
- New ADRs start Proposed. Writing, implementation, tests and director approval
  do not accept them. Record separate authority/time, exact retained reviewed original/
  full SHA-256/byte size and scope; preserve predecessors on revision.
- Required Proposed/unevidenced decisions block affected implementation unless a
  valid scoped exception exists. Acceptance does not automatically make Stories Ready.
- Use `/architecture-decision` to create ADRs through the guided flow

**TR Registry:** `docs/architecture/tr-registry.yaml`
- Stable requirement IDs (e.g. `TR-MOV-001`) that link CDD requirements to stories
- Never renumber existing IDs — only append new ones
- Updated by `/architecture-review` Phase 8

**Control Manifest:** `docs/architecture/control-manifest.md`
- Flat programmer rules sheet: Required / Forbidden / Guardrails per layer
- Retain dated `Manifest Version:`/`Last Updated` as readable legacy metadata.
- Consumers bind complete saved raw-byte SHA-256 (64 hex), byte size, original path/
  time outside the manifest itself; no self-referential full-file hash.
- Story/readiness/dev/review/closure compare exact content even on the same date.
  Date-only legacy records need explicit LegacyRecheck of current rules/dependencies;
  never infer old identity from dates or fabricate old digests.

**Validation:** Run `/architecture-review` after completing a set of ADRs.

## Version References

### Game Engine Reference (`docs/engine-reference/`)

Version-pinned engine API snapshots. **Always check here before using any
engine API** — the LLM's training data predates the pinned engine version.

Current engine: see `docs/engine-reference/[engine]/VERSION.md`

### Product Stack Reference (`docs/reference/<stack>/`)

Version-pinned product stack snapshots. **Always check here before using any
framework, language-version-specific API, package, SDK, database, cloud, or
deployment API** that may have changed after the LLM's training data.

Current product stack: see `docs/reference/<stack>/VERSION.md` after
`/setup-engine` has configured the language/framework.

## Decision and evidence ownership

Apply `standards/notes-adr-sync.md` and `standards/evidence-lifecycle.md`: classify
choices under six dispositions with exact Accepted scope or justified CDD/local
ownership. Not every TR needs an ADR. Local classification does not override the
global Technical Setup minimum of three Foundation ADRs. Significant choices resolve
before affected implementation; independent work continues. Report-only authority
covers its new report, not TR/index/session/log/T3 effects.
