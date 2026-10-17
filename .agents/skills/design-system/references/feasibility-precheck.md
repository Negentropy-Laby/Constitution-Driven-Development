# Technical Feasibility Pre-Check

Before asking the user to begin designing, load technology context and surface
any constraints or knowledge gaps that will shape the design. Use the detected
domain from Phase 2.

**[游戏专用] Step 1 — Determine the engine domain for this system:**
Map the system's category (from `module-index.md`) to an engine domain:

| System Category | Engine Domain |
|----------------|--------------|
| Combat, physics, collision | Physics |
| Rendering, visual effects, shaders | Rendering |
| UI, HUD, menus | UI |
| Audio, sound, music | Audio |
| AI, pathfinding, behavior trees | Navigation / Scripting |
| Animation, IK, rigs | Animation |
| Networking, multiplayer, sync | Networking |
| Input, controls, keybinding | Input |
| Save/load, persistence, data | Core |
| Dialogue, quests, narrative | Scripting |

**[通用产品] Step 1 — Determine the stack domain for this module:**
Map the module's category (from `module-index.md`) to a stack domain:

| Module Category | Stack Domain |
|----------------|--------------|
| Foundation/Infrastructure, config, logging, error handling | Framework / Runtime |
| API, web services, request handling | API Design / Framework |
| Data models, schemas, storage | Data Storage / ORM |
| Auth, permissions, security | Auth / Security |
| UI, frontend, user-facing interfaces | Frontend / UI |
| CLI, tooling, developer-facing | CLI / Distribution |
| Data pipelines, ETL, analytics | Data Pipeline / Analytics |
| Integration, webhooks, third-party APIs | Integration / Messaging |
| Performance, caching, optimization | Performance / Caching |

**[游戏专用] Step 2 — Read engine context (if available):**
- Read `standards/technical-preferences.md` to identify the engine and version
- If engine is configured, read `docs/engine-reference/[engine]/VERSION.md`
- Read `docs/engine-reference/[engine]/modules/[domain].md` if it exists
- Read `docs/engine-reference/[engine]/breaking-changes.md` for domain-relevant entries
- Glob `docs/architecture/adr-*.md` and read any ADRs whose domain matches
  (check the Engine Compatibility table's "Domain" field)

**[通用产品] Step 2 — Read stack context (if available):**
- Read `standards/technical-preferences.md` to identify the language, framework,
  runtime, database, and pinned versions
- If stack reference docs are configured, read `docs/reference/[stack]/VERSION.md`
- Read `docs/reference/[stack]/modules/[domain].md` if it exists
- Read `docs/reference/[stack]/breaking-changes.md` for domain-relevant entries
- Glob `docs/architecture/adr-*.md` and read any ADRs whose domain matches
  (check the Technology Compatibility table's "Domain" field)

**Step 3 — Present the Feasibility Brief:**

**[游戏专用]** If engine reference docs exist, present before starting design:

```
## Technical Feasibility Brief: [System Name]
Engine: [name + version]
Domain: [domain]

### Known Engine Capabilities (verified for [version])
- [capability relevant to this system]
- [capability 2]

### Engine Constraints That Will Shape This Design
- [constraint from engine-reference or existing ADR]

### Knowledge Gaps (verify before committing to these)
- [post-cutoff feature this design might rely on — mark HIGH/MEDIUM risk]

### Existing ADRs That Constrain This System
- ADR-XXXX: [decision summary] — means [implication for this CDD]
  (or "None yet")
```

**[通用产品]** If stack reference docs exist, present before starting design:

```
## Technical Feasibility Brief: [Module Name]
Stack: [language] + [framework/runtime] [version]
Domain: [domain]

### Known Stack Capabilities (verified for [version])
- [capability relevant to this module]
- [capability 2]

### Stack Constraints That Will Shape This Design
- [constraint from stack reference or existing ADR]

### Knowledge Gaps (verify before committing to these)
- [post-cutoff framework/API behavior this design might rely on — mark HIGH/MEDIUM risk]

### Existing ADRs That Constrain This Module
- ADR-XXXX: [decision summary] — means [implication for this CDD]
  (or "None yet")
```

**[游戏专用]** If no engine reference docs exist (engine not yet configured), show a short note:
> "No engine configured yet — skipping technical feasibility check. Run
> `/setup-engine` before moving to architecture if you haven't already."

**[通用产品]** If no stack reference docs exist (stack not yet configured), show a short note:
> "No technology stack configured yet — skipping technical feasibility check. Run
> `/setup-engine` before moving to architecture if you haven't already."

**Step 4 — Ask before proceeding:**

Use `AskUserQuestion`:
- "Any constraints to add before we begin, or shall we proceed with these noted?"
  - Options: "Proceed with these noted", "Add a constraint first", "I need to check the technology docs — pause here"
