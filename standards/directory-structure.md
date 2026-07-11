# Directory Structure

```text
/
# --- Canonical common sources (hand-authored) ---
├── INSTRUCTIONS.md              # Canonical root instructions (generated to CLAUDE.md + AGENTS.md)
├── cdd-manifest.toml            # Canonical -> generated adapter contract
├── skills/                      # Canonical skills (generated into adapter runtimes)
├── agents/                      # Canonical agents (generated into adapter runtimes)
├── hooks/                       # Canonical hooks (generated into adapter runtimes)
├── rules/                       # Canonical path-scoped coding policies (generated to .claude/rules/)
├── workflow/                    # Canonical workflow catalog and generated workflow views
├── templates/                   # Canonical document and memory-bank templates
├── standards/                   # Shared coding, coordination, context, and setup standards
├── skill_testing/               # Cross-project skill/agent testing catalog, specs, rubric
├── adapters/                    # Adapter boundary notes (Claude, Codex, future runtimes)
├── docs/                        # Technical documentation (manuals, references, ADRs, examples)
# --- Nested instruction sources (runtime-neutral; generate CLAUDE.md + AGENTS.md per dir) ---
├── src/INSTRUCTIONS.md          # Canonical src/ guidance (-> src/CLAUDE.md + src/AGENTS.md)
├── design/INSTRUCTIONS.md       # Canonical design/ guidance (-> design/CLAUDE.md + design/AGENTS.md)
├── docs/INSTRUCTIONS.md         # Canonical docs/ guidance (-> docs/CLAUDE.md + docs/AGENTS.md)
# --- Generated runtime adapters (NEVER hand-edit; regenerate via scripts/sync_adapters.py) ---
├── CLAUDE.md                    # Generated root instructions (Claude)
├── AGENTS.md                    # Generated root instructions (Codex)
├── .claude/                     # MIXED OWNERSHIP: generated subtrees + hand-authored config
│   ├── settings.json            #   Hand-authored: hooks wiring, permissions, model
│   ├── statusline.sh            #   Hand-authored status line
│   ├── skills/ agents/ hooks/   #   GENERATED Claude adapters
│   └── rules/                   #   GENERATED Claude path-rule adapters
├── .agents/skills/              # GENERATED Codex skill adapters
├── .codex/                      # MIXED OWNERSHIP: generated subtrees + hand-authored config
│   ├── hooks.json               #   Hand-authored Codex hook wiring
│   ├── agents/ hooks/           #   GENERATED Codex adapters (agents as TOML)
│   └── rules/*.rules            #   Codex NATIVE command-approval policy (runtime-owned; never generator-owned)
# --- Project source / assets / design / production (not adapter assets) ---
├── src/                         # Game or product source code
│   ├── gameplay/ core/ ai/ networking/ ui/   # Game systems
│   └── api/ cli/ services/ data/              # Product systems
├── assets/                      # Game assets or product-facing assets/artifacts
├── design/                      # CDDs, product specs, narrative, levels, balance, UX
├── tests/                       # Unit, integration, performance, playtest, contract, CLI, E2E, migration
├── tools/                       # Build and pipeline tools (ci, build, asset-pipeline)
├── prototypes/                  # Throwaway prototypes (isolated from src/)
├── production/                  # Production management (sprints, milestones, releases)
│   ├── session-state/           # Ephemeral session state (gitignored)
│   └── session-logs/            # Session audit trail (gitignored)
└── memory_bank/                 # Project governance brain (created from templates/ by /constitute)
```

Generated adapter subtrees are owned by `scripts/sync_adapters.py` — only the
manifest-declared subtrees above are generated, and they must never be hand-edited.
`.claude/` and `.codex/` are **mixed-ownership** roots: they also contain
hand-authored runtime config (`settings.json`, `statusline.sh`, `hooks.json`) and,
for Codex, the native `.codex/rules/*.rules` command-approval namespace, none of
which the generator owns. `.agents/` is the **Codex** skill adapter tree (not
Copilot). Codex has no path-glob rule equivalent and consults canonical `rules/`
through root guidance rather than automatic loading.
