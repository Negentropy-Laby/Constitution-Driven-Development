# Agent Coordination Rules

1. **Vertical Delegation**: Leadership agents delegate to department leads, who
   delegate to specialists. Never skip a tier for complex decisions.
2. **Horizontal Consultation**: Agents at the same tier may consult each other
   but must not make binding decisions outside their domain.
3. **Conflict Resolution**: When two agents disagree, escalate to the shared
   parent. If no shared parent, escalate to `creative-director` for design
   conflicts or `technical-director` for technical conflicts.
4. **Change Propagation**: When a design change affects multiple domains, the
   `producer` agent coordinates the propagation.
5. **No Unilateral Cross-Domain Changes**: An agent must never modify files
   outside its designated directories without explicit delegation.

## Scoped Authority Across Roles

Pass original instruction/approval, paths/effects, limits, exact inputs and pending
choices to each role. Execute matching scope without repeated per-role/per-file
questions; delegation never expands authority. Apply the collaboration/evidence/
decision contracts in `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`,
`standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md`.
Report-only excludes inputs/indexes/state; review-only invokes no write entrypoint.
Escalate material new scope/choices and continue unaffected authorized work.

Template evaluation model selection follows [Validation scope and model-based evaluation](evidence-lifecycle.md#validation-scope-and-model-based-evaluation); role assignment and evaluation-model selection are separate.

## Content Comparison and History Retention

Submission review, content migration or replacement, history rewriting and
branch cleanup require a comparison of actual content and necessary context.
Identify each candidate, destination, relevant baselines and assessed scope,
including exclusions. Review the affected content and dependencies; this does
not require re-reviewing the whole repository each time.

### Comparison scope and method

Compare relevant patches, blobs and trees, including file modes, renames and
binary changes. Assess functional semantics, interfaces, data, configuration,
tests, assets and dependencies needed to interpret the result. A Git SHA
identifies an object; ancestry establishes reachability. Neither those facts nor
matching titles alone prove that content is unique, lost or fully replaced.
`patch-id` and `range-diff` assist comparison but do not decide semantic
equivalence or completeness.

Align relevant baselines for rebase, squash, cherry-pick, merge or revision
comparisons, and record one-to-many or many-to-one content mappings when
applicable. Exclude upstream differences only after proving they are unrelated
to the assessed content. Evaluate differences affecting semantics,
compatibility, dependencies or evidence applicability. Assess the currently
effective result, including conflict resolutions and later reverts, rather than
only the original patch or merge point.

### Disposition and evidence

Classify each relevant part of a candidate as:

- **Migrated:** the destination contains the effective content within the
  assessed scope.
- **Superseded or abandoned with evidence:** an evidenced successor correction
  or justified abandonment covers the content; cite the reason, supporting
  evidence and applicable decision authority.
- **Effective but not migrated:** valid content or unfinished work remains
  outside the destination.
- **Unknown:** the available content, context or authority does not support a
  conclusion.

A candidate may contain several dispositions. Unknown content must not be
described as fully replaced. For every candidate, report content correspondence,
unique effective differences, unfinished work, actual evidence uses and recovery
needs, and scope limitations. Keep these findings in the existing owning review,
Story or decision record; no new global history ledger is required.

Matching patches, partial content or final trees do not automatically transfer
tests, independent reviews, approvals or acceptance bound to complete inputs.
Reuse must satisfy the applicable input, environment, scope and authority
requirements. Preserve old reports' original SHA and input bindings. A new
comparison record does not constitute a fresh test run or independent review of
the destination.

### Retention and execution authority

Retain branches or objects according to unique effective changes, unfinished
work, actual current and historical evidence consumers, necessary short-term
rollback and owner requirements. There is no universal duty to retain every old
SHA permanently or archive all history. Specific contracts, Accepted decisions
and explicit retention requirements remain controlling. The instruction to "Keep
local originals and Git history" for **Existing tracked neutral inputs** remains
scoped to that migration; this rule neither expands nor cancels it. Apply
[evidence
preservation](evidence-lifecycle.md#git-objects-and-evidence-preservation) to
required originals and their minimum necessary closure.

A content-replacement conclusion is separate from deletion authority, worktree
occupancy, retention duties and safe execution. This standard grants no
permission to delete, rewrite history, reset, rebase, cherry-pick, force-push or
purge. Resolve those facts under the actual scoped authorization before
dependent operations; unresolved issues block only the operations that depend on
them.

## Model Tier Assignment

> **Claude Code-specific.** The model IDs and `model:` frontmatter below apply to
> Claude Code skill/agent definitions. Codex selects models via its own config and
> ignores this field; treat the tiers as task-complexity guidance only there.

Skills and agents are assigned to model tiers based on task complexity:

| Tier | Model | When to use |
|------|-------|-------------|
| **Haiku** | `claude-haiku-4-5-20251001` | Read-only status checks, formatting, simple lookups — no creative judgment needed |
| **Sonnet** | `claude-sonnet-4-6` | Implementation, design authoring, analysis of individual systems — default for most work |
| **Opus** | `claude-opus-4-6` | Multi-document synthesis, high-stakes phase gate verdicts, cross-system holistic review |

Skills with `model: haiku`: `/help`, `/cdd-status`, `/sprint-status`,
`/story-readiness`, `/scope-check`, `/project-stage-detect`, `/changelog`,
`/patch-notes`, `/onboard`

Skills with `model: opus`: `/review-all-gdds`, `/architecture-review`, `/gate-check`

All other skills default to Sonnet. When creating new skills, assign Haiku if the
skill only reads and formats; assign Opus if it must synthesize 5+ documents with
high-stakes output; otherwise leave unset (Sonnet).

## Subagents vs Agent Teams

> **Claude Code-specific mechanisms.** `Task` spawning and the
> `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` env var are Claude Code features. Codex
> has its own subagent mechanism; the parallel/sequential guidance below applies to
> whichever runtime you use.

This project uses two distinct multi-agent patterns:

### Subagents (current, always active)
Spawned via `Task` within a single Claude Code session. Used by all `team-*` skills
and orchestration skills. Subagents share the session's permission context, run
sequentially or in parallel within the session, and return results to the parent.

**When to spawn in parallel**: If two subagents' inputs are independent (neither
needs the other's output to begin), spawn both Task calls simultaneously rather
than waiting. Example: `/review-all-gdds` Phase 1 (consistency) and Phase 2
(design theory) are independent — spawn both at the same time.

### Agent Teams (experimental — opt-in)
Multiple independent Claude Code *sessions* running simultaneously, coordinated
via a shared task list. Each session has its own context window and token budget.
Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` environment variable.

**Use agent teams when**:
- Work spans multiple subsystems that will not touch the same files
- Each workstream would take >30 minutes and benefits from true parallelism
- A senior agent (technical-director, producer) needs to coordinate 3+ specialist
  sessions working on different epics simultaneously

**Do not use agent teams when**:
- One session's output is required as input for another (use sequential subagents)
- The task fits in a single session's context (use subagents instead)
- Cost is a concern — each team member burns tokens independently

**Current status**: Not yet used in this project. Document usage here when first adopted.

## Parallel Task Protocol

When an orchestration skill spawns multiple independent agents:

1. Issue all independent Task calls before waiting for any result
2. Collect all results before proceeding to dependent phases
3. If any agent is BLOCKED, surface it immediately — do not silently skip
4. Always produce a partial report if some agents complete and others block
