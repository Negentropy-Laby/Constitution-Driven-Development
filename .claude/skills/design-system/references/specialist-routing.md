# CDD Specialist Agent Routing

> Loaded on demand from `design-system/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

## 6. Specialist Agent Routing

This skill delegates to specialist agents for domain expertise. The main session
orchestrates the overall flow; agents provide expert content.

| System Category | Primary Agent | Supporting Agent(s) |
|----------------|---------------|---------------------|
| **Foundation/Infrastructure** (event bus, save/load, scene mgmt, service locator) | `systems-designer` | `gameplay-programmer` (feasibility), `engine-programmer` (engine integration) |
| Combat, damage, health | `game-designer` | `systems-designer` (formulas), `ai-programmer` (enemy AI), `art-director` (hit feedback visual direction, VFX intent) |
| Economy, loot, crafting | `economy-designer` | `systems-designer` (curves), `game-designer` (loops) |
| Progression, XP, skills | `game-designer` | `systems-designer` (curves), `economy-designer` (sinks) |
| Dialogue, quests, lore | `game-designer` | `narrative-director` (story), `writer` (content), `art-director` (character visual profiles, cinematic tone) |
| UI systems (HUD, menus) | `game-designer` | `ux-designer` (flows), `ui-programmer` (feasibility), `art-director` (visual style direction), `technical-artist` (render/shader constraints) |
| Audio systems | `game-designer` | `audio-director` (direction), `sound-designer` (specs) |
| AI, pathfinding, behavior | `game-designer` | `ai-programmer` (implementation), `systems-designer` (scoring) |
| Level/world systems | `game-designer` | `level-designer` (spatial), `world-builder` (lore) |
| Camera, input, controls | `game-designer` | `ux-designer` (feel), `gameplay-programmer` (feasibility) |
| Animation, character movement | `game-designer` | `art-director` (animation style, pose language), `technical-artist` (rig/blend constraints), `gameplay-programmer` (feel) |
| Visual effects, particles, shaders | `game-designer` | `art-director` (VFX visual direction), `technical-artist` (performance budget, shader complexity), `systems-designer` (trigger/state integration) |
| Character systems (stats, archetypes) | `game-designer` | `art-director` (character visual archetype), `narrative-director` (character arc alignment), `systems-designer` (stat formulas) |

[Product] Product module routing:

| Module Category | Primary Agent | Supporting Agent(s) |
|----------------|---------------|---------------------|
| **Foundation/Infrastructure** (config, logging, error handling, data store) | `lead-programmer` | language specialist (implementation), `devops-engineer` (deployment) |
| API, web services, request handling | `lead-programmer` | language specialist (framework idioms), `security-engineer` (auth) |
| Data models, schemas, storage | `lead-programmer` | language specialist (ORM/query patterns), `performance-analyst` (query optimization) |
| Auth, permissions, security | `lead-programmer` | `security-engineer` (audit), language specialist (implementation) |
| UI, frontend, user-facing interfaces | `lead-programmer` | `ux-designer` (flows), `ui-programmer` (implementation), `accessibility-specialist` |
| CLI, tooling, developer-facing | `lead-programmer` | language specialist (CLI conventions), `devops-engineer` (distribution) |
| Data pipelines, ETL, analytics | `lead-programmer` | `analytics-engineer` (data modeling), language specialist (implementation) |
| Integration, webhooks, third-party APIs | `lead-programmer` | `devops-engineer` (reliability), `security-engineer` (data exposure) |
| Performance, caching, optimization | `performance-analyst` | language specialist (profiling), `lead-programmer` (architecture impact) |

**When delegating via Task tool**:
- Provide: system/module name, the relevant game or product concept summary,
  dependency CDD excerpts, the specific section being worked on, and what
  question needs expert input
- The agent returns analysis/proposals to the main session
- The main session presents the agent's output to the user via `AskUserQuestion`
- The user decides; the main session writes to file
- Agents do NOT write to files directly — the main session owns all file writes

---
