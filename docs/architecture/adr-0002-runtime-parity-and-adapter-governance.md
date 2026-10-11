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

ADR-0001 established canonical sources with generated Claude/Codex adapters but
left Codex "secondary", hardcoded the runtime set, hand-maintained path rules only
in `.claude/rules/`, and used a blind text substitution that silently collapsed
distinct runtime tokens. This ADR makes Claude Code and Codex first-class peers,
declares runtimes and per-source targets in manifest v2, canonicalizes path rules
and nested instructions, reserves Codex's native `.codex/rules/*.rules` namespace,
documents mixed runtime-root ownership, and adds a semantic-collapse guard.

## ADR Dependencies

| Field | Value |
|-------|-------|
| **Depends On** | ADR-0001 (Accepted) — extends its canonical→generated model |
| **Enables** | Closeout pass Phases 3–9 |
| **Blocks** | None |
| **Ordering Note** | Phases 3+ cannot start until this ADR is Accepted |

## Current applicability and amendment scope

The original closeout ordering and validation claims below retain their
2026-07-11 historical scope. They are not current freshness evidence, an active
CI promise, or permission to restore local-only maintenance tools.

D1–D6 and the canonical/projection ownership decision remain Accepted. The
current delivered template contract uses installed platform adapters plus the
required neutral inputs; ordinary offline use does not depend on the local Source
maintenance manifest, scripts or fixtures. Updates use the designated external
Source and retain target customizations.

The accepted D7/D8 amendment addresses the lifecycle and maintenance-delivery
conflict explicitly. It does not advance a project phase or waive its Foundation
ADR requirements. The target project's Technical Setup/Architecture gate still
requires its actual qualifying decisions; this Source template repair neither
creates a third Foundation ADR nor counts a fabricated one.

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

### Problem Statement

ADR-0001's model is sound, but eight gaps remained after cutover:

1. Blind sequential substitution collapsed distinct runtime tokens (e.g.
   `CLAUDE.md and AGENTS.md` → `AGENTS.md and AGENTS.md`, and `.claude/skills/…`
   + `.agents/skills/…` → `.agents/skills/…` twice), and byte-freshness accepted
   the corrupt output as correct.
2. Public documentation still described a Claude-only system.
3. Project-structure documentation did not distinguish canonical, generated, and
   runtime-specific assets.
4. Sixteen path-policy files were hand-maintained only in `.claude/rules/`.
5. Memory Bank did not index the framework/adapter contract or freshness state.
6. The edit-protection hook covered only skills and assumed Claude `file_path`
   payloads.
7. Runtime identifiers were hardcoded in Python.
8. `src/`, `design/`, and `docs/` had nested `CLAUDE.md` guidance with no Codex
   `AGENTS.md` counterparts.

### Current State

Canonical roots (`skills/`, `agents/`, `hooks/`, `INSTRUCTIONS.md`) generate
runtime adapters via `cdd-manifest.toml` + `scripts/sync_adapters.py`. The
substitution layer is a manifest-configured blind `str.replace` table followed by
a `forbidden_literals` sweep. Runtimes are the hardcoded tuple
`VALID_RUNTIMES = ("claude", "codex")`. Path rules live only in the Claude adapter
tree. Codex is described as "secondary" in ADR-0001.

### Constraints

Verified against the official Codex documentation (learn.chatgpt.com/docs/…):

- Codex reserves `.codex/rules/` for native Starlark `*.rules` command-approval
  files; the TUI writes `default.rules` there when a command is allowlisted.
  Generating Markdown into that directory is wrong, and a generator `owns_tree`
  contract would prune a user's rules.
  (agent-configuration/rules)
- Codex `apply_patch` `PostToolUse` provides `tool_input.command` (the patch
  text), not `tool_input.file_path`; a patch may touch multiple files; plain
  stdout is ignored so advisories must be JSON (`hookSpecificOutput`).
  (hooks)
- Codex discovers nested guidance via per-directory `AGENTS.md`, walked
  repository-root → current working directory once at session start. It is not
  dynamic per-target-file glob enforcement.
  (agent-configuration/agents-md)
