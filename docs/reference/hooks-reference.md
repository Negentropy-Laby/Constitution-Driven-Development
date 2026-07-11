# Active Hooks

Hooks are configured in `.claude/settings.json` (Claude) and `.codex/hooks.json`
(Codex); they fire automatically:

| Hook | Event | Trigger | Action |
| ---- | ----- | ------- | ------ |
| `validate-commit.sh` | PreToolUse (Bash) | `git commit` commands | Validates design doc sections, JSON data files, hardcoded values, TODO format |
| `validate-push.sh` | PreToolUse (Bash) | `git push` commands | Warns on pushes to protected branches (develop/main) |
| `validate-assets.sh` | PostToolUse (Write/Edit) | Asset file changes | Checks naming conventions and JSON validity for files in `assets/` |
| `session-start.sh` | SessionStart | Session begins | Loads sprint context, milestone, git activity; detects and previews active session state file for recovery |
| `detect-gaps.sh` | SessionStart | Session begins | Detects fresh projects (suggests /constitute) and missing documentation when code/prototypes exist, suggests /reverse-document or /project-stage-detect |
| `pre-compact.sh` | PreCompact | Context compression | Dumps session state (active.md, modified files, WIP design docs) into conversation before compaction so it survives summarization |
| `post-compact.sh` | PostCompact | After compaction | Reminds Claude to restore session state from `active.md` checkpoint |
| `notify.sh` | Notification | Notification event | Shows Windows toast notification via PowerShell |
| `session-stop.sh` | Stop | Session ends | Summarizes accomplishments and updates session log |
| `log-agent.sh` | SubagentStart | Agent spawned | Audit trail start — logs subagent invocation with timestamp |
| `log-agent-stop.sh` | SubagentStop | Agent stops | Audit trail stop — completes subagent record |
| `validate-generated-adapter-change.sh` | PostToolUse (Write/Edit; Codex `apply_patch`) | Edits to any canonical source or generated adapter | Advises the canonical source + adapter regeneration when a generated adapter (skills/agents/hooks/rules, or root/nested instructions) is edited, and advises regeneration when a canonical source is edited. Parses both Claude `tool_input.file_path` and Codex `tool_input.command` (`apply_patch`, possibly multi-file); emits JSON `additionalContext` for Codex. Does not flag Codex-native `.codex/rules/*.rules`. |

Hook reference documentation: `docs/reference/hooks-reference-details/`
Hook input schema documentation: `docs/reference/hooks-reference-details/hook-input-schemas.md`
