# CDD Asset Ownership, Instruction Purpose and Target Submission

## Governing scope

Identify the actual governed project/product and its Source/Target role. Establish
CDD framework provenance, ownership and delivery role before classifying instruction
purpose. A directory, filename, native schema or local manifest alone establishes
neither CDD ownership nor Source authority. Review substantive content and the
complete package's required support, not only its current invocation.

Project-owned skills, agents/roles, tools, configuration, documents, source, tests
and QA/history follow their own project's rules, including development capabilities.
Development use, native `developer_instructions` fields and skill-directory placement
do not make them CDD assets. Actual project-governance decisions establish ownership;
a renamed CDD copy or a nominal package label is not evidence of a new owner.

先确认实际 CDD 框架来源、归属和交付角色，再仅在已确认的 CDD 资产集合内按用途分类。
项目自有技能、角色、工具、配置和文档按项目规则处理，不因用于开发本项目而归入 CDD。
已确认的 CDD 框架模板、投影及专属支持不进入 Target Git 跟踪、暂存、提交及交付／发布集合；
这不禁止经授权的本地保留、发现、加载、生效和使用。

Confirmed CDD framework templates, full platform projections and exclusive support
form the CDD asset collection. Apply the purpose rule within that collection across
skills, standalone roles, native instruction bodies and equivalent packages. Renaming,
tailoring or packaging a CDD template does not itself change its ownership. Shared
CDD/project content must be inspected per substantive part and support role. Unresolved
ownership leaves only the affected classification/action pending.

## Classify ownership, then task intent and the whole CDD package

| Ownership / classification | Actual purpose/content | Target submission treatment |
|---|---|---|
| Project-owned capability or document | Ownership is established under actual project governance; may support development or delivered user functions | Apply project rules; development use alone does not impose CDD local-only treatment |
| Confirmed CDD framework — Development-only | Creates, changes, reviews, verifies, releases or maintains the Target's implementation/development process | CDD template and exclusive support remain outside Target Git/delivery; retain complete required packages locally |
| Confirmed CDD framework — Product-use | Calls already delivered functions for a user task | Purpose alone does not change CDD ownership or grant Git eligibility; separately established project-owned parts follow project rules |
| Shared / mixed CDD and project content | Contains CDD template portions and project-owned portions, possibly with conditional/disabled branches or indirect references | Review actual parts and support; separate CDD framework content from eligible project candidates before submission |
| Unresolved | Provenance, owner, delivery role, body/effects or required references cannot be established | Leave affected classification/submission pending; continue independent authorized work |

Within confirmed CDD developer packages, development includes requirements/planning,
design/architecture, coding, code review, development verification/QA, release/deployment
and maintenance. Read-only developer review/orientation is included. A command named
test/release can instead call an already delivered product feature: inspect its object
and effects, not its name. Classify substantive document outputs and their generator
instructions separately by actual ownership and delivery role.

Task intent chooses the applicable use/development workflow after ownership is known.
Do not route a product-use request into CDD development merely because optional CDD
artifacts are absent. Read actual delivered features and operating instructions.
Git review still examines every branch/body/reference in a confirmed CDD package.

## Preserve CDD identity across packaging and tailoring

The following safeguards apply to confirmed CDD framework content, not independently
established project-owned development capabilities:

- Project names/paths, bespoke prompts, overlays or approved local customizations do
  not by themselves change a CDD template's ownership.
- Platform directories, native skill/agent entries, TOML role configuration and full
  projections do not turn a CDD framework instruction body into minimal adaptation.
- Local availability and exact update-write authority do not confer tracking, staging,
  commit or publication eligibility.
- References, rubrics, prompts and overlays serving only CDD framework instruction/role
  packages follow that CDD body and remain local-only in a Target. Shared project assets
  keep their actual owners; a CDD reference alone does not make them exclusive support.
- A supposedly eligible wrapper/config must not carry, reconstruct or hide excluded
  CDD framework bodies or branches. An authorized binding to a separately available
  local CDD package does not grant that package Git eligibility or disable its local use.
- Split mixed CDD/project content and dependencies substantively. Removing a heading
  or disabling a retained CDD branch does not remove the CDD content from delivery.

## Minimal adaptations and independent configuration

The Target's bounded CDD-related eligible set can contain minimal project-specific
discovery/format bindings and independent portable configuration that neither carries
nor reconstructs CDD framework procedures, role/persona bodies, prompts or exclusive
rubrics. Small size, extension or native loading alone is not evidence of independence.

Independent configuration needs actual schema/purpose/readers independent of the CDD
framework instruction/role package: product runtime, independent build/test tools or
project-owned capabilities can consume it without that package's procedures. A native
loader reading a copied CDD developer role does not make its body independent config.
Shared files need substantive independent consumers and separated CDD content.

This CDD-related restriction does not exclude independently established project-owned
development skills, native roles or their own support. Project source/tests/QA, tools,
configuration and substantive documents retain project rules. A CDD developer instruction
reading them does not change ownership or eligibility; a business-evidence reference is
not automatically an exclusive CDD rubric. Inspect actual content and consumers per file.

## Classification checklist

Before routing, import/update, candidate selection or publication review:

1. Establish the actual governed project/product and Source/Target role from governing
   instructions and substantive delivery facts; do not guess from paths.