- The generator preflight is all-or-nothing, but the write phase is only
  per-file atomic — an I/O failure can leave a partially updated adapter set.

## Decision

### D1 — Runtime support

Claude Code and Codex are both first-class runtimes for root/nested instructions,
skills, agents, and hooks. First-class support does not imply identical native
capabilities; documentation states the differences honestly.

### D2 — Semantic-collapse defense

Neutralize the three known canonical enumeration sites and add a built-in
post-substitution guard that flags a token repeated across a short connector
(`and`/`or`/`,`) only when it contains a replacement **target** — the only token
class a collapse can produce (two distinct sources mapping to one output). Keep
`forbidden_literals` for residual source-token checks. This is independent of the
manifest v2 migration and already implemented in Phase 1.

### D3 — Manifest v2

Manifest version 2 declares:

- runtime IDs and non-empty labels (`[runtimes.*]`);
- validated source IDs, except the reserved CLI selector `all`;
- an explicit `targets` list per source (asymmetric);
- exact output coverage for every declared source/target pair.

The topology rule becomes "exactly one output per declared source target," not the
full Cartesian product of every source and every runtime. `VALID_RUNTIMES` and the
fixed `SOURCE_CLASSES` are removed; CLI `--class` choices are derived from the
manifest, with `all` retained as the selector for every declared source and
therefore rejected as a source ID. v1 manifests receive an actionable error
pointing to `UPGRADING.md`.

A `files` multi-file source shape with a `dest_file_pattern` destination form was
considered for scattered sources but was **not implemented** — nested instructions
are modeled as separate single-file sources instead (see D5). It remains a
documented future option if scattered sources proliferate.

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
policy and remain outside generator ownership.

### D5 — Nested instruction parity

The three existing nested guides become neutral canonical sources:
`src/INSTRUCTIONS.md`, `design/INSTRUCTIONS.md`, `docs/INSTRUCTIONS.md`. They
generate six sibling adapters (`src/CLAUDE.md` + `src/AGENTS.md`, etc.). These
scattered files are individually owned; their parent directories are never owned
or pruned.

Implementation note: each directory is modeled as a separate single-file source
(`nested-src`, `nested-design`, `nested-docs`) with two fixed `dest_file` outputs,
rather than one `files` source with a `dest_file_pattern`. This uses the existing
single-file machinery (no generator changes), at the cost of a slightly more
verbose manifest. The `files` source shape and `dest_file_pattern` remain a
documented future option if scattered sources proliferate.

### D6 — Mixed runtime-root ownership

`.claude/` and `.codex/` are mixed-ownership roots. Only manifest-declared
subtrees are generated (`.claude/skills/`, `.claude/agents/`, `.claude/hooks/`,
`.claude/rules/`, `.agents/skills/`, `.codex/agents/`, `.codex/hooks/`, and the
scattered nested-instruction siblings). Hand-authored runtime config such as
`.claude/settings.json`, `.claude/statusline.sh`, `.codex/hooks.json`, and
`.codex/rules/*.rules` is never described as generated and never mapped wholesale
as `.claude/**` / `.codex/**`.

### D7 — Memory Bank state ownership

The templates `framework_contract.md` and `adapter_state.yaml` are added under
`templates/memory-bank/t2_execution/` and indexed in `document_map.yaml`. Their
original intended lifecycle was (historical Accepted scope, not evidence that
initialization performed a comparison):

- `/constitute` initializes them from templates (status: uninitialized → fresh).
- `/constitute-check` recomputes manifest/source digests, runs or consumes
  freshness evidence, reports fresh/stale/uninitialized, and updates state only
  after approval.
- `/cdd-status` may read the state but does not own it.
- `sync_adapters.py --check` remains read-only and never mutates Memory Bank.
- Templates contain deterministic, uninitialized values (not fabricated live
  state).

Implementation status: the templates and `document_map` index are in place; the
`/constitute` + `/constitute-check` lifecycle wiring (skill updates) and the
workflow-consistency memory-bank checks are a follow-up (see milestone notes).

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

