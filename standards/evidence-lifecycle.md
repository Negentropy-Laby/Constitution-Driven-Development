# Evidence Lifecycle

This cross-project standard governs CDD review, validation, handoff and closure
evidence for Game and Product. It defines executor responsibilities; it does
not certify tools, install enforcement, create project laws/published generations,
or activate `memory_bank/`.

## Authority and review modes

Apply the user's scoped authorization and
[collaboration protocol](../docs/COLLABORATIVE-DESIGN-PRINCIPLE.md). Content
agreement, file-write authority, independent review, ADR acceptance, publication
and completion are separate facts. Checks or saved reports grant none of the others.

Existing authorization persists across roles, files, retries and recovery within
its paths/effects/limits. Record original instruction/approval reference, actor/
authority, scope, exclusions and pending decisions. Ask again only for material
new effects. Historical approval applies only to exact matching input identity
and relevant authority/scope; otherwise retain it as history.

- **Read-only/review-only:** parsing, scanning, rendering to conversation and
  validation never invoke publication, resealing, repair or any write entrypoint,
  including in-memory calls. No status, index or pointer updates.
- **Report-only:** write one new assigned report when authorized; inputs, status,
  indexes and pointers require separately authorized actions.
- **Repair/implementation:** an authorized writer may repair scoped inputs but
  cannot label self-checks independent. Changes require a fresh baseline and any
  independent review required by the selected workflow.

For review-only and report-only validation, inspect the actual public caller,
arguments/mode and receiver before running helpers. Non-dry-run target
validation that invokes a writer, or a constructor/factory that enters a
publication/repair path, crosses this boundary even when its receiver is
an in-memory list. Trace the actual branch/call result; merely constructing
or passing a receiver does not prove its invocation. No disk change does
not prove that no writer ran.
Creating an inert observer/spy or obtaining a bound method without invoking
it is not a writer invocation; an authorized dry-run may verify zero calls.
Any unexpected callback invocation remains a scope breach. Apply these
limits to delegated roles as well as the parent, and inspect their actual
tools/results before claiming the boundary held.

Record `full`/`lean`/`solo` mode and required/completed/skipped/unavailable gates.
Skipped gates do not establish approval or independence. Review requirements
follow the selected workflow; this document adds no unconditional routine gate.

## Identity and preservation

Working records are editable. Published revisions preserve immutable original
bytes. A formal generation is a validated, explicitly published set of revisions;
editing, checking, rendering, reviewing and failed publication do not create one.

Each relied-on input/object records stable record/revision ID, original path,
complete SHA-256 (64 hex characters), byte size, source commit when available,
and collection time with timezone. Uncommitted, ignored, external and indirectly
referenced inputs need their own identities; a commit alone does not identify
them. Observe mtime separately; it does not prove creation, authorship or absence
of intervening writes.

Retain recoverable original bytes in the set or verified immutable storage.
A digest, mutable path, file list or identity record alone cannot recover content.
Classify actual retention as `preserved`, `identity-only` or `missing`. Never
manufacture missing originals, historical IDs, approvals or dates. Exact
reconstruction requires retained bytes matching the full original digest;
describe approximate reconstruction separately.

### Minimum evidence closure

Declare scope/exclusions and retain the smallest complete dependency set that
supports the claim: relied-on records and required direct/indirect attachments,
manifests, decision sources and test inputs. Follow required references to closure;
do not collect the entire workspace by default.

Resolve each required original path relative to its actual owner and directly
attempt to read its body. Record that exact attempt to distinguish absent, unread,
inaccessible and unverified inputs. Ignore-aware listings, extension filters,
`rg --files` and Glob omissions do not establish absence.

Read and bind an existing ignored attachment's complete raw bytes. An access
failure leaves the affected claim incomplete; state the observed limitation
without manufacturing a replacement or reporting the original absent.

Reconcile delegated read results before finalizing closure findings. A verified
successful read remains present even if a parent's filtered listing omits it.
When a delegated read cannot be verified, directly read the original or retain
the affected claim as unverified.

For attachments retained elsewhere record an **original-path witness**: original
path/URI, collection time, full digest, byte size, immutable revision/storage
location and resolvable owner link. Verify existence, exact identity and recoverable
bytes. A renamed copy without this witness, rolling `latest` field, array position
or unchecked link is not a historical address. Report inaccessible dependencies;
narrow the claim or mark affected checks incomplete.

