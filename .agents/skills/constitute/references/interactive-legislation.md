# Interactive Legislation and Handoff

## Phase 3: Interactive Legislation (from scratch)

This phase is entered when the user wants to define a constitution manually
with no concept doc to derive from.

### Phase 3a: Domain + Core Thesis

**Domain question — only ask if not already established.** If the user arrived
from Stage 0 (Question 1 was already answered) or the domain was detected from
a concept doc, skip this. Only ask when entering Phase 3 from Stage 1 "Start
from scratch" where no domain context exists.

If domain is unknown, use `AskUserQuestion`:
- **Prompt**: "What kind of project is this?"
- **Options**:
  - `A game` — 2D/3D interactive experience (any genre, any engine)
  - `A general product` — web app, CLI tool, API, library, mobile app, data pipeline

Record the domain. Then: "We'll start with one sentence: **what is this project, and what is it NOT?**"

Guide the user to produce: Project Name, Core Thesis (BL-01), Anti-Thesis.

Present the draft. Once approved, write `memory_bank/t0_core/active_context.md`
with `Constitution Version: 0.1 (Draft)`.

### Phase 3b: Core Principles (3-5)

"Now the most important part: the **non-negotiable principles** that govern
every decision."

Explain the criteria: 3-5 max, must be falsifiable, must create tension, must
apply to all aspects, each needs a design test.

Use `AskUserQuestion` to present draft principles. Each law gets:
- Support ID (BL-02 through BL-06)
- Status: `Proposed`
- The principle statement
- Current-state requirement
- A design test

Include the reusable source/target boundary section in the draft. Once approved,
write `memory_bank/t0_core/basic_law_index.md`. Keep that fixed section separate
from the numbered laws; all new project laws start as `Status: Proposed`.

### Phase 3c: Technology & Constraints

Ask for broad technology preferences. Detailed configuration is deferred to
`/setup-engine`. Write `memory_bank/t1_axioms/tech_context.md`,
`system_patterns.md`, `behavior_context.md` at a high level.

### Phase 3d: Review Mode

Check `production/review-mode.txt`. If not set, use `AskUserQuestion`:
Full / Lean (recommended) / Solo. Write choice to file.

### Phase 3e: Ratification

Before finalizing, present the complete constitution for ratification:

```
## Constitution Ratification
Version: 1.0
All laws are currently Status: Proposed.

To take effect, they must be ratified (Status: Accepted).
```

Use `AskUserQuestion`:
- **Prompt**: "The constitution is drafted. Ratify it?"
- **Options**:
  - `Ratify — all laws become Accepted` — Write version 1.0 with all laws Accepted. Record sign-off.
  - `Revise first` — I want to edit before ratifying.
  - `Leave as Draft` — Write as version 0.1 (Draft). Ratify later.

If "Ratify": update all law statuses to `Accepted ([date])`.
Write version 1.0 to `active_context.md` with changelog entry and sign-off.
Write `memory_bank/README.md`.


### Phase 3f: Handoff After Interactive Legislation

Constitution written from scratch. Now route to the correct next step.
This is the handoff for Path C "Formalize first" — the user has a clear spec
but no concept doc yet. Note this explicitly:

> "Your constitution is established. Your concept isn't yet formalized as a
> document. Run `/brainstorm [your spec]` to produce `design/cdd/game-concept.md`
> (or `product-concept.md`) — it will validate your principles against a
> structured concept. Then return to `/constitute` to update."

This is a unique state: constitution exists, but no concept doc. Stage 1a
assumes a concept doc already exists, so do NOT use Stage 1a routing here.
Instead, route directly to `/brainstorm`:

- Phase 3d Review Mode (if not already set from Phase 3d)
- Handoff: "Type `/brainstorm [your spec]` to begin."
- After `/brainstorm` completes, return to `/constitute`. It will detect the
  existing constitution AND the new concept doc, and offer to update via
  Stage 5 → `Revise from source` (Phase 6 amendment workflow). The revision
  will compare the new concept doc against the existing principles and
  propose amendments for any changes.

---
