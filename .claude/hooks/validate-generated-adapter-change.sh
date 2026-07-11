#!/bin/bash
# PostToolUse hook: advises after edits to canonical sources or generated adapters.
# Advisory only (exit 0 = non-blocking).
#
# Works for both runtimes:
#   - Claude Code Write|Edit provides tool_input.file_path  -> advisory on stderr
#   - Codex apply_patch       provides tool_input.command    -> advisory as JSON
#     on stdout (plain stdout/stderr is ignored by Codex PostToolUse).
#
# Classification (generated trees checked first -- they are more specific):
#   generated adapter edit  -> warn GENERATED; point at canonical source + regen
#   canonical source edit   -> advise regeneration (and skill-test/lint for skills)
# Codex native .codex/rules/*.rules (command-approval policy) is never flagged.

set -u
NL=$'\n'
INPUT=$(cat)

# --- parse tool_input.file_path and tool_input.command (jq, else grep fallback) ---
FILE_PATH=""
COMMAND=""
if command -v jq >/dev/null 2>&1; then
    FILE_PATH=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
    COMMAND=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)
else
    FILE_PATH=$(printf '%s' "$INPUT" | grep -oE '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*"file_path"[[:space:]]*:[[:space:]]*"//;s/"$//;s/\\\\/\\/g' | head -1)
    COMMAND=$(printf '%s' "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\(.*\)"[[:space:]]*[,}].*/\1/p' | sed 's|\\\\|/|g' | head -1)
fi

