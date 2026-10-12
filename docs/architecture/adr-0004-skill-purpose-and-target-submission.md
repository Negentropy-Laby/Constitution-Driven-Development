# ADR-0004: Instruction purpose and Target submission eligibility

## Status

Accepted — revision 2, by the CDD Source governance owner. The separate
acceptance decision and exact reviewed original are recorded below.

## Acceptance Record

- **Acceptance Authority:** CDD Source governance owner (user), separate decision
  `Sentinel_ceef6c093658819184a07249f5c536ca`, accepting the exact reviewed
  Proposed revision 2 and authorizing this Status/Acceptance Record update.
- **Accepted At:** 2026-10-12T05:49:37Z
  (2026-10-12T13:49:37+08:00).
- **Reviewed Original:** The complete pre-acceptance Proposed revision 2 of
  `docs/architecture/adr-0004-skill-purpose-and-target-submission.md`, retained
  separately as immutable acceptance evidence: **13,814 UTF-8 bytes**, SHA-256
  `6dfa3d4d9c99124722749cefdc963ffb2d9e7f8e848c1560accecdbb20d5c08e`.
  This identifies the retained Proposed original, not this Accepted successor;
  the successor's full-file identity is recorded separately, never self-hashed.
- **Accepted Scope:** The complete reviewed revision 2's architectural choice,
  consequences and migration constraints: in a CDD Target, development-only skills,
  standalone agent/role definitions, native development-instruction bodies,
  equivalent instruction templates and their exclusive support remain local-only
  and are excluded from Git tracking/staging/commit/publication. Project-specific
  names/prompts/overlays, platform directories, TOML/native loading and complete
  projections give no exception. Independent configuration requires substantive
  consumers independent of development instructions and role packages; a native
  developer-role loader does not qualify. Product-use skills/agents follow actual
  product rules; mixed content requires real separation. Business source/tests,
  substantive documents and QA retain their own eligibility. Complete required
  local inputs are preserved. Source developer templates/projections remain
  framework product assets, excluding maintenance material. This accepts the
  scoped qualification of ADR-0003 Decisions 3/4 and 5/6 described in this revision;
  ADR-0001/0002/0003 remain unchanged and no historical witness is reconstructed.
- **Effect Limits:** This accepts the Source choice and records it; it grants no
  Target migration/untracking, move/delete, config/hook activation, registry/control-
  manifest, project law/state transition or execution/QA qualification. Project
  migration and publication still require their own precise authority/evidence.
  No exception, reacceptance or predecessor supersession is granted. Source local
  batch-commit authority was separately supplied; this acceptance is not that grant.
- **Supporting Notes / Evidence:** ADR-0001/0002/0003 and
  `standards/notes-adr-sync.md` retain their existing governing scope. The independent
  review of the exact retained revision 2 closed the standalone-agent/native-role
  coverage finding and left only acceptance pending. The complete reviewed
  original, input identities, independent review and subsequent acceptance/body-
  equality validation are retained separately; raw approval/chat and review process
  records remain outside reusable templates.
- **Lifecycle Interpretation:** All sections after this record remain verbatim
  from the approved Proposed original, including its Proposed revision lineage.
  Their Proposed/pending-acceptance wording describes the review-time state;
  this Status/Acceptance Record records its later acceptance. The acceptance
  prerequisite is satisfied by the decision above; retained unchecked criteria
  do not certify migration, implementation or runtime execution. Those effects
  and their evidence remain separately governed.

## Proposed Revision Lineage

The earlier Proposed revision 1 (12,331 UTF-8 bytes, SHA-256
`afc2923550e83e40a408644f5287d096af683077bfaea1418f3eef9688384cad`)
is retained separately and was not Accepted. Revision 2 extends the entity scope
to independent agents/roles and native instruction configuration, and requires
configuration independence from developer instruction/role packages rather than
skills alone. An earlier draft identity or approval cannot accept this revision.
The complete reviewed revision 2 identity is retained outside its own hashed file.

## Date

2026-10-12 — draft authored.

## Decision Makers

The user requested the purpose standard. Exact Source governance acceptance of
this reviewed proposal remains a separate owner decision; no actor/time is guessed.

## Summary

A Target skill, standalone agent/role or native instruction body that only develops
its own project is a development template, with exclusive support/full projections.
Skills or agents using delivered product functions for user tasks can instead be
a product capability under project rules; mixed content requires real separation.

## Stack Compatibility

