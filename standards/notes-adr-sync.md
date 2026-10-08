# Notes and ADR Synchronization

This shared Game/Product standard assigns handoff, readiness, review and closure
responsibilities. It installs no watcher, hook, CI gate or automatic acceptance.
Apply the [collaboration protocol](../docs/COLLABORATIVE-DESIGN-PRINCIPLE.md) and
[evidence lifecycle](evidence-lifecycle.md) to authority/input identity.

## Scope and ownership

Review meaningful changes to choices, constraints, alternatives, consequences
and required verification in Notes, proposals, Stories, implementation or reviews.
Inspect code decisions without Notes too. Spelling/format/link-only repairs need
mechanical checks, not reopening unchanged choices. Review affected choices and
dependants, not the entire project on every edit.

Working Notes are editable working records of a question or choice: rationale,
alternatives, unresolved constraints and supporting evidence. They may be a named
section in an existing Story/proposal/review or a project-established note file;
no new Notes directory, global index or mandatory format is imposed. For example,
a Story's "Retry approach" note can compare two options and link the observed
failure while leaving the decision pending.

Notes retain their unique rationale/evidence with that owner. They do not replace
CDD requirements/detailed contracts or confer ADR acceptance. ADRs own significant
technical choices and their accepted scope/consequences; an ADR attachment is a
supporting Note only when it actually contains such working rationale. Notes and
ADRs may have many-to-many links. Keep full content with its owner.

Read governing CDDs, relevant Accepted ADRs, TR registry/control manifest and
owning Story/scoped review as applicable. Missing required inputs mean incomplete
affected checks, not fabricated TR-IDs or PASS. Optional Memory Bank absence uses
the existing workflow fallback.

## Triggers

| Trigger | Executor action | Completion condition |
|---|---|---|
| Meaningful decision batch ready for handoff | Author checks changes against requirements/exact evidence and records disposition. | Every affected choice classified; recheck changed decisions/evidence. |
| Trust boundary, public contract, durable format, state ownership or governing architectural constraint changes | Author routes the material choice through `/architecture-decision` immediately. | ADR/revision Accepted before affected implementation starts/continues, or scoped exception under existing governance. Continue independent work. |
| Story readiness | `/story-readiness` checks planned coverage. | Required ADRs Accepted; justified `cdd-layer`/`no-adr` valid. |
| Code review and Story closure | `/code-review`/`/story-done` check actual changes, freshness, coverage and actions. | No unresolved material choice approved; required updates done, permitted advisory actions have owner/due phase. |
| Epic/milestone/phase review | `/architecture-review`, `/milestone-review` or owning gate reconciles included Stories/modules. | Conflicts/unhandled choices resolved or reported with impact/owner; prior completion does not replace this check. |

## Shared disposition record

One row per decision lives in the existing Story evidence or scoped review, keyed
by Note/source path plus subject. Record summary/source, named CDD requirement
and existing TR-ID if assigned, ADR section/revision and Accepted scope or no-ADR
reason, disposition, affected paths/dependencies, source/test evidence, full input
hashes/manifest, commit plus uncommitted/ignored identities, verification time,
author/reviewer and remaining action/owner/due phase. Exceptions include scope,
authority/risks. Do not invent IDs or reuse historical approval without exact
input and authority match.

| Disposition | Meaning/action |
|---|---|
| `covered` | Accepted ADR covers exact choice/scope; cite section and verify current evidence. |
| `cdd-layer` | Named CDD owns detailed contract with no new architecture; cite owner/evidence. |
| `no-adr` | Local implementation/testing/process detail with no significant architectural choice; give reason/owner. |
| `documentation-update` | Choice unchanged, facts/references need repair. Required repairs precede closure; only permitted advisory work remains with owner/due phase. |
| `adr-required` | Significant choice lacks Accepted decision; resolve before affected implementation. |
| `conflict` | Contradicts Accepted ADR or governing requirement/law; report immediately and resolve through owner. |

Never infer `covered` from filename, `implemented` status, green tests or absent
ADR link. Unresolved required ADR/conflict blocks affected readiness/implementation/
closure; name dependencies and continue independent work. Explicit user exceptions
do not relabel Proposed ADRs Accepted or conflicts resolved.

## Updating decisions and closing evidence

Use `/architecture-decision` and `templates/architecture-decision-record.md`.
New ADRs start Proposed even when code exists. Draft writing, tests, director
recommendation and write approval do not accept ADRs. Record acceptance authority,
exact revision/date/scope separately. Changed Accepted choices need reviewed
revision/successor with preserved history/supersession.

Link supporting Notes/evidence; add reciprocal links where useful. Frozen archives
stay untouched. Do not replace entire Notes with pointers or copy full narratives
into ADRs. Update affected CDDs/TR coverage/registry/control manifest through owning
workflows within existing authority; keep paired languages consistent if maintained.

Authorized T3 pointers retain immutable revisions/exact baselines. Report-only
writes only its new report. Synchronization alone does not publish, advance phases
or complete Stories. Without Memory Bank keep disposition in existing Story/review
and disclose the absent optional index.

## Review examples

| Situation | Result |
|---|---|
| Punctuation/link repair | Mechanical check; unchanged choice not reopened. |
| CDD-owned Game tuning/Product API/CLI verification | `cdd-layer` with named owner/evidence; no manufactured ADR. |
| Shipped trust boundary with green tests | `adr-required`; affected work waits for acceptance/valid exception. |
| Missing ADR link in local helper | Classify first; justified `no-adr` can pass. |
| Archived supporting Note | Cite frozen historical scope, do not edit. |
| Completed Stories disagree on state ownership | Cross-module `conflict`; individual closure does not resolve it. |
