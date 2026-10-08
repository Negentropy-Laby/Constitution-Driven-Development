# Test Evidence: [Story Title]

> **Story**: `[path to story file]`
> **Story Type**: [Visual/Feel | UI]
> **Date**: [date]
> **Tester**: [who performed the test]
> **Build / Commit**: [version or git hash]

---

## What Was Tested

[One paragraph describing the feature or behaviour that was validated. Include
the acceptance criteria numbers from the story that this evidence covers.]

**Acceptance criteria covered**: [AC-1, AC-2, AC-3]

Bind actual observed Story/AC/build/config/test inputs, exact applicable scope,
runtime/platform and observer/time in the existing descriptions/Notes/conditions.
Reference recoverable original results/screenshots and the exact closure/evidence
record using Path + full SHA-256 + Bytes + CollectedAt. File existence, a PASS word
or evidence sufficiency alone does not prove execution. Record historical reuse
explicitly; unexecuted current checks remain NotRun, unavailable checks Blocked
and awaiting results/reviews Pending. Unresolved required applicability or
conflicting scope is Unknown, with its reason; it blocks dependent closure
without implying observed execution or failure. Risk acceptance is a separate record and
does not change these observed results.

---

## Acceptance Criteria Results

| # | Criterion (from story) | Result | Notes |
|---|----------------------|--------|-------|
| AC-1 | [exact criterion text] | PASS / FAIL / NotRun / Blocked / Pending / Unknown | [any observations] |
| AC-2 | [exact criterion text] | PASS / FAIL / NotRun / Blocked / Pending / Unknown | |
| AC-3 | [exact criterion text] | PASS / FAIL / NotRun / Blocked / Pending / Unknown | |

---

## Screenshots / Video

List all captured evidence below. Store files in the same directory as this
document or in `production/qa/evidence/[story-slug]/`.

| # | Filename | What It Shows | Acceptance Criterion |
|---|----------|--------------|----------------------|
| 1 | `[filename.png]` | [brief description of what is visible] | AC-1 |
| 2 | `[filename.png]` | | AC-2 |

*If video: note the timestamp and what it demonstrates.*

---

## Test Conditions

- **Game state at start**: [e.g., "fresh save, player at level 1, no items"]
- **Platform / hardware**: [e.g., "Windows 11, GTX 1080, 1080p"]
- **Framerate during test**: [e.g., "stable 60fps" or "~45fps — within budget"]
- **Any special setup required**: [e.g., "dev menu used to trigger specific state"]

---

## Observations

[Anything noteworthy that didn't cause a FAIL but should be recorded. Examples:
minor visual jitter, frame dip under load, behaviour that technically passes
but felt slightly off. These become candidates for polish work.]

- [Observation 1]
- [Observation 2]

If nothing notable: *No significant observations.*

---

## Sign-Off

Record which sign-offs the actual Story/DoD/governing owner or selected QA scope
requires, with its policy source, authority and exact applicable scope. When this
template is selected as the governing evidence owner, all three listed sign-offs
are required before COMPLETE via `/story-done`: Visual/Feel requires designer or
art-lead, UI requires UX lead or designer, alongside Developer and QA Lead.
Default optional QA orchestration does not waive that selected obligation.

Use the existing Signature cells to record Approved / Pending / Deferred with
reason, or governed N/A with its actual policy rationale. Developer self-signature
is implementation acknowledgement, not independent design/QA review. Each required
review needs the actual qualified role/observer and bound evidence; unavailable
reviewers remain incomplete, rather than assumed approved.

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Developer (implemented) | | | [ ] Approved |
| Designer / Art Lead / UX Lead | | | [ ] Approved |
| QA Lead | | | [ ] Approved |

**An unavailable sign-off can be marked "Deferred — [reason]"** if the person is
unavailable, but a required Deferred review remains Pending and blocks COMPLETE.
Resolve every required sign-off before closure; sprint review timing or separately
accepted risk cannot turn a deferred/failed/unexecuted required check into PASS.
COMPLETE or COMPLETE WITH NOTES requires all required actual PASS, evidence,
independent reviews/decisions and named closure authority; otherwise BLOCKED.
Legacy COMPLETE WITH RISKS aliases NOTES only when those facts are all eligible.

---

*Template: `templates/test-evidence.md`*
*Used for: Visual/Feel and UI story type evidence records*
*Location: `production/qa/evidence/[story-slug]-evidence.md`*
