---
name: brainstorm
description: "Use this skill when a new game or software product needs a collaboratively authored concept document covering users, goals, scope, and design principles before module planning."
argument-hint: "[domain hint, or 'open'] [--review full|lean|solo]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, WebSearch, Task, AskUserQuestion
---

## Required reading and completion controls

Read and apply `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`,
`standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md` for actual
scoped authority. Agreement on a concept/principle set does not ratify project law,
accept ADRs or authorize unlisted writes. Reuse matching named write authority;
new effects require their concrete draft/path summary and approval.

References are package-relative and shipped with this entry. Read only the
sections required by the current phase/domain, before that phase's work. A link
or previous summary is not a read. Missing, unread or truncated required material
leaves that affected step INCOMPLETE; retain the draft and report the gap.
Read long sections in bounded consecutive chunks until complete.

COMPLETE requires the approved resolved concept file to be written and Read back.
Failed writing/readback remains Incomplete; context pressure grants no write scope.
Resolve conflicting domain evidence as Unknown before domain-specific work.

## User Guide

- When to use: Guided concept ideation — from zero idea to a structured concept document. Supports both game and general product domains. Uses professional ideation techniques, user psychology frameworks, and structured creative exploration.
- Inputs: Command arguments: `/brainstorm [domain hint, or 'open'] [--review full|lean|solo]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

When this skill is invoked:

1. **Parse the argument** for an optional hint (e.g., `roguelike`, `developer tools`,
   `space survival`, `productivity`, `cozy farming`, `health tracking`).
   If `open` or no argument, start from scratch.
   Also resolve the review mode (once, store for all gate spawns this run):
   1. If `--review [full|lean|solo]` was passed → use that
   2. Else read `production/review-mode.txt` → use that value
   3. Else → default to `lean`

   See `standards/director-gates.md` for the full check pattern.

2. **Detect domain context.** The hint usually reveals the domain — game-specific hints
   (roguelike, platformer, RPG, FPS, puzzle, farming sim) suggest game mode; general
   hints (SaaS, CLI tool, developer tool, mobile app, data pipeline) suggest product
   mode. If ambiguous, ask during Phase 1. The domain choice affects which frameworks
   and terminology apply at each phase — sections below are marked
   **[通用场景]** (both domains), **[游戏专用]** (game-domain), or **[通用产品]** (product-domain).

3. **Check for existing concept work before resuming**:

Read `standards/technical-preferences.md`, existing scoped domain decisions,
and the substantive bodies of any `design/cdd/game-concept.md` and
`design/cdd/product-concept.md` before selecting a branch. Filenames, placeholder
or copied concept text and shared extensions do not establish a domain. Read
actual configured values in `Product Stack` or the populated legacy
`Language & Framework`, `Platform & Deployment`, and `Agent Routing` /
`File Extension Routing`
sections in their owning domain context; missing new sections or a concept do
not erase configured legacy Product facts. A placeholder Game concept does not
override a configured Product.

Resolve Game from consistent substantive Game concept/decision or actual
configured engine/domain and Game behavior evidence; resolve Product from
consistent substantive Product concept/decision or actual Product configuration.
Two substantive concepts, conflicting concept/configuration values or mixed scope
leave the affected branch **Unknown** until a scoped decision resolves the conflict.
With no consistent substantive concept/scoped decision or sufficient actual
configuration evidence, the domain is also Unknown; a valid concept alone can
establish the domain before stack configuration.
Record the supporting sections and values. For Unknown, use an existing matching
scoped decision or clarify with the user/configured project lead before
domain-specific delegation or writes; resolved configured facts need no new vote.
Independent neutral reads may continue. Domain selection does not waive required
branch inputs: read their actual originals and leave missing inputs Incomplete.
Never silently default to Game.

   - Resume the substantive concept matching the resolved domain and approved
     scope; a hint or filename does not relabel saved work. Read its applicable
     `game-pillars.md` or `principles.md` if present.
   - If no configured domain or substantive concept exists, use Phase 1 to obtain
     the user's domain choice before domain-specific ideation; do not resume an
     empty/copied concept as completed work. Conflicts need a scoped decision
     before resuming; preserve both originals.

4. **Run through ideation phases** interactively, asking the user questions at
   each phase. Do NOT generate everything silently — the goal is **collaborative**
   exploration** where the AI acts as a creative facilitator, not a replacement**
   for the human's vision.

   **Use `AskUserQuestion`** at key decision points:
   - Constrained preference questions (domain, scope, team size)
   - Concept selection ("Which 2-3 concepts resonate?") after presenting options
   - Direction choices ("Develop further, explore more, or prototype?")
   - Principle/pillar ranking after concepts are refined
   Write full analysis in conversation text first, then use
   `AskUserQuestion` to capture the decision with concise labels.

   Professional ideation principles to follow:
   - Withhold judgment — no idea is bad during exploration
   - Encourage unusual ideas — outside-the-box thinking sparks better concepts
   - Build on each other — "yes, and..." responses, not "but..."
   - Use constraints as creative fuel — limitations often produce the best ideas
   - Time-box each phase — keep momentum, don't over-deliberate early

---

### Phase 1: Creative Discovery

Start by understanding the person, not the project. Ask these questions
conversationally (not as a checklist).

**[通用场景]** Both domains:

**Practical constraints** (shape the sandbox before ideation).
Bundle these into a single multi-tab `AskUserQuestion` with these exact tab labels:
- Tab "Experience" — "What kind of experience do you most want to create?" Options depend on domain context:
  - **游戏专用**: Challenge & Mastery / Story & Discovery / Expression & Creativity / Relaxation & Flow
  - **通用产品**: Efficiency & Speed / Creativity & Expression / Connection & Collaboration / Insight & Understanding
- Tab "Timeline" — "What's your realistic development timeline?" (Weeks / Months / 1-2 years / Multi-year)
- Tab "Dev level" — "Where are you in your dev journey?" (First project / Shipped before / Professional background)

Use exactly these tab names — do not rename or duplicate them.

Before domain-specific discovery questions, Read the Phase 1 section for the
resolved Game or Product domain in [Domain Question Banks](references/domain-questions.md).
Use its emotional/frustration anchors and taste/usage profile conversationally;
specific game/product names remain free text.

**Synthesize** the answers into a brief — 3-5 sentences summarizing what you
learned. Read it back and confirm it captures their intent.

- **游戏专用**: Produce a **Creative Brief** — a 3-5 sentence summary of the
  person's emotional goals, taste profile, and constraints.
- **通用产品**: Produce a **Discovery Brief** — a 3-5 sentence summary of the
  person's frustration anchors, usage profile, and constraints.

---

### Phase 2: Concept Generation

Using the discovery brief as a foundation, generate **3 distinct concepts**
that each take a different creative direction.

Before generating concepts, Read Phase 2 in
[Ideation Techniques](references/ideation-techniques.md): apply Mashup plus the
resolved domain's verb/MDA or action/JTBD techniques, preserving three distinct
directions and their risks.

**[通用场景]** For each concept, present:

- **Working Title**
- **Elevator Pitch** (1-2 sentences — must pass the "10-second test")
- **Core Action** — **游戏专用**: Core Verb (single most common player action) / **通用产品**: Core Action (single most common user action)
- **Core Promise** — **游戏专用**: Core Fantasy (the emotional promise) / **通用产品**: Core Promise (the emotional/functional payoff)
- **Unique Hook** (passes the "and also" test)
- **Primary Driver** — **游戏专用**: Primary MDA Aesthetic (which emotion dominates?) / **通用产品**: Primary User Need (which user motivation dominates?)
- **Estimated Scope** (small / medium / large)
- **Why It Could Work** (1 sentence on market/audience fit)
- **Biggest Risk** (1 sentence on the hardest unanswered question)

Present all three. Then use `AskUserQuestion` to capture the selection.

**CRITICAL**: This MUST be a plain list call — no tabs, no form fields. Use exactly this structure:

```
AskUserQuestion(
  prompt: "Which concept resonates with you? You can pick one, combine elements, or ask for fresh directions.",
  options: [
    "Concept 1 — [Title]",
    "Concept 2 — [Title]",
    "Concept 3 — [Title]",
    "Combine elements across concepts",
    "Generate fresh directions"
  ]
)
```

Do NOT use a `tabs` field here. This is a plain `prompt` + `options` call.
Never pressure toward a choice — let them sit with it.

---

### Phase 3: Core Experience Design

For the chosen concept, use structured questioning to build the experience
architecture. This is the backbone — if it isn't satisfying in isolation,
no amount of features or content will save it.

**[通用场景]** Ask these as `AskUserQuestion` calls — derive the options from the
chosen concept, don't hardcode them:

1. **Core action feel** — prompt: "What's the primary feel of the core action/interaction?"
   Generate 3-4 options that fit the concept's domain and tone, plus a free-text escape.

2. **Key design dimension** — identify the most important design variable for this
   specific concept and ask about it. Generate options that match. Always include a
   free-text escape.

   - **游戏专用示例**: world reactivity, pacing, player agency, skill ceiling
   - **通用产品示例**: information density, workflow speed, collaboration depth, learning curve

After capturing answers, analyze what makes the core experience satisfying:
- **游戏专用**: Audio feedback, visual juice, timing satisfaction, tactical depth?
- **通用产品**: Responsiveness, visual clarity, feedback quality, friction removal?

Before developing the chosen experience, Read Phase 3 in
[Ideation Techniques](references/ideation-techniques.md). Cover the four Game loop
scales or four Product journey scales and autonomy, competence and relatedness
with the domain-specific questions there.

---

### Phase 4: Principles and Boundaries

**[通用场景]** Both game and product projects use non-negotiable principles to keep
decisions aligned as the project grows. Game studios call them **pillars**; product
teams call them **principles**. The structure is identical.

**[游戏专用]** Game pillars are used by real AAA studios (God of War, Hades, The Last of
Us) to keep hundreds of team members making decisions that all point the
same direction. Even for solo developers, pillars prevent scope creep and
keep the vision sharp.

**[通用产品]** Product principles are used by successful product teams (Linear,
Notion, Figma, Vercel) to keep features aligned with the core promise as
the product grows from MVP to platform. Even for solo builders, principles
prevent "wouldn't it be cool if..." features from diluting the product's
identity.

Collaboratively define **3-5 principles**:
- Each has a **name** and **one-sentence definition**
- Each has a **design test**: "If we're debating between X and Y, this principle
  says we choose __"
- Principles should feel like they create tension with each other — if all
  principles point the same way, they're not doing enough work

Real-world examples:
- **游戏专用**: God of War's "visceral combat", Hades' "every run teaches something new",
  Celeste's "tough but fair"
- **通用产品**: "Local-first: everything works offline by default", "Progressive
  disclosure: complexity is earned, not inflicted", "API stability: no breaking
  changes without a documented migration path"

Then define **3+ anti-principles** (what this project is NOT):
- Format: "We will NOT do [thing] because it would compromise [principle]"
- Anti-principles prevent scope creep — "wouldn't it be cool if..."

**Principle confirmation**: After presenting the full principle set, use `AskUserQuestion`:
- Prompt: "Do these principles feel right for your project?"
- Options: `[A] Lock these in` / `[B] Rename or reframe one` / `[C] Swap one out` / `[D] Something else`

If the user selects B, C, or D, make the revision, then use `AskUserQuestion` again:
- Prompt: "Principles updated. Ready to lock these in?"
- Options: `[A] Lock these in` / `[B] Revise another principle` / `[C] Something else`

Repeat until the user selects [A] Lock these in.

**Review mode check** — apply before spawning CD-PILLARS and AD-CONCEPT-VISUAL:
- `solo` → skip both. Proceed to Phase 5.
- `lean` → skip both (not PHASE-GATEs). Proceed to Phase 5.
- `full` → spawn as normal.

**After principles are agreed, spawn BOTH `creative-director` AND `art-director` via Task in parallel.**

- **`creative-director`** — gate **CD-PILLARS** (`standards/director-gates.md`)
  - **游戏专用**: Pass: full pillar set, anti-pillars, core fantasy, unique hook.
  - **通用产品**: Pass: full principle set, anti-principles, core promise, unique hook.
    Frame: "Review these product principles for coherence, tension, and falsifiability."

- **`art-director`** — gate **AD-CONCEPT-VISUAL** (`standards/director-gates.md`)
  - **游戏专用**: Pass: game concept elevator pitch, pillars, target platform, reference games.
  - **通用产品**: Pass: product elevator pitch, principles, target platform, reference products.
    Frame: "Propose 2-3 named visual/brand identity directions with visual rules."

Collect both verdicts, present together using a two-tab `AskUserQuestion`:
- Tab **"Principles"**: creative-director feedback. Options: `Lock in as-is` / `Revise [specific]` / `Discuss further`.
- Tab **"Visual anchor"**: art-director's 2-3 named visual directions. Options: each direction + `Combine elements` + `Describe my own`.

The user's selected visual anchor (the named direction or their custom
description) is stored as the **Visual Identity Anchor** — it will be written
into the concept document. **游戏专用**: becomes the foundation of the
**art bible**. **通用产品**: becomes the foundation for the product
**brand style guide**, `design/ux/interaction-patterns.md`, and, only for
UI-heavy products, `design/design-system.md`.

If creative-director returns CONCERNS or REJECT, resolve before visual selection.

---

### Phase 5: Audience Validation

Validate who this is actually for.

Before audience validation, Read the Phase 5 section for the resolved domain in
[Domain Question Banks](references/domain-questions.md). Validate primary/secondary
audience, exclusions and market fit; Game uses player motivations, Product uses
personas, JTBD and switching triggers.

---

### Phase 6: Scope and Feasibility

Ground the concept in reality.

**[通用场景]** Both domains:

- **MVP definition**: What's the absolute minimum build that tests the core hypothesis?
  - **游戏专用**: "Is the core loop fun?"
  - **通用产品**: "Does the core interaction solve the user's job?"
- **Biggest risks**: Technical, design, market — **通用产品 adds**: adoption risks
- **Scope tiers**: Full vision vs. what ships if time runs out

**[游戏专用]** Game-specific feasibility:

- **Target platform**: Use `AskUserQuestion` — "What platforms are you targeting for this game?"
  Options: `PC (Steam / Epic)` / `Mobile (iOS / Android)` / `Console` / `Web / Browser` / `Multiple platforms`
  Record the answer — it directly shapes the engine recommendation and will be passed to `/setup-engine`.
  Note platform implications if relevant (e.g., mobile means Unity is strongly preferred; console means Godot has limitations; web means Godot exports cleanly).
- **Engine experience**: Use `AskUserQuestion` — "Do you already have an engine you work in?"
  Options: `Godot` / `Unity` / `Unreal Engine 5` / `No preference — help me decide`
  - If they pick an engine → record it as their preference and move on. Do NOT second-guess it.
  - If "No preference" → tell them: "Run `/setup-engine` after this session — it will walk you through the full decision based on your concept and platform target." Do not make a recommendation here.
- **Art pipeline**: What's the art style and how labor-intensive is it?
- **Content scope**: Level/area count, item count, gameplay hours

**[通用产品]** Product-specific feasibility:

- **Target platform**: Use `AskUserQuestion` — "What platforms are you targeting for this product?"
  Options: `Web (browser)` / `Desktop (Windows/macOS/Linux)` / `Mobile (iOS/Android)` / `CLI / Server` / `Multiple platforms`
  Record the answer — it directly shapes the stack recommendation and will be passed to `/setup-engine`.
  Note platform implications if relevant (e.g., mobile-first means offline support and battery impact matter; web means accessibility and SEO are critical; CLI means composability and scripting matter; server means throughput and concurrency model matter).
- **Tech stack experience**: Use `AskUserQuestion` — "Do you already have a tech stack you work in?"
  Options: `Python ecosystem (Django, FastAPI, Flask)` / `JavaScript/TypeScript (React, Next.js, Node)` / `Rust` / `Go` / `No preference — help me decide`
  - If they pick a stack → record it as their preference and move on. Do NOT second-guess it.
  - If "No preference" → tell them: "Run `/setup-engine` after this session — it will walk you through the full decision based on your concept and platform target." Do not make a recommendation here.
- **Design system**: What's the visual complexity and labor intensity?
- **Feature scope**: Screen count, integration count, user personas served

**[通用场景]** Review mode checks and gates:

**Review mode check** — apply before spawning TD-FEASIBILITY:
- `solo` → skip. Note: "TD-FEASIBILITY skipped — Solo mode." Proceed directly to scope tier definition.
- `lean` → skip (not a PHASE-GATE). Note: "TD-FEASIBILITY skipped — Lean mode." Proceed directly to scope tier definition.
- `full` → spawn as normal.

**After identifying biggest technical risks, spawn `technical-director` via Task using gate TD-FEASIBILITY (`standards/director-gates.md`) before scope tiers are defined.**

- **游戏专用**: Pass core loop description, platform, engine choice, technical risks.
- **通用产品**: Pass core user journey, platform, tech stack choice, technical risks.

Present the assessment to the user. If HIGH RISK, offer to revisit scope before finalising. If CONCERNS, note them and continue.

**Review mode check** — apply before spawning PR-SCOPE:
- `solo` → skip. Note: "PR-SCOPE skipped — Solo mode." Proceed to document generation.
- `lean` → skip (not a PHASE-GATE). Note: "PR-SCOPE skipped — Lean mode." Proceed to document generation.
- `full` → spawn as normal.

**After scope tiers are defined, spawn `producer` via Task using gate PR-SCOPE (`standards/director-gates.md`).**

Pass: full vision scope, MVP definition, timeline estimate, team size.

Present the assessment to the user. If UNREALISTIC, offer to adjust the MVP definition or scope tiers before writing the document.

---

4. **Generate the concept document**.

   - **游戏专用**: Template `templates/game-concept.md` → write `design/cdd/game-concept.md`
   - **通用产品**: Template `templates/product-concept.md` → write `design/cdd/product-concept.md`

   Include a **Visual Identity Anchor** section with the selected visual direction,
   one-line visual rule, supporting principles, and design philosophy summary.

   Fill in ALL sections from the ideation conversation. **游戏专用**: including the
   MDA analysis, player motivation profile, and flow state design sections.

5. Use `AskUserQuestion` for write approval:
- Prompt: "Concept is ready. May I write it?"
- Options: `[A] Yes — write it` / `[B] Not yet — revise a section first`

If [B]: ask which section to revise using `AskUserQuestion`. **游戏专用** options: `Elevator Pitch` / `Core Fantasy & Unique Hook` / `Pillars` / `Core Loop` / `MVP Definition` / `Scope Tiers` / `Risks` / `Something else — I'll describe`. **通用产品** options: `Elevator Pitch` / `Core Promise & Unique Hook` / `Principles` / `User Journey` / `MVP Definition` / `Scope Tiers` / `Risks` / `Something else — I'll describe`.

After revising, show the updated section as a diff or clear before/after, then use `AskUserQuestion` — "Ready to write the updated concept document?"
Options: `[A] Yes — write it` / `[B] Revise another section`
Repeat until the user selects [A]. With scoped write authority, write only the
chosen domain's resolved concept path and Read it back. Report a failed write or
unreadable result as Incomplete and retain the draft in conversation. Only a
successfully saved, verified concept supports the saved-file summary and COMPLETE
verdict below; concept content approval does not grant separate legal acceptance.

**Scope consistency rule**: The "Estimated Scope" field must match the full-vision
timeline from Scope Tiers — not just "Large (9+ months)". Write as "Large (X–Y months,
solo)" or "Large (X–Y months, team of N)".

6. **Suggest next steps** using the Recommended Next Steps section below.
   Read the actual catalog before recommending the current full route; do not
   run commands, ratify laws/ADRs or advance state from a recommendation.

7. **Output a summary** with the chosen concept's elevator pitch, principles,
   primary audience, biggest risk, and file path.
   - **游戏专用**: include engine recommendation in the summary.
   - **通用产品**: include tech stack recommendation in the summary.

Verdict: **COMPLETE** — concept created and handed off for next steps.

---

## Context Window Awareness

This is a multi-phase skill. If context reaches or exceeds 70% during any phase,
report the actual persistence state:

- If the approved concept was written and Read back successfully, name its actual
  saved path: **游戏专用** `design/cdd/game-concept.md` or **通用产品**
  `design/cdd/product-concept.md`, as applicable. A fresh session can resume from it.
- If it has not been saved, or the write/read-back failed, say that the draft and
  unresolved decisions remain in conversation. Provide a compact recovery summary
  to carry into the next session; do not claim a saved file or automatically write
  one because context is low. Continue only within the existing authority.

---

## Recommended Next Steps

After a saved, read-back concept, Read `workflow/workflow-catalog.yaml` and use
its current order, required/optional flags and domain/surface conditions. Missing
or unread catalog leaves the route incomplete; the groups below are navigation,
not a substitute for its actual steps or gates. Present every applicable step
through normal entry to Game Production / Product Implementation:

1. **Concept**: `/constitute` if needed, `/design-review` on the resolved concept,
   then `/gate-check concept`. Preserve existing legal acceptance; concept
   agreement is not ratification. Optionally expand the Game visual anchor with
   `/art-bible` before CDDs, or the Product brand/style branch when applicable;
   refine pillars/principles with `creative-director` when useful.
2. **Systems Design / Specification**: `/map-systems`, `/design-system` per module,
   `/design-review` per CDD, `/review-all-gdds`, `/gate-check systems-design`.
3. **Technical Setup / Architecture**: `/setup-engine` for the engine or framework,
   `/create-architecture`, `/architecture-decision` for required choices,
   `/architecture-review`, `/create-control-manifest`, accessibility requirements
   from their actual template, `/test-setup`, `/gate-check technical-setup`.
4. **Pre-Production / Pre-Implementation**: applicable `/ux-design` and `/ux-review`
   (including Product surface/interaction requirements), `/prototype` for the core
   Game loop or Product journey, `/create-epics`, `/create-stories`, `/sprint-plan new`,
   `/story-readiness`, required `/playtest-report` validation, then
   `/gate-check pre-production`. Optional early experiments skip no boundary.

Qualify each phase with its required gate and exact evidence/acceptance scope.
Use the catalog for later phases too; suggestions never imply execution or completion.
