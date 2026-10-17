# Constitution Amendment Workflow

## Phase 6: Amendment Workflow

This is the formal process for changing an existing constitution.

### Step 6a: Determine Amendment Trigger

Amendments are triggered when:
- User selects "Amend constitution" (Stage 5)
- User selects "Revise from source" (Stage 5)
- Concept document has changed (Stage 3-4 with existing constitution)
- `/constitute-check` flags stale principles
- User explicitly requests amendment

### Step 6b: Load and Compare

1. Read current constitution (`basic_law_index.md` + `active_context.md`)
2. Read changed source artifacts (concept doc, CDDs, ADRs — whatever triggered this)
3. Compute what changed:
   - **New content in concept doc** → candidate new principles
   - **Changed content in concept doc** → candidate principle amendments
   - **Removed content in concept doc** → candidate principle deprecation
   - **New CDDs** → principles may need scope expansion
   - **New ADRs** → may formalize previously implicit principles

### Step 6c: Present Amendment Proposal

Present the proposed changes as a structured diff:

```
## Proposed Constitutional Amendment
Current Version: 1.2
Proposed Version: 1.3

### Changed Principles
Law 2 (BL-03): "API-first design" → "API-first design with OpenAPI spec"
  Reason: concept doc now specifies OpenAPI requirement
  Impact: ADR-0005 (API framework choice) needs review
  Status: Accepted → Accepted (amended)

### New Principles
Law 6 (BL-08): "Observability by default" — all services must expose metrics
  Source: derived from new CDD monitoring-module.md
  Design test: if choosing between a logging library and a metrics library, this
    principle says choose the one that provides both structured logs AND metrics
  Status: Proposed

### Deprecated Principles
Law 4 (BL-05): "Monolith-first" → Superseded by Law 6
  Reason: project has grown beyond monolith scale; observability requires
    service-level instrumentation
  Status: Accepted → Superseded by BL-08

### Principles Unchanged
Law 1 (BL-02): [name] — no change
Law 3 (BL-04): [name] — no change
Law 5 (BL-07): [name] — no change
```

### Step 6d: User Review Each Change

Present each changed/new/deprecated principle's exact draft and Support ID.
Verify separate authority to accept/amend/supersede that precise law revision;
content agreement or permission to write alone leaves acceptance pending.
The following choice requests that explicit law action, separately from its
file-write scope. Reuse matching existing authority when verified.
Present each principle individually using `AskUserQuestion`:
- **Prompt**: "Amendment: [change description]. Approve this change?"
- **Options**:
  - `Approve — apply this amendment`
  - `Revise — I want to edit this amendment`
  - `Reject — keep the current version for this principle`

### Step 6e: Write Amended Constitution

Only apply accepted-law status changes when Step 6d verified the exact legal
action and the file-write effects are covered; otherwise retain a Proposed
amendment without altering the binding prior law.

1. Update `basic_law_index.md`:
   - Changed laws: update text, keep Support ID, set Status to `Accepted (amended [date])`
   - New laws: add with new Support ID, Status `Accepted ([date])`
   - Deprecated laws: set Status to `Superseded by BL-XX ([date])` or `Deprecated ([date])`
2. Bump version in `active_context.md`
3. Append changelog entry
4. Record sign-off
5. Update `memory_bank/t0_core/amendment_log.md`
6. Write `memory_bank/t3_archive/amendments/amendment-v[version]-[YYYY-MM-DD].md`
   as the detailed amendment evidence. If the same filename exists, use
   `amendment-v[version]-[YYYY-MM-DD]-[NN].md` and do not overwrite history.

The T3 amendment evidence must include: version, date, trigger, changed
principles, rationale, rejected alternatives, approval/sign-off, impacted T1/T2/T3 files, and follow-up checks.

### Step 6f: Changelog and Sign-Off

Append to `active_context.md`:

```
## Constitution Changelog
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.2 | 2026-05-01 | [user] + AI | Amended Law 2 (BL-03): API-first → API-first with OpenAPI. Added Law 6 (BL-08): Observability by default. Superseded Law 4 (BL-05) → BL-08. |

## Amendment Sign-Off
This amendment was approved on 2026-05-01.
Changes reviewed and accepted:
  - BL-03: amended (API-first with OpenAPI spec)
  - BL-05: superseded by BL-08
  - BL-08: added as Accepted
Amendment session: /constitute (triggered by concept doc update)
```

### Step 6g: Impact Warnings

After writing, flag any downstream impacts:

> "Amendment complete. The following artifacts may need review:
> - ADR-0005: references Law 2 — verify the amended principle is still compatible
> - monitoring-module.md: new CDD — run `/design-review` to validate"

---
