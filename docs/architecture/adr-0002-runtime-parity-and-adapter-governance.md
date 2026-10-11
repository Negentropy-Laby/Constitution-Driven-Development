# ADR-0002: Runtime parity and adapter governance

## Status

Accepted — ratified 2026-07-11 for the original decision and closeout scope.
The D7/D8 delivery amendment below is **Accepted** by the user's separate
2026-10-11 decision bound to the exact reviewed draft identified below. Writing,
review, tests and publication alone did not establish that acceptance.

## Date

2026-07-11

## Decision Makers

Maintainers — ratified 2026-07-11.

## Summary

Claude Code and Codex are first-class peers with explicit capability differences.
Canonical path policies, nested instructions, deterministic projections and
mixed-root ownership preserve one authority source. Installed projects keep
complete adapters and neutral inputs. The designated Source keeps template
ownership; general mirrors and maintenance records stay outside Git submission
and publication scope regardless of their local placement.

This is a delivery-facing summary of the existing Accepted decision, without a
new choice or acceptance. The complete pre-separation text remains in Git
revision `2dfbe67e67a01ee70e8da74ab13523c7cd40785a` at this path and as a
separately retained exact original. The historical implementation and closeout
record stays recoverable outside the template delivery.

## ADR Dependencies

| Field | Value |
|-------|-------|
| **Depends On** | ADR-0001 (Accepted), whose canonical/projection core remains valid |
| **Enables** | Implementation of this Accepted governance contract |
| **Blocks** | Changes that require a new, unaccepted decision |
| **Ordering Note** | A substantive change to an Accepted choice needs separate ADR acceptance before its affected implementation |

## Current applicability and amendment scope

D1-D6 and the canonical/projection ownership choices remain Accepted. Normal
installed-file use does not require a maintenance mapping, script, fixture or
reader. Updates require the actual designated external Source, covered authority,
exact candidate scope, retained target customizations and independent review.

The Accepted D7/D8 amendment does not advance a project phase or waive Foundation
ADR requirements. A target's Technical Setup/Architecture gate still requires its
actual qualifying decisions; this Source documentation separation does not create
or qualify a Foundation ADR.

## D7/D8 amendment acceptance

- **Authority:** User decision `Sentinel_05a0a7b6c5c0819181ae4993f6b201c5`,
  response “批准执行” to the explicit acceptance/publication question
  `Sentinel_e82e42dfbfc881919fd277d3a43ceb50`.
- **Scope:** Only the reviewed D7 initialization/evidenced-freshness and D8
  business-hook/maintenance-delivery amendment, with ADR-0001's applicability
  explanation. The canonical-to-projection core and original historical scope
  remain intact; acceptance does not advance a project phase or confer other
  state, release or publication authority.
- **Exact reviewed original:** This ADR's Proposed draft, 21741 UTF-8 bytes,
  SHA-256
  `2cd0f3ac08f3f0dbfa4da3315b3712f8f302659adccae5cd6b05c09c87fc66fd`.
  The complete reviewed original is retained as acceptance evidence; this is
  the pre-acceptance draft identity, not a self-hash of this updated file.
- **Historical predecessor:** The full 2026-07-11 Accepted decision remains in
  Git revision `040b2b75179c5e1a317418f61b2074186d97abc0` at this path.
- **Recorded at (UTC):** 2026-10-11T03:02:04.514716+00:00.
  The delegated decision transcript supplies message identity and response,
  not the original message timestamp; no more precise decision time is inferred.

## Context

Platform discovery, metadata, policy-loading and hook payloads differ. Generated
and hand-owned objects coexist under runtime roots. Governance must express
actual capabilities, canonical ownership and complete comparison scope without
making historical maintenance implementation a prerequisite for ordinary use.

## Decision

### D1 — Runtime support

Claude Code and Codex are both first-class runtimes for root/nested instructions,
skills, agents, and hooks. First-class support does not imply identical native
capabilities; documentation states the differences honestly.

### D2 — Semantic-collapse defense

Canonical runtime enumerations avoid collapse during substitution. The Accepted
post-substitution guard flags a repeated token across a short connector
(`and`/`or`/`,`), only when the token contains a replacement target. Residual forbidden
source literals are also checked. These conditions retain the Accepted defense;
they do not introduce a broader false-positive rule.

### D3 — Mapping topology

The Accepted version-2 mapping declares runtime IDs and non-empty labels,
validated source IDs, explicit per-source targets and exactly one output for each
declared source/target pair. Coverage is asymmetric, not the Cartesian product of
all sources and runtimes. The selector `all` is reserved and is not a source ID;
source selection follows the declared classes. Older mappings need an actionable
upgrade explanation. The mapping remains Source maintenance context outside the
ordinary delivered-project inputs; its Accepted format and topology are unchanged.

Skill packages include their full Markdown input set. The root `SKILL.md` is
the only entrypoint; `references/` provides on-demand supporting materials.
A nested `SKILL.md` is not a valid entry. This retains the Accepted package and
projection boundary.

### D4 — Rules ownership and capability asymmetry

`rules/` is canonical common path-policy content.

- Claude output: `.claude/rules/*.md`, generated and byte-identical.
- Codex output: none under `.codex/rules/`.
- Codex behavior: root guidance instructs the agent to consult canonical `rules/`
  entries whose `paths` frontmatter matches the target before editing.
- Capability statement: Claude has native path-glob loading; Codex receives
  instruction-driven access to the same canonical policy but not equivalent
  automatic file-glob enforcement.

Codex native `.codex/rules/*.rules` files are runtime-specific command-approval
policy and remain outside projection ownership.

### D5 — Nested instruction parity

