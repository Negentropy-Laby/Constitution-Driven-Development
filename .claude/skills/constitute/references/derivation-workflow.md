# Constitution Derivation Workflow

## Phase 4: Auto-Derivation Workflow (from existing artifacts)

### Step 4a: Read Source Artifacts Silently

Read all available artifacts. Build a complete picture.

### Step 4b: Extract and Present Section by Section

For each constitutional element, extract from the best available source:

| Element | Primary Source | Fallback |
|---------|---------------|----------|
| Core thesis | Concept doc → elevator pitch | — |
| Principles | Concept doc → pillars/principles | — |
| Anti-thesis | Concept doc → anti-pillars/anti-principles | — |
| Domain | Concept doc content | Ask user |
| Tech context | technical-preferences.md | Concept doc platform section |
| System patterns | ADRs → architecture decisions | — |
| Behavior context | CDDs → implicit conventions | — |

Present each section with `AskUserQuestion`:
- **Prompt**: "[Section name] derived from your project."
- **Options**:
  - `Approve — write as-is`
  - `Edit — I want to refine this`
  - `Skip this section`

### Step 4c: Write Approved Sections

Include the reusable source/target boundary section in the law-index draft
submitted for approval. Its inclusion does not make it an already-approved
source-derived law or ratify new project laws. Write each approved section to
the appropriate `memory_bank/` file immediately.
Create directories as needed. All newly derived laws start as `Status: Proposed`.
Concept/content approval and permission to write the law index do not accept laws.
Independently verify any existing law-acceptance authority against the exact
presented text/revision, Support IDs and scope before recording `Accepted`;
retain the matching authority/date/evidence and preserve prior history.
When that authority is absent or does not match, keep the laws Proposed and use
Phase 3e to present the exact law set for explicit ratification. Reuse verified
matching ratification authority without asking again; missing acceptance stays
pending, never inferred from concept approval or a successful file write.

Also create the T0-T3 memory-bank control plane skeleton listed in Phase 3e.1.
For derived projects, populate `document_map.yaml`, `current_state.md`,
`workflow_contract.md`, and T1 index files from the source artifacts when
evidence exists; otherwise leave template placeholders with clear `missing` or
`not started` status.

### Step 4d: Alignment Report (if CDDs or ADRs exist)

Generate:
```
## Constitution Alignment Report
Constitution Version: [actual version and Draft/ratified status]

### Principles
✓ [Law 1]: [name] — supported by ADR-0001, ADR-0003
⚠ [Law 2]: [name] — no ADR coverage found
⚠ [Law 3]: [name] — CDD [module].md may conflict

### Gaps
1. [gap + suggested fix]

Overall: ALIGNED / NEEDS ATTENTION
```

### Step 4e: Write Version and Sign-Off

Write the actual version/status to `active_context.md`: use version 0.1 (Draft)
while initial derived laws remain Proposed; version 1.0 requires the separately
verified ratification above. Append the derivation source entry:
`Initial constitution derived from concept doc and [N] CDDs / [M] ADRs`.
Record content/write approval separately from exact law-acceptance sign-off.
Only a verified ratification records its actual authority, scope and date; do not
manufacture sign-off or reuse a concept approval as the acceptance record.

### Step 4f: Review Mode and Stage-Aware Handoff

Report whether the constitution is a Proposed draft or a ratified law set.
Then set review mode within its write authority and route to the correct next
phase based on the detected stage. A draft does not satisfy a gate requiring
Accepted laws.

**Review Mode**: Check `production/review-mode.txt`. If not set, use
`AskUserQuestion`: Full / Lean (recommended) / Solo. Write choice.

**Stage-aware handoff** — the next steps differ by stage:

| Stage | Detected Artifacts | Next Steps |
|-------|-------------------|------------|
| **1. Concept** | Concept doc exists, module index missing | `/design-review` on concept → `/gate-check concept` → `/map-systems` |
| **2a. Mapped** | Module index exists, MVP CDDs incomplete | `/map-systems next` or `/design-system [module]` → `/design-review` |
| **2b. Designed** | Module index + MVP CDDs exist | `/review-all-gdds` → `/gate-check systems-design` → `/setup-engine` |
| **3. Architected** | ADRs exist | `/gate-check` to validate current phase. Next incomplete phase from pipeline. |
| **4a. Source only** | Source code exists, no production artifacts | "You have source code but no production tracking. Run `/project-stage-detect` to assess your current phase, or `/gate-check` if you know where you are." |
| **4b. Implemented** | Source + production artifacts exist | `/gate-check` to validate current phase. Next incomplete phase from pipeline. |

Show the full pipeline from Phase 7 for context, then use `AskUserQuestion`:
- **Prompt**: "Constitution established. Which step would you like to start with?"
- **Options**: 3-4 concrete next steps from the stage-appropriate list above.
  Include `Something else — I'll tell you`.

When confirmed: "Type `[skill command]` to begin."

---
