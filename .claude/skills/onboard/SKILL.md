---
name: onboard
description: "Generates a contextual onboarding document for a new contributor or agent joining the project. Summarizes project state, architecture, conventions, and current priorities relevant to the specified role or area."
argument-hint: "[role|area]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
model: haiku
---
Read and apply `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`,
`standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md` for scoped
authority, exact evidence and decision ownership. Existing named authority
continues; analysis is read-only and report-only excludes input/index/state writes.


## User Guide

- When to use: Generates a contextual onboarding document for a new contributor or agent joining the project. Summarizes project state, architecture, conventions, and current priorities relevant to the specified role or area.
- Inputs: Command arguments: `/onboard [role|area]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

## Purpose Routing before Contributor Onboarding

**Confirm asset ownership before instruction purpose.** Apply
`standards/skill-purpose.md` after establishing actual CDD framework provenance,
ownership and delivery role for the complete package and its required support.
Classify purpose only within that confirmed CDD asset collection. Project-owned
skills, agents/roles, tools, configuration and documents follow their project's
rules, including development capabilities; development use, native instruction
fields and skill-directory placement do not make them CDD assets. Renaming or
tailoring a CDD template does not itself change its ownership. Unresolved ownership
stays pending only for the affected action.

Confirmed CDD developer templates, full platform projections and exclusive support
remain local-only in a Target, excluded from Git tracking/staging/commits/delivery/
publication. Within that CDD collection, inspect complete bodies, conditional
branches and direct/indirect support; split mixed CDD/project content before
submission. Native `developer_instructions` fields and standalone roles receive
the same ownership review even without a skill dependency. Minimal adaptations
and independent configuration must not carry or reconstruct CDD framework
instruction bodies or exclusive support; a native loader alone does not qualify
a copied CDD role as independent configuration. This CDD-related restriction does
not exclude independently established project-owned development skills or roles.
Names/fields such as test or release do not decide ownership or purpose.

Git exclusion does not disable authorized local retention, discovery, loading,
effect or use. Preserve complete required local CDD inputs at usable paths; an
input allowlist does not grant them Git eligibility. Missing/unread required
originals leave the affected CDD workflow pending. A fresh Target clone may need
those inputs provisioned separately. Review Git candidates separately from local
inputs and update-write scope. Ordinary template use must not depend on a local
maintenance toolkit, reader, lock, live Source or Source ADR reader; optional
authorized local maintenance operations remain allowed.

Ordinary Target use requires complete installed agent/skill packages for the
selected runtime and all required local inputs. It does not require an additional
complete copy of the Source-root `agents/` or `skills/` trees. This does not waive
required originals, prohibit authorized local copies or change Git eligibility.
Source development, reproduction, generation and explicitly selected checks of
canonical originals retain their own input and authorization requirements. Resolve
consumer installation paths under `standards/directory-structure.md`, section
"Consumer layout resolution for imports and updates".

Do not submit a general CDD source mirror, template-maintenance tools/annotations,
tool-only metadata, maintenance locks/caches or actual template-maintenance output.
The designated CDD Source owns general CDD definitions independently of local
storage. Local copies alone do not establish Source authority or authorize moving,
deleting or changing log paths.

Distinguish using delivered functions from developing the actual project.
Contributor/agent orientation below is CDD framework development support; its body/
exclusive framework references/overlays stay local-only in a Target even if tailored/
native. Source delivers its templates/full projections as framework product assets.
Project-owned contributor skills, native roles and generated orientation documents
retain project rules. Product-user onboarding uses actual delivered instructions/
capabilities. Inspect shared/mixed ownership per part; split confirmed CDD content
and exclusive support from project-owned candidates before submission.

## Phase 0: Domain Routing

Read concept bodies and `standards/technical-preferences.md` domain/capability
evidence. Game keeps vision/pillars/engine/assets/playtests; Product uses user
promise/API/CLI/data/auth/architecture/workflows. Missing concepts never default
Game. Disclose Unknown/conflicts; neutral orientation continues.

## Phase 1: Load Project Context

Read actual runtime root guidance and canonical `INSTRUCTIONS.md` where available,
`standards/technical-preferences.md`, declared stage, active sprint/Story bodies
and established session context. Missing runtime copies do not imply missing
governance; disclose source gaps and retain supported partial guidance.

Read the actual selected installed role definition if a role is specified. CDD
Source may read its canonical owner; a Target reads its complete authorized local
role inputs, including ignored CDD inputs, without requiring a general CDD Source
mirror or maintenance toolkit. Project-owned roles retain project rules. This lookup
grants no import/copy or runtime-activation authority. Report missing/unknown
observations when unavailable; ignore status alone does not make a readable role
unavailable.

### Phase 1a: Establish Configuration and Freshness

Assess actual applicable configuration bodies, including populated legacy aliases,
after the reads above. **Configured** means actual applicable values are present;
a valid N/A choice is not an unset placeholder. **NotConfigured** means the
successfully read applicable configuration is explicitly unset or retains its
unconfigured choice/placeholders. Missing, inaccessible, insufficient or conflicting
configuration stays **Unknown**, with the affected gap disclosed.

Confirm a fresh project only when direct checks show NotConfigured plus reusable
root defaults without accepted project laws, substantive concepts/business source,
ADRs, sprints or active project commitments. A missing runtime root copy or optional
Memory Bank alone does not establish fresh or absent governance: use available
canonical root guidance and approved governing alternatives. An established legacy
project with usable configuration/context remains an established project. If required
governing sources are unavailable, affected orientation remains BLOCKED while
supported observations continue.

For confirmed fresh + NotConfigured, state **This project has not been configured yet** and provide minimal orientation. Recommend `/constitute` as the primary next
action after reading its complete installed entry and required references for the
actual fresh branch. Explain only that entry's actual Starting Fresh handoff and
catalog route (brainstorm, then return for principles, with stack setup when
applicable); do not invent a fixed initialize/setup/brainstorm sequence. Missing
required recommendation inputs stay disclosed and pending. This recommendation
runs no skill, initializes no governance and activates nothing.

---

## Phase 2: Scan Relevant Area

- For programmers: scan `src/` for architecture, patterns, key files
- For designers: scan `design/` for existing design documents
- [Game] For narrative: read `design/narrative/` world-building/story docs
- For QA: read actual tests/QA evidence; counts do not prove coverage/execution.
- [Product] Read relevant CDD user promises/contracts, surface profile, API/CLI/
  data/auth/workflow docs and `docs/reference/[stack]/VERSION.md`.
- [Game] Read applicable engine references, art bible/assets, pillars and playtests.
- For production: scan `production/` for current sprint and milestone

Read recent changes (git log if available) to understand current momentum.

---

## Phase 3: Generate Onboarding Document

```markdown
# Onboarding: [Role/Area]