The original Accepted implementation used the generated-file and asset hooks
(`validate-generated-adapter-change.sh`,
`validate-assets.sh`) to parse both Claude (`tool_input.file_path`) and Codex
(`tool_input.command` apply_patch headers, possibly multi-file) payloads. They
handled POSIX/Windows separators and absolute/relative paths, emitted JSON
advisories for Codex `PostToolUse` (plain stdout was ignored), and kept a
non-blocking stderr fallback for Claude. That generated-file implementation
covered all generated output classes, not just skills.

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

### Runtime capability matrix

| Capability | Claude Code | Codex |
|---|---|---|
| Root instructions | Generated `CLAUDE.md` | Generated `AGENTS.md` |
| Nested instructions | Generated nested `CLAUDE.md` | Generated nested `AGENTS.md`; loaded along the startup working-directory chain |
| Skills | Generated `.claude/skills/` | Generated `.agents/skills/` |
| Agents | Generated Markdown adapters | Generated TOML adapters with documented metadata loss |
| Delivered business hooks | Delivered `.claude/hooks/` plus actual `settings.json` wiring, including `validate-assets.sh` | Delivered `.codex/hooks/` plus actual `hooks.json` wiring and trust review, including `validate-assets.sh` |
| Local maintenance hook (accepted D8 scope) | Generated-file hook retired from delivery and wiring; historical implementation only | Generated-file hook retired from delivery and wiring; historical implementation only |
| CDD path policies | Native `.claude/rules/` path globs | Canonical `rules/` consulted through guidance; no equivalent path-glob enforcement |
| Native command rules | Claude permission/settings surface | `.codex/rules/*.rules`; runtime-specific and never generator-owned |
| Runtime settings | Hand-authored mixed-root files | Hand-authored mixed-root files |

Skill packages are not limited to a single file: every `*.md` under
`skills/<name>/` is canonical, mirrored to both runtime trees. The package-root
`SKILL.md` is the entrypoint, deeper Markdown (for example
`skills/<name>/references/*.md`) is on-demand material the entrypoint links to,
and a nested `SKILL.md` is rejected by the generator. `expected_count` for the
skills source counts packages, not Markdown files.

## Alternatives Considered

### Alternative 1: Generate Codex rules Markdown to `.codex/rules/`

- **Description:** Emit `.codex/rules/*.md` as a Codex counterpart to
  `.claude/rules/`.
- **Pros:** Symmetric output; no topology relaxation needed.
- **Cons:** Pollutes Codex's native command-approval directory; a generator
  `owns_tree` contract would prune a user's `default.rules`.
- **Rejection Reason:** Data-loss risk and semantic mismatch — Codex `.rules`
  files solve a different problem (command approval) than CDD path policies.

### Alternative 2: Collapse guard via a single `\b`-anchored regex

- **Description:** One broad "doubled token" regex.
- **Pros:** Smallest implementation.
- **Cons:** Misses backtick-wrapped and leading-dot tokens; produced five false
  positives on legitimate same-path prose on first cut.
- **Rejection Reason:** Target-containment is precise (no false negatives — a
  collapse always produces a target token; no realistic false positives —
  canonical prose uses source vocabulary, not target vocabulary).

### Alternative 3: Leave rules Claude-only, undocumented

- **Rejection Reason:** Violates the
  "adapter dirs contain only wrappers/settings/generated copies/pointers"
  principle from ADR-0001.

### Alternative 4: Defer nested-instruction parity

- **Rejection Reason:** Manifest v2 is already in flight this pass, and nested
  parity needs no new schema (three single-file sources reuse existing
  machinery), so the marginal cost is lowest now; a later follow-up would
  re-open migration-doc and output-ownership churn.

### Alternative 5: Fully tokenized source prose (`{{PLACEHOLDERS}}`)

- **Rejection Reason:** Still rejected (per ADR-0001). Neutral wording plus the
  collapse guard covers the failure mode without adding templating syntax to
  every canonical file.

## Consequences

### Positive

- One neutral authority per asset class; genuine Codex parity for instructions,
  skills, agents, and hooks.