| Field | Value |
|---|---|
| Domain | Unknown project domain; CDD Source public governance, no configured Game/Product instance |
| Language / Runtime | No new executable language/API choice; existing mapping-parser baseline unchanged |
| Framework / Libraries | No new dependency or machine schema |
| Surface / Contract | Target instruction-purpose, local-input and Git submission public contract |
| Knowledge Risk | Runtime/native behavior Not Verified; no inferred compatibility from document checks |
| References Consulted | Source/root/docs instructions, governing standards, Accepted ADR-0001/0002/0003, T0/T2 and actual platform mapping |
| Version-Sensitive APIs / Formats | No renderer transform, native format or runtime schema changes |
| Verification Required | Whole-package purpose/effect/reference classification; independent-config/minimal-adaptation counterexamples; local closure/projections and new scope acceptance; actual consumer execution separately |

## ADR Dependencies

| Field | Value |
|---|---|
| Depends On | Recorded Accepted ADR-0001/0002 Source canonical/projection and local-use contracts; ADR-0003 revision 1's current boundary/migration/effect limits |
| Enables | After exact-scope acceptance, the additional purpose qualification in the proposed standard and synchronized entrances |
| Blocks | Adopting/publishing the additional Target instruction-eligibility constraint or migrating tracking under it before acceptance/valid exception |
| Ordering Note | Proposed scoped amendment, not replacement/reacceptance of all ADR-0003 decisions; separate project effects stay separately authorized |

## Context

ADR-0003 Accepted revision 1 is retained at **19,378 bytes**, SHA-256
`3eae138ebf8e048fc5cef5c746ddbf48def43084acd8cd2f086f947c321889fc`.
Its exact original acceptance does not cover newly rewritten decision content.
This proposal leaves that file and ADR-0001/0002 unchanged.

ADR-0003 Decision 3 allows required platform adaptations/portable project config;
Decision 4 protects substantive project-specific customizations from blanket
classification as generic originals. They do not yet explicitly exclude a
development-only instruction/role body or its exclusive project overlay called adaptation/
configuration. The new purpose axis closes that gap and adds a public governing
eligibility constraint, beyond spelling or renaming a reusable source original.

ADR-0001 Decision 2's committed complete projections remain Source product assets.
ADR-0002's complete Markdown and installed local-use contracts remain usable-input
requirements. Discovery, projection completeness and read closure do not imply a
Target Git entitlement for pure development content. Business documents, tests
and legitimate independent configuration retain their actual delivery roles.

## Decision

Subject to this proposal's exact-scope acceptance:

1. Identify the actual governed project/product and Source/Target role, then
   distinguish using its delivered functions from developing that project. Intent
   selects the workflow; Git eligibility examines the complete package.
2. In a CDD Target, skills, agent/role definitions, native role configuration
   containing instructions and equivalent templates used only to develop this
   project are excluded from Git tracking/staging/commit/publication, with their
   exclusive support. Standalone roles without any skill dependency are included.
   This covers requirements,
   design, coding, code review, development verification, release and maintenance.
   Read-only development support is included.
3. Project specificity, names/paths, custom prompts, overlays, platform directories,
   native discovery/loading, TOML schemas and full projections supply no exception.
   Developer persona/instruction fields are content, not mere config metadata. Exclusive
   development references/overlays follow the body; do not package them as
   independent configuration or minimal adaptation.
4. Product-use skills or agents call this project's delivered features for user tasks
   and may be product capabilities under project rules. Test/release names alone
   prove nothing. Split mixed/conditional development content and dependency paths
   before its use part can become a candidate. Unread/unknown content stays pending.
5. Minimal adaptations contain discovery/format/bindings without embedding or
   reconstructing development procedures. Independent portable config needs real
   schema/purpose/readers independent of development instructions and role packages;
   a native loader consuming developer_instructions is not an independent reader.
   Config must not carry or reconstruct developer role/persona/prompts. Field names
   alone do not decide purpose. Business source/tests,
   substantive documents and QA/history follow their own rules; an eligible output
   does not make its development generator skill eligible.
6. Preserve complete required local developer/neutral packages and references
   separately from Git candidates and exact update-write paths. Fresh Target clones
   may need both provisioned separately. Do not truncate packages, make maintenance
   normal-use prerequisites, or require a Target to fetch this Source ADR.
7. CDD Source delivers developer templates/full projections as its framework
   product; they remain Source-eligible. Source maintenance tools, annotations and
   process output stay excluded. A Target copy does not inherit that Source role.

### Governing scope and preserved choices

This proposes the narrower Target instruction-body/agent-role/support interpretation of ADR-0003
Decisions 3/4 and candidate separation in Decisions 5/6. It does not supersede its
other choices, change Source renderer ownership/transforms/modes, reaccept prior
ADRs or reconstruct missing historical D7/D8 evidence. Local writes are not
Accepted status or an exception.