# Normalize backslashes to forward slashes, then reduce an absolute path to
# repo-relative (best-effort via git toplevel; cygpath fallback for the msys/
# Windows form mismatch). Relative paths pass through unchanged. Absolute paths
# that cannot be reduced are left as-is so the */CLAUDE.md fallback below still
# flags them instead of going silent.
to_relpath() {
    local p root stripped pu ru s2
    p=$(printf '%s' "$1" | sed 's|\\|/|g')
    case "$p" in
        /*|[A-Za-z]:/*)
            root=$(git rev-parse --show-toplevel 2>/dev/null) || root=""
            if [ -n "$root" ]; then
                root=$(printf '%s' "$root" | sed 's|\\|/|g')
                stripped="${p#"$root"/}"
                if [ "$stripped" != "$p" ]; then
                    p="$stripped"
                elif command -v cygpath >/dev/null 2>&1; then
                    pu=$(cygpath -u "$p" 2>/dev/null) || pu=""
                    ru=$(cygpath -u "$root" 2>/dev/null) || ru=""
                    if [ -n "$pu" ] && [ -n "$ru" ]; then
                        s2="${pu#"$ru"/}"
                        [ "$s2" != "$pu" ] && p="$s2"
                    fi
                fi
            fi
            ;;
    esac
    printf '%s' "$p"
}

# Collect candidate paths (dedup, preserve order).
PATHS=""
add_path() {
    local p existing; p=$(to_relpath "$1"); [ -z "$p" ] && return
    if [ -n "$PATHS" ]; then
        while IFS= read -r existing; do
            [ "$existing" = "$p" ] && return
        done < <(printf '%s\n' "$PATHS")
    fi
    PATHS="${PATHS:+$PATHS$NL}$p"
}
[ -n "$FILE_PATH" ] && add_path "$FILE_PATH"
if [ -n "$COMMAND" ]; then
    # apply_patch headers "*** Update/Add/Delete File: <path>" and optional
    # "*** Move to: <path>" destinations. Decode literal \n first so the grep/sed
    # fallback (when jq is absent) splits lines the same way jq would.
    while IFS= read -r pp; do
        [ -n "$pp" ] && add_path "$pp"
    done < <(
        printf '%s\n' "$COMMAND" |
            sed 's/\\n/\n/g' |
            sed -n \
                -e 's/^.*\(Update\|Add\|Delete\) File: //p' \
                -e 's/^.*Move to: //p'
    )
fi

[ -z "$PATHS" ] && exit 0

# Codex invoked us via apply_patch (command present) -> emit JSON on stdout.
EMIT_JSON=false
[ -n "$COMMAND" ] && EMIT_JSON=true

ADVISORY=""
emit() { ADVISORY="${ADVISORY}${ADVISORY:+$NL}$1"; }

while IFS= read -r P; do
    [ -z "$P" ] && continue
    case "$P" in
        # --- generated instruction adapters (root + nested) ---
        CLAUDE.md|AGENTS.md)
            emit "=== Generated Adapter Edited: root-instructions ==="
            emit "WARNING: \"CLAUDE.md\" and \"AGENTS.md\" are GENERATED. Edits overwritten by:"
            emit "  python scripts/sync_adapters.py --write --class root-instructions"
            emit "Edit the canonical source instead: INSTRUCTIONS.md" ;;
        src/CLAUDE.md|src/AGENTS.md)
            emit "=== Generated Adapter Edited: nested-src ==="
            emit "WARNING: src/CLAUDE.md and src/AGENTS.md are GENERATED. Edit src/INSTRUCTIONS.md, then:"
            emit "  python scripts/sync_adapters.py --write --class nested-src" ;;
        design/CLAUDE.md|design/AGENTS.md)
            emit "=== Generated Adapter Edited: nested-design ==="
            emit "WARNING: design/CLAUDE.md and design/AGENTS.md are GENERATED. Edit design/INSTRUCTIONS.md, then:"
            emit "  python scripts/sync_adapters.py --write --class nested-design" ;;
        docs/CLAUDE.md|docs/AGENTS.md)
            emit "=== Generated Adapter Edited: nested-docs ==="
            emit "WARNING: docs/CLAUDE.md and docs/AGENTS.md are GENERATED. Edit docs/INSTRUCTIONS.md, then:"
            emit "  python scripts/sync_adapters.py --write --class nested-docs" ;;
        */CLAUDE.md|*/AGENTS.md)
            # Absolute instruction path that could not be reduced to repo-relative.
            emit "=== Generated Adapter Edited: instruction (absolute path) ==="
            emit "WARNING: a generated CLAUDE.md or AGENTS.md was edited. These are GENERATED."
            emit "Edit the canonical INSTRUCTIONS.md (root, or src/ / design/ / docs/), then regenerate:"
            emit "  python scripts/sync_adapters.py --write" ;;
        # --- generated skill trees ---
        */.claude/skills/*|*/.agents/skills/*|.claude/skills/*|.agents/skills/*)
            SKILL=$(printf '%s' "$P" | sed -nE 's#.*\.(claude|agents)/skills/([^/]+).*#\2#p' | head -1)
            emit "=== Generated Adapter Edited: ${SKILL:-skill} ==="
            emit "WARNING: \".claude/skills/\" and \".agents/skills/\" are GENERATED. Edits here are overwritten by:"
            emit "  python scripts/sync_adapters.py --write --class skills"
            [ -n "$SKILL" ] && emit "Edit the canonical source instead: skills/$SKILL/SKILL.md" ;;
        # --- generated agent trees ---
        */.claude/agents/*|*/.codex/agents/*|.claude/agents/*|.codex/agents/*)
            emit "=== Generated Adapter Edited: agents ==="
            emit "WARNING: \".claude/agents/\" and \".codex/agents/\" are GENERATED. Edit agents/<name>.md, then:"
            emit "  python scripts/sync_adapters.py --write --class agents" ;;
        # --- generated hook trees ---
        */.claude/hooks/*|*/.codex/hooks/*|.claude/hooks/*|.codex/hooks/*)
            emit "=== Generated Adapter Edited: hooks ==="
            emit "WARNING: \".claude/hooks/\" and \".codex/hooks/\" are GENERATED. Edit hooks/<name>.sh, then:"
            emit "  python scripts/sync_adapters.py --write --class hooks" ;;
        # --- generated rules tree (Claude only) ---
        */.claude/rules/*|.claude/rules/*)
            emit "=== Generated Adapter Edited: rules ==="
            emit "WARNING: \".claude/rules/\" is GENERATED. Edit rules/<name>.md, then:"
            emit "  python scripts/sync_adapters.py --write --class rules" ;;
        # --- canonical source edits (advise regeneration) ---
        INSTRUCTIONS.md)
            emit "=== Canonical Source Modified: root-instructions ==="
            emit "Regenerate runtime adapters: python scripts/sync_adapters.py --write --class root-instructions" ;;
        src/INSTRUCTIONS.md)
            emit "=== Canonical Source Modified: nested-src ==="
            emit "Regenerate: python scripts/sync_adapters.py --write --class nested-src" ;;
        design/INSTRUCTIONS.md)
            emit "=== Canonical Source Modified: nested-design ==="
            emit "Regenerate: python scripts/sync_adapters.py --write --class nested-design" ;;
        docs/INSTRUCTIONS.md)
            emit "=== Canonical Source Modified: nested-docs ==="
            emit "Regenerate: python scripts/sync_adapters.py --write --class nested-docs" ;;
        */skills/*/SKILL.md|skills/*/SKILL.md)
            SKILL=$(printf '%s' "$P" | sed -nE 's#.*skills/([^/]+)/SKILL\.md.*#\1#p' | head -1)
            emit "=== Canonical Skill Modified: ${SKILL:-skill} ==="
            if [ -n "$SKILL" ]; then
                emit "Run /skill-test static $SKILL to validate structural compliance."
                emit "Run python scripts/skill_lint.py skills/$SKILL/SKILL.md for non-blocking markdown/frontmatter checks."
            fi
            emit "Regenerate runtime adapters: python scripts/sync_adapters.py --write --class skills" ;;
        */agents/*.md|agents/*.md)
            emit "=== Canonical Source Modified: agents ==="
            emit "Regenerate: python scripts/sync_adapters.py --write --class agents" ;;
        */hooks/*.sh|hooks/*.sh)
            emit "=== Canonical Source Modified: hooks ==="
            emit "Regenerate: python scripts/sync_adapters.py --write --class hooks" ;;
        */rules/*.md|rules/*.md)
            RULE=$(printf '%s' "$P" | sed -nE 's#.*rules/([^/]+)\.md.*#\1#p' | head -1)
            emit "=== Canonical Source Modified: rules/${RULE:-rule} ==="
            emit "Regenerate: python scripts/sync_adapters.py --write --class rules" ;;
    esac
done < <(printf '%s\n' "$PATHS")

[ -z "$ADVISORY" ] && exit 0

if $EMIT_JSON; then
    # Codex PostToolUse ignores plain stdout; emit JSON additionalContext.
    if command -v jq >/dev/null 2>&1; then
        printf '%s' "$ADVISORY" | jq -Rsc '{hookSpecificOutput:{hookEventName:"PostToolUse",additionalContext:.}}'
    else
        ESC=$(printf '%s' "$ADVISORY" | sed 's/\\/\\\\/g; s/"/\\"/g' | sed ':a;N;$!ba;s/\n/\\n/g')
        printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s"}}\n' "$ESC"
    fi
else
    printf '%s\n===================================================\n' "$ADVISORY" >&2
fi
exit 0