`src/INSTRUCTIONS.md`, `design/INSTRUCTIONS.md` and `docs/INSTRUCTIONS.md` are
neutral canonical owners of six sibling Claude/Codex instruction files. They are
individually owned; parent directories are never owned or pruned. The Accepted
mapping models each directory as its separate single-file source
(`nested-src`, `nested-design`, `nested-docs`) with two fixed destination files.
The alternative multi-file source/destination-pattern shape remains a future
option requiring separate review; it is not a replacement made by this summary.

### D6 — Mixed runtime-root ownership

`.claude/` and `.codex/` are mixed-ownership roots. Only declared derived
subtrees and individual nested siblings follow their canonical owners:
`.claude/skills/`, `.claude/agents/`, `.claude/hooks/`, `.claude/rules/`,
`.agents/skills/`, `.codex/agents/` and `.codex/hooks/`. Runtime-owned
`.claude/settings.json`, `.claude/statusline.sh`, `.codex/hooks.json` and
`.codex/rules/*.rules` remain independent. Never claim or replace either runtime
root wholesale. D8 retires the specific maintenance hook from template delivery.

### D7 — Memory Bank state ownership

`framework_contract.md` and `adapter_state.yaml` are neutral templates indexed
in `document_map.yaml`. Their earlier initialization-to-fresh choice was
superseded only by the separately Accepted amendment below. The exact historical
choice and implementation record remain recoverable; neither is current evidence.

#### Accepted D7 amendment — initialization and evidenced freshness

Initialization copies `adapter_state.yaml` unchanged with deterministic
`uninitialized` values. It initializes `framework_contract.md` using actual
project/Source bindings, leaving unknown bindings unconfigured. It does not
infer `fresh`, fabricate digests, or claim a check ran. See the current `/constitute` workflow and
`templates/memory-bank/t2_execution/framework_contract.md`.

A fresh/stale determination requires an actual comparison of the current,
applicable owner/source identity, exact delivery allowlist and installed bytes,
including project customization ownership. Record the comparison inputs, result,
time and authority. Writing that record to a state file requires exact approved
state-write scope; conversation or an independently authorized report does not
require state-write authority. A local maintenance
check may supply evidence if actually available and applicable; it is not a
required delivered dependency or the only valid comparison method.

Without that comparison, live freshness is unavailable. Preserve any recorded
state and its historical evidence; do not silently replace it, reuse an old
`fresh` as current evidence, or stamp `stale` merely because maintenance tools
are absent. `/constitute-check` may report the gap and a draft; it updates state
only under exact authority. `/cdd-status` only reads `adapter_state.yaml` and
never owns or recomputes its freshness; its separately authorized roadmap/mirror
writes remain governed by their own scope.

**Acceptance:** Accepted within the exact D7 scope and reviewed original
identified above. This supersedes the original initialization-to-fresh choice;
the original Accepted decision remains recoverable in Git history. Other state
writes and project advancement still require their own governing authority.

### D8 — Hook payload compatibility

The retained business asset hook parses applicable Claude `tool_input.file_path` and Codex
`tool_input.command` patch headers, including multi-file changes, POSIX/Windows
separators and absolute/relative paths. Codex `PostToolUse` uses JSON advisories;
Claude keeps the non-blocking stderr fallback. This compatibility decision remains
valid for that asset hook independently of the historical generated-file maintenance hook.

#### Accepted D8 amendment — business hooks and local maintenance

The delivered business asset hook `validate-assets.sh` remains wired in both
runtime configurations. Retain its applicable asset checks and payload/path
compatibility. Normal business hooks and runtime safety configuration are not
classified as template maintenance merely because they are hooks.

`validate-generated-adapter-change.sh` is a local-only maintenance hook: its
tracking entry and runtime wiring were retired under the Source delivery boundary.
The old generated-file check and historical maintenance CI are not prerequisites
for normal template use and must not be reinstated through this ADR. Other
delivered hooks remain subject to their actual configuration, applicable inputs
and runtime trust requirements.

**Acceptance:** Accepted within the exact D8 scope and reviewed original
identified above. The maintenance-delivery change is separate from the still-valid
payload compatibility of the retained business hook. The original D8 remains in
history; the user's explicit decision, not repair/tests/publication, accepts
this amendment.

### Alternatives considered

Equivalent native capabilities cannot be assumed merely because both runtimes
are first-class. Codex command-approval rules cannot stand in for Claude path-glob
policies. Owning whole runtime roots would destroy independently owned settings.
Blind substitution without a collapse guard can merge distinct runtime tokens.
Building adapters as a consumer prerequisite would remove direct installed use.

## Consequences

Consumers retain complete installed adapters, required neutral inputs and actual
project customizations. Path policies and native command approval keep their
separate capability claims. Offline reading remains usable; live freshness,
execution and project qualification still need their own applicable evidence.

## Rollback / compatibility

Retain full historical originals and accepted evidence. Compare the complete
current owner/input/output scope before any authorized projection or restore;
invalid preflight has no write or prune effect. Other-owner changes block their
affected restore. No business hook is activated, no project state is written and
no project gate is passed by this documentation separation.

## CDD Requirements Addressed

Foundational — no direct CDD requirement. Enables: the governance system that
every CDD workflow (concept, design, architecture, story, release) depends on.
This ADR governs how authority content reaches the agent runtimes; it does not
implement any single game mechanic or product module.

## Related

- Extends: [ADR-0001](adr-0001-generated-runtime-adapters.md). Supersedes in part
  its "Codex secondary" framing and the rules/nested-instruction ownership gap;
  ADR-0001's core canonical→generated decision and its rejection of fully
  tokenized prose remain valid.