Keep a manifest digest outside its own hashed dependency set. Independent reports
bind exact input manifests/revisions. Publish later reviews separately, including
them only in later sets if needed; never rewrite a reviewed set to include its
own review or introduce self-referential hash cycles.

### Evidence record metadata

This section owns the record extensions used by evidence, review, closure and
skill-testing indexes. Keep existing table columns/keys compatible and retain full
reports with their original owners; an index links records rather than duplicating
their narratives.

Each new/revised source's companion metadata records:

- Stable record/revision ID, original path and recoverable original-byte location.
- Complete SHA-256 and byte size; input-manifest path and full digest; source
  commit plus identities for relied-on uncommitted/ignored inputs.
- Collection/verification time with timezone, scope/exclusions and reading omissions.
- Author/reviewer, independence and the distinct write, acceptance, publication
  and completion authority facts.
- Decision disposition, requirement/ADR owner and section, and remaining
  action/owner/due phase under `standards/notes-adr-sync.md`.

Apply the identity/closure rules above and the authority rules in this standard.
Authorized current-pointer changes retain immutable historical revisions and
their exact approval scope. A mutable pointer establishes neither acceptance nor
completion. Absent Memory Bank uses the existing owning Story/report fallback.

## Publication and corrections

Formal publication needs explicit authority and a tool that preserves the prior
set and pointer on failure. Record unique ID, predecessor, scope/exclusions,
sources, rule/generator identity, revisions, original paths, full digests, sizes
and publication time separately from collection.

Resolve an exact already-successful predecessor/scope/content/rule/generator
match before checking predecessor freshness: return its existing ID without
changing the current pointer. Incidental timestamps do not create content.
New publications reject stale predecessors, concurrency, duplicate-ID collisions
and incomplete sets; never overwrite existing sets. Failed attempts may have
separately authorized incident records.

Corrections are new revisions/errata identifying original and reason; preserve
originals. Mutable indexes may update current pointers with authority while
retaining historical revisions and approval scope. An index is not immutable
evidence or completion proof.

Adapter `--write` regenerates declared adapters; it is not formal publication,
decision acceptance or project-memory update. Tools lacking these guarantees
may produce working artifacts/check results but must not claim formal generations.

## Independent verification and claims

Report byte integrity, structural consistency, semantic correctness, reading
coverage, runtime execution, independent verification, approval and completion
separately. Equal hashes establish equality at compared collections, not absence
of intervening writes. Keywords, line counts, last-line quotations and link
presence do not prove full reading or behavior. Static reasoning is not runtime
evidence. Disclose omissions/environment limits; increased reading alone is not FAIL.

Trace behavioral findings through the actual public caller, data flow and
governing contract. Determine effective arguments after parsing, explicit
forwarding and overrides. A helper's default affects behavior only when that
call path leaves the argument unspecified. Bind the finding to the observed
branch/result and retain separate failures separately.

Record author/checker/reviewer and their actions. Independent reviewers inspect
exact bound inputs without repair or treating authors' conclusions as evidence.
Input edits make the role a writer; preserve earlier findings and obtain a fresh
baseline for required independent review. Keep valid partial findings and block
only work depending on unresolved issues.

Write counterexamples and restore checks run on isolated copies without connection
to source/formal evidence paths. Main-module guards, environment flags and CLI
confirmation prevent mistakes, not establish actor authority or isolation.

## Removal, restore and storage claims

Do not delete referenced originals. Permanent deletion needs independent explicit
authority for the exact object list, resolved paths, identities, affected references
and preservation outcome. Editing, regeneration, archival, named-candidate cleanup
or pointer replacement does not authorize sweeping unknown objects/erasing history.

Restore into an isolated destination first; verify exact bytes and required
closure. Production restore/overwrite needs its own scoped authority. Never
test destructive behavior against originals.

Distinguish logical bytes from allocated physical storage, path entries from
object identity and different volumes. Hard links, deduplication, sparse/
compressed files, copies and cross-volume moves may change those measures.
Count logical bytes per declared set; claim allocated/reclaimed bytes only with
a measured method and volume. Removing a path does not prove object/storage removal.

## Incidents and fallback

On unauthorized writes, missing originals or mismatches stop affected publication/
closure, preserve available originals and report observed/recovered/retained facts
separately. Resume within authorized remediation after preservation/rechecking;
continue unaffected independent work.

Detailed artifacts stay in established paths. Initialized projects may index
authorized results in T3; templates remain reusable. Without `memory_bank/` use
the existing Story/report/conversation fallback, disclose the absent optional
index and do not initialize it as a side effect.
