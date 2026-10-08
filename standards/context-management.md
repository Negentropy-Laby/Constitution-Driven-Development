# Context Management

Context is the most critical resource in an agent session. Manage it actively.

## File-Backed State (Primary Strategy)

**The file is the memory, not the conversation.** Conversations are ephemeral and
will be compacted or lost. Files on disk persist across compactions and session crashes.

### Session State File

Maintain `production/session-state/active.md` as a living checkpoint when its
write/update effect is authorized. Report-only/review-only work uses its assigned
report or conversation and does not update session state as a side effect.
For authorized implementation, update it after each significant milestone:

- Design section approved and written to file
- Architecture decision made
- Implementation milestone reached
- Test results obtained

The state file should contain: current task, progress checklist, key decisions
made, files being worked on, and open questions.

### Status Line Block (Production/Implementation and later)

For Game Production/Polish/Release or Product Implementation/Verification/Release,
include this block only in an authorized checkpoint. Actual configured status-line
support may parse it; the block does not prove a qualified stage:

```markdown
<!-- STATUS -->
Epic: Combat System
Feature: Melee Combat
Task: Implement hitbox detection
<!-- /STATUS -->
```

- All three fields (Epic, Feature, Task) are optional — include only what applies
- Update this block when switching focus areas
- The status line displays it as a breadcrumb: `Combat System > Melee Combat > Hitboxes`
- Remove or empty the block when no active work focus exists

After any disruption (compaction, crash, `/clear`), read the state file first.

### Incremental File Writing

When creating multi-section documents (design docs, architecture docs, lore entries):

1. Include skeleton and checkpoint paths/effects in approved scope
2. Draft with existing choices and discuss material unresolved decisions
3. Write incremental sections within scope, honoring explicit per-section preferences
4. Update session state only when that effect is authorized
5. After writing a section, previous discussion about that section can be safely
   compacted — the decisions are in the file

This keeps the context window holding only the *current* section's discussion
(~3-5k tokens) instead of the entire document's conversation history (~30-50k tokens).

## Proactive Compaction

> Command names below (`/clear`, `/compact`) are Claude Code commands; Codex has
> its own compaction flow. Actual runtime support/wiring determines hook firing;
> generated scripts alone prove neither. The discipline applies to both domains.

- **Compact proactively** at ~60-70% context usage, not reactively at the limit
- **Use `/clear`** between unrelated tasks, or after 2+ failed correction attempts
- **Natural compaction points:** after writing a section to file, after committing,
  after completing a task, before starting a new topic
- **Focused compaction:** `/compact Focus on [current task] — sections 1-3 are
  written to file, working on section 4`

## Context Budgets by Task Type

- Light (read/review): ~3k tokens startup
- Medium (implement feature): ~8k tokens
- Heavy (multi-system refactor): ~15k tokens

## Subagent Delegation

> Subagent spawning (`Task` in Claude Code) is runtime-specific; both Claude Code
> and Codex support subagents. The guidance below applies to whichever runtime
> you use.

Use subagents for research and exploration to keep the main session clean.
Subagents run in their own context window and return only summaries:

- **Use subagents** when investigating across multiple files, exploring unfamiliar code,
  or doing research that would consume >5k tokens of file reads
- **Use direct reads** when you know exactly which 1-2 files to check
- History inheritance is runtime-specific. Supply exact inputs, scope, exclusions
  and pending decisions explicitly instead of assuming inheritance.

## Compaction Instructions

When context is compacted, preserve the following in the summary:

- Reference to `production/session-state/active.md` (read it to recover state)
- List of files modified in this session and their purpose
- Original authorization reference, paths/effects, exclusions and pending authorities
- Exact input revisions and preserved originals for relied-on evidence
- Decision disposition and acceptance authority
- Active sprint tasks and their current status
- Agent invocations and their outcomes (success/failure/blocked)
- Test results (pass/fail counts, specific failures)
- Unresolved blockers or questions awaiting user input
- The current task and what step we are on
- Which sections of the current document are written to file vs. still in progress

**After compaction:** Read `production/session-state/active.md` and any files being
actively worked on to recover full context. The files contain the decisions; the
conversation history is secondary.

## Recovery After Session Crash

If a session dies ("prompt too long") or you start a new session to continue work:

1. If a supported configured hook actually ran, use its preview; otherwise locate
   the established authorized checkpoint/report directly
2. Read the full state file for context
3. Read the partially-completed file(s) listed in the state
4. Continue from the next incomplete section or task

Read `standards/evidence-lifecycle.md` for authority and exact-input recovery.
Missing optional session state/Memory Bank uses the existing report/conversation
fallback, without initialization or checkpoint-write authority. Preserve Game
combat examples above; Product checkpoints can name API/CLI/data/workflow tasks.