`standards/skill-purpose.md` owns the actual rule, integrated into root instructions,
T0/constitute, T2, directory/adapter norms, adoption/audit/routing/onboarding and
update/acceptance guidance. Reusable entries carry general purpose rules, not
this proposal's status, raw chat/process reports or a Source ADR runtime dependency.

## Alternatives Considered

- Allow project-specific/projected developer skills: rejected; packaging and
  tailoring do not change developing the Target itself.
- Exclude all skills/files used during development: rejected; product-use skills,
  Source product templates, business code/tests/docs and independent config differ.
- Judge names/frontmatter/current invocation: rejected; mixed, conditional and
  indirect developer procedures would bypass whole-package review.

## Consequences

Purpose governs eligibility despite packaging. Consumers review complete
instructions/dependencies and separately provision developer packages missing from
Git clones. Real splits of mixed packages add work; hidden developer branches or
nominal independent readers do not suffice. No business behavior, native metadata,
hook wiring or machine schema changes are proposed.

## Risks and Verification

| Risk | Required check |
|---|---|
| Standalone developer agent/native instructions bypass skill-only checks | Classify every role/persona/native instruction body even without a skill; native loading/schema is no exception |
| Bespoke developer overlays launder excluded procedures | Read actual bodies/exclusive consumers; no name/path/config exception |
| Product-use commands named test/release wrongly excluded | Identify delivered function, business object/task and effects |
| Shared business source/tests/docs discarded because a dev skill reads them | Verify actual independent roles/readers; classify outputs apart from generators |
| Disabled branches/imported prompts retained in use wrappers | Require substantive content/dependency separation before submission |
| Local completeness confused with Git completeness | Preserve full installed packages/read closure; inspect Git candidates separately |
| Local writing mistaken for acceptance/migration | Keep new scope Proposed; require exact owner acceptance and separate effects |

## Migration Plan

1. Read-only classify exact Target packages, delivered features/tasks, complete
   body/reference/overlay effects, shared assets and independent config consumers.
2. Preserve local originals, complete required closure, customizations, before
   bytes and Git history. Reconciliation remains pending under the unaccepted new
   rule; do not retroactively declare prior tracking compliant or violated.
3. Close this new scope with exact reviewed-original acceptance or a valid actual
   separately authorized recorded exception. Old ADR-0003 approval cannot accept
   this new content; no exception is supplied here.
4. Separately obtain precise project authority for exact instruction/role/support paths,
   tracking-only index effects, needed precise ignores and mixed-content splits.
   Preserve actual required inputs, project assets and history.
5. Review resulting candidates/index/reference closure. Commit/publication, state
   changes and actual runtime/QA qualification require their own authority/evidence.

No Target migration, untracking, deletion, relocation, config activation, registry
write, commit/push/merge or project state transition is performed here.

## Validation Criteria

- [ ] Exact reviewed Proposed revision accepted by actual governance owner, with
  retained full original/SHA-256/size, scope and real time, or valid exception.
- [ ] Whole-package classification covers skills, standalone agents/roles, native
  instruction fields/overlays, independent-loader cases and all development phases, bespoke
  overlays/full projections, exclusive/shared references and unknown/mixed branches.
- [ ] Genuine product-use agent and skill/test/release cases, independent build/test config and business
  documents/QA are distinct from development instruction/role bodies.
- [ ] Canonical/full changed-package projections obey actual Accepted mappings;
  normal local use retains complete inputs without maintenance/Source ADR readers.
- [ ] Future tracking migration has separately authorized exact paths/effects,
  local closure/history retention and actual before/after candidate review.
- [ ] Runtime/loading/QA/release claims have actual separate execution evidence;
  static instruction review does not qualify them.

## CDD Requirements Addressed

Foundational Source template-use governance; no allocated project TR/Epic/Story
or configured Game/Product CDD instance. No new Foundation qualification, law
ratification or stage completion is fabricated for a consumer.

## Related

- [ADR-0001](adr-0001-generated-runtime-adapters.md): Source projection ownership.
- [ADR-0002](adr-0002-runtime-parity-and-adapter-governance.md): complete local use,
  mixed roots and retained historical-evidence limits.
- [ADR-0003](adr-0003-target-local-inputs-and-git-eligibility.md): exact Accepted
  predecessor unchanged; new scoped qualification proposed here.
- [Skill purpose](../../standards/skill-purpose.md), [adapter norms](../../adapters/README.md)
  and [directory roles](../../standards/directory-structure.md).
- [Decision synchronization](../../standards/notes-adr-sync.md) and
  [evidence lifecycle](../../standards/evidence-lifecycle.md).
