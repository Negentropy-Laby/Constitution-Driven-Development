# ADR-0001: Canonical authority sources and generated runtime adapters

## Status

Accepted

- **Date:** 2026-07-10
- **Baseline:** `main` @ `43082d4`

> **Superseded in part by [ADR-0002](adr-0002-runtime-parity-and-adapter-governance.md)**
> (2026-07-11): runtime parity (Codex becomes first-class), manifest-declared
> runtimes/targets, canonicalized rules and nested instructions, the
> semantic-collapse guard, and mixed-runtime-root ownership are extended by
> ADR-0002. This ADR's core canonical→generated decision and its rejection of
> fully tokenized prose remain valid.

## Current delivery applicability

The canonical-to-generated decision remains in force. Installed projects use
the complete delivered platform adapters and their required neutral template and
standard inputs directly, including offline use. They do not rebuild adapters
or require a local CDD maintenance toolkit. Updates use the designated
CDD Source; a target keeps its business documents, configuration and customizations
without becoming a second general CDD Source.

This delivery-facing summary preserves the Accepted choices and introduces no
new decision or acceptance. The complete pre-separation text is available at
[this immutable Git revision](https://github.com/Negentropy-Laby/Constitution-Driven-Development/blob/2dfbe67e67a01ee70e8da74ab13523c7cd40785a/docs/architecture/adr-0001-generated-runtime-adapters.md).
Historical implementation and validation details are outside current template
Git submission/publication. Their local storage location does not determine
compliance.

## Context

Duplicating authority content across independently edited runtime trees creates
structural drift. Runtime discovery and metadata capabilities differ; the
canonical owners and deterministic platform projections make those differences
explicit while keeping installed adapters ready for use.

## Decision

1. The hand-authored canonical owners are `skills/`, `agents/`, `hooks/` and
   `INSTRUCTIONS.md`. Claude-origin wording is projected deterministically for
   Codex; it does not claim runtime-neutral source prose.
2. Platform outputs stay committed and directly usable at their installed paths.
   Derived files are never independently hand-authored after cutover; canonical
   changes and their complete platform projections are reviewed together.
3. The single source/output/transform/ownership mapping uses the Accepted TOML
   contract. Its strict standard-library parser has the Accepted Python 3.11
   baseline and adds no dependency. This Source maintenance mapping is external
   to normal delivered-project inputs; its Accepted choice has not been replaced.
4. Each declared managed destination tree contains exactly its projected file
   set; EXTRA/orphan files fail the comparison. Root instruction files are
   individually owned and their parent is never pruned. Recognition of EXTRA
   does not itself confer deletion authority.
5. Comparison uses exact UTF-8/LF bytes and the Accepted 0644 mode contract,
   rather than newline-normalized text.
6. All outputs are rendered and validated before any mutation. Writes are
   per-file atomic; invalid expected counts or empty source coverage must not
   erase usable adapters. This retains the Accepted complete preflight and
   atomic-write contract.
7. Codex agent metadata intentionally retains only `name`, `description` and
   `developer_instructions`; `tools`, `model`, `maxTurns`, `memory`, `skills`,
   `disallowedTools` and `isolation` have no corresponding agent-schema fields.
   Unknown future frontmatter fields block projection instead of being silently
   discarded. Canonical `agents/*.md` retains the full metadata.

## ADR Dependencies

ADR-0002 extends runtime parity, rules, nested instructions and mixed ownership.
Its separately Accepted D7/D8 amendment governs initialization, evidenced
freshness and the maintenance-delivery boundary. This summary preserves the
original Accepted record and does not ratify a changed choice.

## Alternatives considered

Independent manual copies retain drift risk. Symlinks are unreliable across
Windows and runtime discovery. Building adapters after clone would remove
ready-to-use entries. Fully tokenized runtime-neutral prose remains rejected:
it adds source syntax and substitution complexity while platform capabilities
still differ. A future runtime may justify a separately reviewed decision.

## Consequences

Source authors maintain canonical definitions and deliver their reviewed platform
projections. Consuming projects use the installed entries and required neutral
inputs offline, retain project customizations and exclude general Source mirrors
from consumer Git submission/publication.
Installation alone is not proof of loading, execution or current freshness.

## Rollback / compatibility

Keep usable installed adapters until an applicable read-only comparison succeeds.
Owner inputs never come from their own destination projections. Invalid preflight
performs zero writes and zero pruning. Any authorized restore retains exact
before/after identities, complete output context and unrelated changes; history
remains recoverable. A change to an Accepted choice requires its own ADR acceptance.
## Stack Compatibility

| Field | Value |
|---|---|
| Language / Runtime | Accepted mapping-parser baseline: Python 3.11, as recorded in Decision 3 |
| Framework / Libraries | Standard-library TOML parsing; no added dependency under Decision 3 |
| Surface / Contract | Claude Code and Codex instruction, skill, agent and hook projections; capability differences remain explicit |
| Knowledge Risk | Not Verified for any current CLI release; this record supplies no current version qualification |
| References Consulted | This ADR's Decision 3 and 7; ADR-0002's runtime, rule and mixed-ownership contracts |
| Version-Sensitive APIs / Formats | TOML mapping/agent schemas and runtime frontmatter fields; current native CLI compatibility is Not Verified |
| Verification Required | Applicable native discovery, metadata and hook behavior against the actual runtime version and installed revision |

## CDD Requirements Addressed

Foundational — no direct Game system or Product module CDD requirement was
identified in this historical decision. It governs canonical authority ownership,
complete deterministic projections and directly usable installed adapters for
CDD workflows. A project-specific CDD/TR mapping is Unknown here; this section
does not invent requirement IDs or qualify a project's Foundation ADRs.