- The known duplicate-adjacency collapse class and its tested variants are
  blocked before output is written.
- Documentation matches the actual mixed-ownership, multi-runtime reality.

### Negative

- The generator and manifest schema grow (v2, runtimes, per-source targets).
- Downstream v1 manifests require migration.

### Neutral

- Codex path-policy access is instruction-driven, not path-glob enforced — an
  explicit, documented capability difference, not a defect.

## Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| v1→v2 manifest migration breaks downstream forks | Medium | High | Strict v2 with actionable error pointing to `UPGRADING.md` |
| `owns_tree` prunes untracked custom rules | Low | High | check-before-write `EXTRA` review; `UPGRADING.md` backup step; git cannot recover untracked prunes |
| Codex hook rename requires re-trust/restart | Medium | Low | Document restart + `/hooks` trust review in `UPGRADING.md` |
| Partial adapter set on I/O failure | Low | Medium | Per-file atomic writes; run `--check` after any failure and report all stale/missing/extra |

## Migration Plan

Closeout Phases 3–9, each a separate approval and rollback unit:

1. Manifest v2 foundation (runtimes, targets, dynamic classes) — retains the
   280-output baseline.
2. Canonical `rules/` with Claude-only generated projection — baseline 296.
3. Nested-instruction canonicalization (3 sources → 6 adapters) — baseline 302.
4. Cross-runtime hook compatibility and rename.
5. Docs, standards, contributor, upgrade, and acceptance parity.
6. Memory Bank framework/adapter-state templates, owners, validators, tests.
7. Final local gate + diff review; remote 3-OS CI only after separately authorized
   push.

`UPGRADING.md` holds the downstream v1→v2 procedure: custom-rules backup/merge,
`EXTRA` review before `--write`, generated hook rename, Codex hook re-trust.

**Rollback plan:** Never blanket `git restore`/`reset`/`checkout` mixed-ownership
directories — that would overwrite hand-authored runtime config. Restore each
phase's touched-path inventory as one reviewed inverse patch. A schema rollback
must restore generator + manifest + canonical sources + configs + tests + docs +
newly created outputs together as a single unit. If a dedicated commit is later
authorized, reverting that commit is an additional rollback option.

## Validation Criteria

The entries below record the original closeout baseline and then-configured CI.
They do not assert a current run or active maintenance workflow. In particular,
the 322-output result and three-operating-system CI statement are historical;
current applicability/evidence must be checked separately.

Status legend: `[x]` met · `[~]` partial (see note) · `[ ]` deferred to the follow-up milestone.

- [x] Old P0 source sentences fail generation with `SubstitutionError`; zero
      collapse hits in generated trees.
- [x] Manifest v2 declares runtimes + per-source targets; a v1 manifest yields an
      actionable error.
- [x] `rules/` has 16 canonical files; `.claude/rules/` is byte-identical
      generated; `.codex/rules/` is never generator-owned (proven by a survival
      test, not a non-existence assertion).
- [x] Three nested `INSTRUCTIONS.md` generate six byte-identical sibling adapters.
- [x] Generated-file and asset hooks handle both Claude and Codex payloads for
      every source class, including absolute paths.
- [~] Memory Bank: `document_map.yaml` maps exact generated subtrees and
      `adapter_state.yaml` carries uninitialized template values — MET; the
      `/constitute` + `/constitute-check` lifecycle wiring is deferred.
- [~] Public docs: top-level + structural docs (README, USER-MANUAL, QUICK-START,
      WORKFLOW-GUIDE, setup-requirements, directory-structure, adapters/*) show
      accurate capability differences — MET; Tier 3 reference breadth
      (agent-roster, skills-reference, etc.) is deferred.
- [x] Final adapter baseline fresh locally (322 ok, 0 stale/missing/extra);
      the Template Consistency workflow verifies it on three operating systems per change.

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
- Official Codex docs:
  `learn.chatgpt.com/docs/agent-configuration/rules`,
  `learn.chatgpt.com/docs/hooks`,
  `learn.chatgpt.com/docs/agent-configuration/agents-md`.
