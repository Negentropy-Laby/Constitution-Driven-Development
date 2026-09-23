# Cross-CDD Design Holism Checks

> Loaded on demand from `review-all-gdds/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

## Phase 3: Design Holism

Review all CDDs together through the lens of design theory. These are issues
that individual CDD reviews cannot catch because they require seeing all
modules at once.

**[游戏专用]** Game design holism checks:

### 3a: Progression Loop Competition

A game should have one dominant progression loop that players feel is "the
point" of the game, with supporting loops that feed into it. When multiple
systems compete equally as the primary progression driver, players don't know
what the game is about.

Scan all CDDs for systems that:
- Award the player's primary resource (XP, levels, prestige, unlocks)
- Define themselves as the "core" or "main" loop
- Have comparable depth and time investment to other systems doing the same

```
⚠️  Competing Progression Loops
combat.md: Awards XP, unlocks abilities, is described as "the core loop"
crafting.md: Awards XP, unlocks recipes, is described as "the primary activity"
exploration.md: Awards XP, unlocks map areas, described as "the main driver"
→ Three systems all claim to be the primary progression loop and all award
  the same primary currency. Players will optimise one and ignore the others.
  Consider: one primary loop with the others as support systems.
```

**[通用产品]** Value Loop Competition:

A product should have one dominant value loop that users feel is "the point"
of the product, with supporting features that feed into it. When multiple
modules compete equally as the primary value driver, users don't know what
the product is about.

Scan all CDDs for modules that:
- Claim to deliver the primary user outcome or "main experience"
- Define themselves as the "core" or "main" workflow
- Have comparable feature depth and UI prominence

```
⚠️  Competing Value Loops
dashboard.md: Delivers insights, described as "the main experience"
reporting.md: Delivers insights, described as "the primary workflow"
notifications.md: Delivers insights, described as "the core value prop"
→ Three modules all claim to be the primary value driver and all deliver
  the same user outcome. Users will gravitate to one and ignore the others.
  Consider: one primary value loop with the others as supporting features.
```

### 3b: Player Attention Budget

Count how many systems require active player attention simultaneously during
a typical session. Each actively-managed system costs attention:

- Active = player must make decisions about this system regularly during play
- Passive = system runs automatically, player sees results but doesn't manage it

More than 3-4 simultaneously active systems creates cognitive overload for most
players. Present the count and flag if it exceeds 4 concurrent active systems:

```
⚠️  Cognitive Load Risk
Simultaneously active systems during [core loop moment]:
  1. [system-a].md — [decision type] (active)
  2. [system-b].md — [resource management] (active)
  3. [system-c].md — [tracking] (active)
  4. [system-d].md — [item/action use] (active)
  5. [system-e].md — [cooldown/timer management] (active)
  6. [system-f].md — [coordination decisions] (active)
→ 6 simultaneously active systems during the core loop.
  Research suggests 3-4 is the comfortable limit for most players.
  Consider: which of these can be made passive or simplified?
```

**[通用产品]** User Cognitive Load:

Count how many modules require active user attention simultaneously during a
typical session. More than 3-4 simultaneously active interaction modes creates
cognitive overload for most users.

```
⚠️  Cognitive Load Risk
Simultaneously active modules during [core workflow]:
  1. realtime-notifications.md — push alerts (active)
  2. dashboard.md — widget updates (active)
  3. inline-editing.md — form interactions (active)
  4. search.md — query input (active)
  5. chat.md — messaging (active)
→ 5 simultaneously active interaction modes during the core workflow.
  Research suggests 3-4 is the comfortable limit for most users.
  Consider: which of these can be made passive or batched?
```

### 3c: Dominant Strategy Detection

**[游戏专用]** A dominant strategy makes other strategies irrelevant — players discover it,
use it exclusively, and find the rest of the game boring. Look for:

- **Resource monopolies**: One strategy generates a resource significantly
  faster than all others
- **Risk-free power**: A strategy that is both high-reward and low-risk
  (if high-risk strategies exist, they need proportionally higher reward)
- **No trade-offs**: An option that is superior in all dimensions to all others
- **Obvious optimal path**: If any progression choice is "clearly correct",
  the others aren't real choices

```
⚠️  Potential Dominant Strategy
combat.md: Ranged attacks deal 80% of melee damage with no risk
combat.md: Melee attacks deal 100% damage but require close range
→ Unless melee has a significant compensating advantage (AOE, stagger,
  resource regeneration), ranged is dominant — higher safety, only 20% less
  damage. Consider what melee offers that ranged cannot.
