# ADR-0002: Runtime parity and adapter governance

## Status

Accepted — ratified 2026-07-11. Closeout Phases 3–9 may proceed.

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
intended lifecycle is:

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

### D8 — Hook payload compatibility

The generated-file and asset hooks (`validate-generated-adapter-change.sh`,
`validate-assets.sh`) parse both Claude (`tool_input.file_path`) and Codex
(`tool_input.command` apply_patch headers, possibly multi-file) payloads, handle
POSIX/Windows separators and absolute/relative paths, emit JSON advisories for
Codex `PostToolUse` (plain stdout is ignored), and keep a non-blocking stderr
fallback for Claude. They cover all generated output classes, not just skills.

### Runtime capability matrix

| Capability | Claude Code | Codex |
|---|---|---|
| Root instructions | Generated `CLAUDE.md` | Generated `AGENTS.md` |
| Nested instructions | Generated nested `CLAUDE.md` | Generated nested `AGENTS.md`; loaded along the startup working-directory chain |
| Skills | Generated `.claude/skills/` | Generated `.agents/skills/` |
| Agents | Generated Markdown adapters | Generated TOML adapters with documented metadata loss |
| Hooks | Generated `.claude/hooks/` plus `settings.json` wiring | Generated `.codex/hooks/` plus `hooks.json` wiring and trust review |
| CDD path policies | Native `.claude/rules/` path globs | Canonical `rules/` consulted through guidance; no equivalent path-glob enforcement |
| Native command rules | Claude permission/settings surface | `.codex/rules/*.rules`; runtime-specific and never generator-owned |
| Runtime settings | Hand-authored mixed-root files | Hand-authored mixed-root files |

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
- [~] Final adapter baseline fresh locally (302 ok, 0 stale/missing/extra);
      remote 3-OS CI pending (not yet pushed).

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
- Plan of record: `C:\Users\WSMAN\.claude\plans\giggly-munching-wreath.md`
  (session-local).