## Project Summary
[Game vision/player experience or Product user promise/workflow; report
Configured/NotConfigured/Unknown from actual applicable configuration, observed
engine/stack values and domain. State declared phase, observed/candidate work and
verified qualification separately. For confirmed fresh + NotConfigured, say the
project has not been configured yet; disclose source gaps without inventing values.]

## Your Role
[What this role does on this project, key responsibilities, who you report to]

## Project Architecture
[Relevant architectural overview for this role]

### Key Directories
| Directory | Contents | Your Interaction |
|-----------|----------|-----------------|

### Key Files
| File | Purpose | Read Priority |
|------|---------|--------------|

## Current Standards and Conventions
[Relevant current root/standard and canonical role guidance; source metadata
is not proof of runtime model/tools/memory behavior or completed agent execution]

## Current State of Your Area
[What has been built, what is in progress, what is planned next]

## Current Sprint Context
[What the team is working on now and what is expected of this role]

## Key Dependencies
[What other roles/systems this role interacts with most]

## Common Pitfalls
[Things that trip up new contributors in this area]

## First Tasks
[Suggested first tasks to get oriented and productive]

1. [Read these documents first]
2. [Review this code/content]
3. [Start with this small task]

## Questions to Ask
[Questions the new contributor should ask to get fully oriented]
```

---

## Phase 4: Save Document

Present the onboarding document to the user.

Default output is conversational. Reuse covered exact onboarding path/effect;
if saving is requested without coverage, show draft and ask "May I write this to
`production/onboarding/onboard-[role]-[date].md`?" Write only that document.
Report-only excludes checkpoint/index/state; declined saving/review-only writes nothing.

---

## Phase 5: Next Steps

Verdict: **ONBOARDING COMPLETE** for produced orientation, disclosing omissions
and save outcome; it does not certify project/Story/runtime qualification.
Unavailable required sources leave affected orientation BLOCKED with useful
partial guidance retained; do not call the missing result complete.

For confirmed fresh + NotConfigured, the primary recommendation is `/constitute`
under Phase 1a's complete-read check; it is a recommendation, not an invocation.
For established projects, offer relevant next actions from the observed context:

- Share the onboarding doc with the new contributor before their first session.
- Use `/sprint-status` for an actual current sprint.
- Use `/help` if the contributor needs guidance on what to work on next.

Unknown configuration/freshness retains supported neutral guidance and its source
gaps; it does not become NotConfigured or trigger initialization.
