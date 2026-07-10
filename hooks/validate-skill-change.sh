#!/bin/bash
# PostToolUse hook: advises after skill file changes.
# Advisory only (exit 0 = non-blocking).
#
# Classification (generated trees checked first — they are more specific):
#   - generated adapter edits  .claude/skills/<name>/ or .agents/skills/<name>/
#       -> warn the file is GENERATED and will be overwritten on regeneration;
#          point at the canonical source
#   - canonical skill edits    skills/<name>/SKILL.md
#       -> advise skill-test, canonical lint, and adapter regeneration
#
# Input schema (PostToolUse for Write|Edit):
# { "tool_name": "Write", "tool_input": { "file_path": "...", "content": "..." } }

INPUT=$(cat)

# Parse file path -- use jq if available, fall back to grep
if command -v jq >/dev/null 2>&1; then
    FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
else
    FILE_PATH=$(echo "$INPUT" | grep -oE '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/"file_path"[[:space:]]*:[[:space:]]*"//;s/"$//;s/\\\\/\\/g')
fi

# Normalize path separators (Windows backslash to forward slash)
FILE_PATH=$(echo "$FILE_PATH" | sed 's|\\|/|g')

# --- Generated adapter trees: warn (overwritten on regeneration) ---
if echo "$FILE_PATH" | grep -qE '(^|/)\.(claude|agents)/skills/[^/]+/'; then
    SKILL_NAME=$(echo "$FILE_PATH" | sed -nE 's#.*\.(claude|agents)/skills/([^/]+).*#\2#p' | head -1)
    echo "=== Generated Adapter Edited: ${SKILL_NAME:-unknown} ===" >&2
    echo "WARNING: \".claude/skills/\" and \".agents/skills/\" are GENERATED. Edits here are overwritten by:" >&2
    echo "  python scripts/sync_adapters.py --write --class skills" >&2
    if [ -n "$SKILL_NAME" ]; then
        echo "Edit the canonical source instead: skills/$SKILL_NAME/SKILL.md" >&2
    fi
    echo "===================================================" >&2
    exit 0
fi

# --- Canonical skill source: skills/<name>/SKILL.md ---
if echo "$FILE_PATH" | grep -qE '(^|/)skills/[^/]+/SKILL\.md$'; then
    SKILL_NAME=$(echo "$FILE_PATH" | sed -nE 's#.*skills/([^/]+)/SKILL\.md.*#\1#p' | head -1)
    if [ -n "$SKILL_NAME" ]; then
        echo "=== Canonical Skill Modified: $SKILL_NAME ===" >&2
        echo "Run /skill-test static $SKILL_NAME to validate structural compliance." >&2
        echo "Run python scripts/skill_lint.py skills/$SKILL_NAME/SKILL.md for non-blocking markdown/frontmatter checks." >&2
        echo "Regenerate runtime adapters: python scripts/sync_adapters.py --write --class skills" >&2
        echo "===================================================" >&2
    fi
    exit 0
fi

exit 0