2. Establish provenance, ownership and delivery role for each complete instruction
   package and support. Separate confirmed CDD assets, project-owned assets and
   shared/unknown portions before applying CDD purpose restrictions.
3. Name the task and actual delivered function/surface for a use claim. Inspect whether
   each effect concerns user/business data or project development. Intent alone does
   not establish ownership, Git entitlement or execution authority.
4. Read confirmed CDD skills, standalone roles/native fields, required direct/indirect
   references, conditions, overlays and wrappers to closure. Frontmatter or a sampled
   invocation is insufficient; missing required inputs leave affected CDD work pending.
5. Classify the confirmed CDD body as development-only, product-use, mixed or unresolved,
   including conditional/disabled branches. Inspect each dependency's actual owner
   and exclusive/shared support role.
6. Define a substantive split for mixed CDD/project packages; eligible project parts
   must not carry excluded CDD bodies back through wrappers or references. Independent
   config requires actual readers. Classification supplies no rewrite authority.
7. Keep complete required local CDD packages separate from eligible Git candidates and
   approved update-write paths. Native discovery/loading does not grant a CDD projection
   Git eligibility and is not prohibited by its Git exclusion.
8. Apply existing acceptance/migration/publication authority. Existing tracked confirmed
   CDD inputs need separate exact-path tracking-only reconciliation, preserving local
   inputs, customizations and history. Project-owned assets are not CDD untracking
   candidates solely because they support development. This rule alone does not
   untrack, move/delete, initialize, activate or publish.

Use the existing scoped review/adoption owner to record provenance/ownership/delivery
role, task/function, complete body/support, classification, independent-reader evidence,
eligible paths and unresolved actions. No new machine schema, manifest, lock, report
directory or Source ADR runtime reader is required.

## Examples and counterexamples

| Case | Classification/outcome | Reason |
|---|---|---|
| Project-governance-confirmed development skill or standalone native developer role | Project-owned; apply project Git rules | Developing the project does not make its own capability a CDD asset |
| Project-owned skill queries a delivered order API and exports an invoice | Project-owned product-use candidate | Actual delivered function/user task; project rules still apply |
| Delivered diagnostic test-URL or business release feature | Inspect actual ownership and feature effects | Test/release names do not imply CDD development purpose |
| Confirmed CDD skill writes project requirements/design/code or reviews developer QA | CDD development-only; local-only template | Actual framework origin plus development purpose |
| Customized CDD platform skill builds/deploys/patches the Target | CDD template remains local-only | Tailoring and full projection do not change CDD ownership |
| Overlay/rubric only serves a CDD developer template | Exclusive CDD support; local-only | Follows its confirmed CDD body, not all project development material |
| Project-owned source/tests/docs/QA read by a CDD template | Apply project rules | A reference does not transfer ownership |
| Wrapper retains a disabled CDD branch or imports its CDD prompt | Shared/mixed CDD content; split before submission | Branch flags/sidecars do not remove retained framework content |
| Project-owned code-review product used on a customer's code | Product-use candidate under project rules | Uses a delivered service rather than developing that service |
| Independent compiler/test-runner config has real readers and no copied CDD body | Independent configuration candidate | Actual schema/consumer is independent of CDD instructions |
| Runtime discovery binding points to authorized local CDD input without copying it | Minimal binding candidate | Referenced CDD package stays local-only but remains usable |
| CDD generator writes a substantive project ADR/orientation document | Classify generator and document separately | CDD template ownership does not transfer to the instantiated document |
| Confirmed CDD native role contains developer_instructions and invokes no skill | CDD developer template; local-only | Native schema and no SKILL.md dependency do not change its origin |
| Project-owned native developer role invokes no skill | Project-owned; apply project rules | Native fields and development purpose do not establish CDD ownership |
| Complete ignored CDD package and required references | Authorized local discovery/loading/use remains available | Git exclusion is not runtime loading isolation |
| Only a package name/path is readable, with no ownership/body evidence | Unresolved; affected eligibility pending | Appearance alone establishes neither CDD nor project ownership |
| CDD Source delivers developer templates and complete projections | Source framework product assets | Source role differs from Target; Source maintenance remains excluded |

## Local use, migration and governance

CDD framework assets and maintenance tools are excluded from Target Git tracking,
staging, commits and delivery/publication contents. Placement inside/outside a repository
is independent of that boundary. Git exclusion and ignore rules do not prohibit their
authorized local retention, discovery, loading, effect or use. Preserve complete required
CDD packages, references and neutral inputs at usable paths. Optional authorized local
maintenance may run; ordinary template use needs no maintenance toolkit/reader/lock,
live Source or Source ADR fetch. Missing actual required inputs leave affected CDD work
pending; a fresh Target clone may need them provisioned separately.

Ignore rules do not remove tracked/staged content or prevent forced addition or separate
publication. Confirmed tracked CDD inputs require the applicable governance gate and
separate exact-path tracking-only migration authority. Keep actual local files, required
references, customizations, recoverable before bytes and Git history. No automatic
untracking, deletion or relocation is authorized. Apply project rules to its own assets.

Review does not accept laws/ADRs, establish execution freshness, advance stages or grant
write/commit/publication effects. Apply [decision synchronization](notes-adr-sync.md)
and [evidence lifecycle](evidence-lifecycle.md). [Adapter boundaries](../adapters/README.md)
separate local closure from Git candidates; [directory roles](directory-structure.md)
record ownership/placement without making paths an ownership exception.