```

**[通用产品]** Dominant Path Detection:

A dominant path makes other workflows irrelevant — users discover it, use it
exclusively, and never explore the rest of the product. Look for:

- **Workflow monopolies**: One workflow achieves the result significantly faster
- **Risk-free automation**: A bulk operation that is both safer and faster than
  the manual workflow it replaces
- **No trade-offs**: An option superior in all dimensions (speed, accuracy, effort)
- **Obvious optimal path**: If any workflow choice is "clearly correct", the
  others aren't real choices

```
⚠️  Potential Dominant Path
import.md: CSV bulk import processes 1000 records in 10 seconds
manual-entry.md: Form-based entry processes 5 records per minute
→ Unless manual entry has a significant compensating advantage (data validation,
  relationship mapping, audit trail), bulk import is dominant — faster, less
  error-prone. Consider what manual entry offers that import cannot.
```

### 3d: Economic Loop Analysis

**[游戏专用]** Identify all resources across all CDDs (gold, XP, crafting materials, stamina,
health, mana, etc.). For each resource, map its **sources** (how players gain
it) and **sinks** (how players spend it).

Flag dangerous economic conditions:

| Condition | Sign | Risk |
|-----------|------|------|
| **Infinite source, no sink** | Resource accumulates indefinitely | Late game becomes trivially easy |
| **Sink, no source** | Resource drains to zero | System becomes unavailable |
| **Source >> Sink** | Surplus accumulates | Resource becomes meaningless |
| **Sink >> Source** | Constant scarcity | Frustration and gatekeeping |
| **Positive feedback loop** | More resource → easier to earn more | Runaway leader, snowball |
| **No catch-up** | Falling behind accelerates deficit | Unrecoverable states |

```
🔴 Economic Imbalance: Unbounded Positive Feedback
gold economy:
  Sources: monster drops (scales with player power), merchant selling (unlimited)
  Sinks: equipment purchase (one-time), ability upgrades (finite count)
→ After equipment and abilities are purchased, gold has no sink.
  Infinite surplus. Gold becomes meaningless mid-game.
  Add ongoing gold sinks (upkeep, consumables, cosmetics, gambling).
```

**[通用产品]** Data Flow Loop Analysis:

Identify all data flows across all CDDs. For each data source, map its
**inputs** (how data enters the system) and **outputs** (how data is consumed
or archived).

Flag dangerous data conditions:

| Condition | Sign | Risk |
|-----------|------|------|
| **Infinite source, no sink** | Data accumulates indefinitely | Unbounded storage growth, degraded query performance |
| **Sink, no source** | Data expected but never produced | Feature becomes unavailable |
| **Source >> Sink** | Data production far exceeds consumption | Storage costs, stale data |
| **Sink >> Source** | Constant demand, insufficient supply | Frustration, data gaps |
| **Unbounded feedback loop** | More data → easier to produce more | Resource exhaustion |
| **No cleanup** | Archived state never pruned | Compliance risk, storage cost |

```
🔴 Data Flow Imbalance: Unbounded Growth
api-ingestion.md:
  Sources: event stream (unlimited), user uploads (unlimited)
  Sinks: real-time dashboard (last 24h only), export (on-demand)
→ After 24 hours, ingested data has no consumer but is never archived or
  pruned. Storage grows linearly with no bound. Add archival policy or
  time-to-live to control storage costs and query performance.
