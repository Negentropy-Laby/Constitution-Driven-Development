# Directory Structure

The tree below describes the designated Source-library checkout. An import-mode
consumer keeps approved platform outputs, necessary neutral support and its
project-custom inputs; it excludes general root `agents/` or `skills/` mirrors
from Git submission/publication. This is a content boundary, not a local-directory
restriction: ignored maintenance files may remain in either repository.
Use the project's reviewed delivery allowlist, actual installed readers and
portable Source binding. Required neutral inputs are listed in
`adapters/README.md` and extend through the selected workflow's actual required
references; do not omit them or add general source mirrors to Git delivery. Ordinary
installed-file use needs no maintenance reader, profile or lock. Source-dependent
updates preserve reviewed project differences and require the sole actual Source.
Retain approved portable project differences in the project's established configuration.

```text
/
# --- Canonical common sources in the Source library (hand-authored) ---
├── INSTRUCTIONS.md              # Canonical root instructions (generated to CLAUDE.md + AGENTS.md)
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
# --- Installed runtime adapters (derived from the canonical owners) ---
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
│   ├── session-state/           # Ephemeral contents gitignored; .gitkeep retained
│   └── session-logs/            # Session audit trail (gitignored)
└── memory_bank/                 # Project governance brain (created from templates/ by /constitute)
```

In the Source-library checkout, the listed adapter subtrees derive from their
canonical owners. Review canonical changes and the exact platform projections
together; do not independently author the derived files.
`.claude/` and `.codex/` are **mixed-ownership** roots: they also contain
hand-authored runtime config (`settings.json`, `statusline.sh`, `hooks.json`) and,
for Codex, the native `.codex/rules/*.rules` command-approval namespace, none of
which the generator owns. `.agents/` is the **Codex** skill adapter tree (not
Copilot). Codex has no path-glob rule equivalent and consults canonical `rules/`
through root guidance rather than automatic loading.

## Discovery and evidence boundaries

In an import-mode project, offline installed Markdown/context reads do not
require current Source availability, but do not establish Source freshness or
regeneration/write authority. Source checks and generation require actual Source
inputs and separate approved maintenance scope. Never recover a consumer's
missing canonical root by copying installed outputs back into `agents/` or `skills/`.

The layout records ownership, not activation. Skills copy verbatim to
`.claude/skills/` and use platform-specific wording for `.agents/skills/`.
Agent Markdown copies to Claude; Codex TOML retains only `name`, `description`
and `developer_instructions`, dropping the seven known operational fields in
`adapters/README.md`. Generated files do not promise equivalent model, tools,
memory, isolation or execution.

A platform-definition comparison does not certify every linked input. Relied-on
neutral support in `standards/`, `templates/`, `workflow/`, `skill_testing/`,
`rules/`, `docs/` and `adapters/` needs its own exact identity; freshness does not
certify linked semantics. The consumer's T2 framework contract binds installed
paths and designated Source authority; local general-source/tool presence does
not confer that authority and does not determine submission compliance.
Optional `memory_bank/` requires separately authorized initialization. Its T2
testing mount references canonical `skill_testing/` without another testing tree.
Read `standards/evidence-lifecycle.md` and actual runtime metadata for evidence,
loading, execution and qualification claims.
