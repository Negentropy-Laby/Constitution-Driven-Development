#!/bin/bash
# PostToolUse hook: validates asset files (naming + JSON) after edits.
# Works for both runtimes:
#   - Claude Code Write|Edit provides tool_input.file_path  -> advisory on stderr
#   - Codex apply_patch       provides tool_input.command    -> advisory as JSON
#     on stdout (plain stdout/stderr is ignored by Codex PostToolUse).
#
# Exit behavior:
#   exit 0 = success/advisory, or a Codex JSON block decision for invalid JSON
#   exit 1 = Claude-side invalid JSON failure reported on stderr
#
# Classification: only paths under assets/ are checked.

set -u
NL=$'\n'
INPUT=$(cat)

# Parse tool_input.file_path and tool_input.command (jq, else grep/sed fallback).
FILE_PATH=""
COMMAND=""
if command -v jq >/dev/null 2>&1; then
    FILE_PATH=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
    COMMAND=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)
else
    FILE_PATH=$(printf '%s' "$INPUT" | grep -oE '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*"file_path"[[:space:]]*:[[:space:]]*"//;s/"$//;s/\\\\/\\/g' | head -1)
    COMMAND=$(printf '%s' "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\(.*\)"[[:space:]]*[,}].*/\1/p' | sed 's|\\\\|/|g' | head -1)
fi

norm() { printf '%s' "$1" | sed 's|\\|/|g'; }

# Hook commands run with the session cwd, which may be below the repository
# root. Resolve relative edit paths against Git's toplevel for filesystem checks;
# retain the original normalized path for classification and diagnostics.
GIT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || GIT_ROOT=""
GIT_ROOT=$(norm "$GIT_ROOT")
resolve_for_check() {
    local p; p=$(norm "$1")
    case "$p" in
        /*|[A-Za-z]:/*) printf '%s' "$p" ;;
        *)
            if [ -n "$GIT_ROOT" ]; then
                printf '%s/%s' "$GIT_ROOT" "$p"
            else
                printf '%s' "$p"
            fi
            ;;
    esac
}

# Collect candidate paths as provided (deduped) so diagnostics preserve the
# patch spelling. Filesystem checks resolve them separately through
# resolve_for_check() above.
PATHS=""
add_path() {
    local p existing; p=$(norm "$1"); [ -z "$p" ] && return
    if [ -n "$PATHS" ]; then
        while IFS= read -r existing; do
            [ "$existing" = "$p" ] && return
        done < <(printf '%s\n' "$PATHS")
    fi
    PATHS="${PATHS:+$PATHS$NL}$p"
}
decode_patch_command() {
    local decoded=${1//\\n/$'\n'}
    printf '%s\n' "$decoded"
}
json_escape() {
    local escaped=$1
    escaped=${escaped//\\/\\\\}
    escaped=${escaped//\"/\\\"}
    escaped=${escaped//$'\n'/\\n}
    escaped=${escaped//$'\r'/\\r}
    escaped=${escaped//$'\t'/\\t}
    printf '%s' "$escaped"
}
[ -n "$FILE_PATH" ] && add_path "$FILE_PATH"
if [ -n "$COMMAND" ]; then
    # apply_patch Update/Add headers plus an optional rename destination.
    while IFS= read -r pp; do
        [ -n "$pp" ] && add_path "$pp"
    done < <(
        decode_patch_command "$COMMAND" |
            sed -n \
                -e 's/^.*Update File: //p' \
                -e 's/^.*Add File: //p' \
                -e 's/^.*Move to: //p'
    )
fi

EMIT_JSON=false
[ -n "$COMMAND" ] && EMIT_JSON=true

WARNINGS=""
ERRORS=""
saw_assets=false

while IFS= read -r P; do
    [ -z "$P" ] && continue
    case "$P" in
        */assets/*|assets/*) ;;
        *) continue ;;
    esac
    saw_assets=true
    FILENAME=$(basename "$P")
    # ADVISORY: lowercase-with-underscores naming (POSIX grep, not Perl).
    if echo "$FILENAME" | grep -qE '[A-Z[:space:]-]'; then
        WARNINGS="${WARNINGS}${WARNINGS:+$NL}  NAMING: $P must be lowercase with underscores (got: $FILENAME)"
    fi
    # BLOCKING: JSON validity for assets/data/*.json.
    if echo "$P" | grep -qE '(^|/)assets/data/.*\.json$'; then
        CHECK_PATH=$(resolve_for_check "$P")
        if [ -f "$CHECK_PATH" ]; then
            PYTHON_CMD=""
            for cmd in python python3 py; do
                if command -v "$cmd" >/dev/null 2>&1; then PYTHON_CMD="$cmd"; break; fi
            done
            if [ -n "$PYTHON_CMD" ]; then
                if ! "$PYTHON_CMD" -m json.tool "$CHECK_PATH" > /dev/null 2>&1; then
                    ERRORS="${ERRORS}${ERRORS:+$NL}  FORMAT: $P is not valid JSON — fix syntax errors before continuing"
                fi
            fi
        fi
    fi
done < <(printf '%s\n' "$PATHS")

[ "$saw_assets" = false ] && exit 0

emit_block() {
    local msg=""
    if [ -n "$WARNINGS" ]; then
        msg="${msg}=== Asset Validation: Warnings ===${WARNINGS}${NL}==================================${NL}(Warnings are advisory. Fix before final commit.)${NL}"
    fi
    if [ -n "$ERRORS" ]; then
        msg="${msg}=== Asset Validation: ERRORS (Blocking) ===${ERRORS}${NL}===========================================${NL}Fix these errors before proceeding."
    fi
    if $EMIT_JSON; then
        if command -v jq >/dev/null 2>&1; then
            if [ -n "$ERRORS" ]; then
                printf '%s' "$msg" | jq -Rsc '{decision:"block",reason:.,hookSpecificOutput:{hookEventName:"PostToolUse",additionalContext:.}}'
            else
                printf '%s' "$msg" | jq -Rsc '{hookSpecificOutput:{hookEventName:"PostToolUse",additionalContext:.}}'
            fi
        else
            local esc
            esc=$(json_escape "$msg")
            if [ -n "$ERRORS" ]; then
                printf '{"decision":"block","reason":"%s","hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s"}}\n' "$esc" "$esc"
            else
                printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s"}}\n' "$esc"
            fi
        fi
    else
        printf '%s\n' "$msg" >&2
    fi
}

if [ -n "$WARNINGS" ] || [ -n "$ERRORS" ]; then
    emit_block
fi
if [ -n "$ERRORS" ]; then
    # Codex consumes the block decision from stdout only on a successful hook
    # run. Claude keeps the existing non-zero stderr failure contract.
    $EMIT_JSON && exit 0
    exit 1
fi
exit 0