```

### 3e: Difficulty Curve Consistency

**[游戏专用]** When multiple systems scale with player progression, they must scale in
compatible directions and at compatible rates. Mismatched scaling curves
create unintended difficulty spikes or trivialisations.

For each system that scales over time, extract:
- What scales (enemy health, player damage, resource cost, area size)
- How it scales (linear, exponential, stepped)
- When it scales (level, time, area)

Compare all scaling curves. Flag mismatches:

```
⚠️  Difficulty Curve Mismatch
combat.md: Enemy health scales exponentially with area (×2 per area)
progression.md: Player damage scales linearly with level (+10% per level)
→ By area 5, enemies have 32× base health; player deals ~1.5× base damage.
  The gap widens indefinitely. Late areas will become inaccessibly difficult
  unless the curves are reconciled.
```

**[通用产品]** Complexity Curve Consistency:

When multiple modules increase in feature complexity across versions, they
must scale at compatible rates. Mismatched complexity curves create
unintended adoption barriers or feature abandonment.

```
⚠️  Complexity Curve Mismatch
user-management.md: Basic CRUD in v1, RBAC in v2, SSO in v3 (linear growth)
reporting.md: Basic charts in v1, custom SQL in v2, ML predictions in v3 (exponential)
→ By v3, reporting requires data science expertise while user management is
  still accessible. The complexity gap widens — late-adopter users may abandon
  reporting entirely. Ensure all modules scale complexity at compatible rates.
```

### 3f: Pillar Alignment

**[游戏专用]** Every system should clearly serve at least one design pillar. A system that
serves no pillar is "scope creep by design" — it's in the game but not in
service of what the game is trying to be.

For each CDD system, check its Player Fantasy section against the design pillars.
Flag any system whose stated fantasy doesn't map to any pillar:

```
⚠️  Pillar Drift
fishing-system.md: Player Fantasy — "peaceful, meditative activity"
Pillars: "Brutal Combat", "Tense Survival", "Emergent Stories"
→ The fishing system serves none of the three pillars. Either add a pillar
  that covers it, redesign it to serve an existing pillar, or cut it.
```

Also check anti-pillars — flag any system that does what an anti-pillar
explicitly says the game will NOT do:

```
🔴 Anti-Pillar Violation
Anti-Pillar: "We will NOT have linear story progression — player defines their path"
main-quest.md: Defines a 12-chapter linear story with mandatory sequence
→ This system directly violates the defined anti-pillar.
```

**[通用产品]** Principle Alignment:

Every module should clearly serve at least one project principle. A module
that serves no principle is "scope creep by design" — it's in the product
but not in service of what the product is trying to be.

For each CDD module, check its User Promise section against the project
principles. Flag any module whose stated promise doesn't map to any principle.

```
⚠️  Principle Drift
chat-module.md: User Promise — "real-time communication"
Principles: "Data Accuracy", "Workflow Automation", "Audit Compliance"
→ The chat module serves none of the three principles. Either add a principle
  that covers it, redesign it to serve an existing principle, or cut it.
```

Also check anti-principles — flag any module that does what an anti-principle
explicitly says the project will NOT do.

### 3g: Player Fantasy Coherence

**[游戏专用]** The player fantasies across all systems should be compatible — they should
reinforce a consistent identity for what the player IS in this game. Conflicting
player fantasies create identity confusion.

```
⚠️  Player Fantasy Conflict
combat.md: "You are a ruthless, precise warrior — every kill is earned"
dialogue.md: "You are a charismatic diplomat — violence is always avoidable"
exploration.md: "You are a reckless adventurer — diving in without a plan"
→ Three systems present incompatible identities. Players will feel the game
  doesn't know what it wants them to be. Consider: do these fantasies serve
  the same core identity from different angles, or do they genuinely conflict?
```

[Product] User Experience Coherence:

The user experience across all modules should be compatible -- they should
reinforce a consistent mental model. Conflicting UX patterns create user
confusion and erode trust.

```
⚠️  UX Coherence Conflict
dashboard.md: Drag-and-drop widgets, real-time updates, infinite scroll
admin-panel.md: Form-based CRUD, page reloads, paginated tables
cli-tool.md: Command-line only, pipeable output, no visual feedback
-> Three modules present incompatible interaction models. Users will feel the
  product does not know what kind of tool it wants to be. Consider: do these
  UX patterns serve different user personas, or do they genuinely conflict
  for the same user?
```

---
