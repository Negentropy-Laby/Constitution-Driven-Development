# Instruction Purpose and Target Submission

## Governing scope

Identify the actual project whose product is being used or developed before
classifying an instruction package. Distinguish a CDD Target from the designated CDD Source
product/library; a directory, copied package or local manifest does not establish
that role. Classify complete instruction content and its dependency closure,
not only the command name, current invocation, author or storage path.

对于采用 CDD 的 Target，只用于开发本项目的 skill 一律视作模板，不得进入
Git 跟踪、暂存、提交或发布集合。使用型 skill 调用本项目已交付功能完成用户任务，
可按项目规则作为产品能力提交；混合型须拆开开发部分。

This covers skills, agent/role definitions, native role configuration containing
instructions and equivalent development-instruction templates with exclusive
support, regardless of filename/schema, packaging or whether they invoke a skill.
Native `developer_instructions` and persona/role bodies receive the same actual
purpose review; the field name itself neither excludes nor qualifies product-use.
此规则同样覆盖 agent/角色定义、原生配置中的指令和等价开发指令模板及专属支持，
不以调用 skill、SKILL.md 路径、TOML 格式或原生加载为条件。

It does not exclude business source code, independent build/test tools or configuration,
substantive project documents, or real business QA/history because developers use
them. Their actual project rules and delivery roles remain.

## Classify task intent, then the whole package

| Classification | Actual purpose/content | Target submission treatment |
|---|---|---|
| Product-use | Calls this project's already delivered functions for a user task, without developing this project | May be a project-owned product capability under project rules; no automatic Git or execution authority |
| Development-only | Creates, changes, reviews, verifies, releases or maintains this project's implementation/development process | A template excluded from Target Git/publication regardless of customization or packaging; retain complete required packages locally |
| Mixed | Contains product-use and development instructions, including conditional, disabled or indirect development branches | Separate development body/support from the use package; the original mixed package is not a submit-ready use instruction package |
| Unresolved | Product, delivered surface, actual effect, body or required references cannot be established | Leave affected classification/submission pending; continue independent authorized work |

Development includes requirements/planning, design/architecture, coding, code
review, development verification/QA, release preparation/deployment and maintenance
of this project. Read-only developer review/orientation is included. A command
named test/release can instead be an already delivered product feature: its
object/effect decide, not the name. A substantive project document output does not
make its generator instruction product-use; classify the document separately.

A product-use request must not be routed into CDD development simply because
optional development artifacts are absent. Read actual delivered features and
operating instructions. Intent selects the workflow; Git classification still
examines every branch/body/reference in the complete instruction package.

## No packaging or project-specific exception

- Project names/paths, bespoke prompts, internal ownership, overlays or approved
  local customizations do not change development purpose.
- Platform directories, native skill/agent entries, TOML role configuration, generated wrappers or full platform
  projections do not turn development content into minimal adaptation.
- Local availability and exact update-write authority do not confer tracking,
  staging, commit or publication eligibility.
- References, rubrics, prompt fragments and overlays serving only development
  instruction/role packages follow the body and remain local-only. Do not relabel them project config.
- A use wrapper/config must not embed, reconstruct, import or execute a hidden
  development branch as part of the supposedly product-use package. A pointer to
  a separately available optional local development package does not permit
  submitting that package; classify the wrapper's actual behavior too.
- Split mixed instructions and their dependency graph. Removing a heading or
  disabling a retained branch is not a substantive split.

## Minimal adaptations and independent configuration

Minimal required adaptation supplies runtime discovery/format or bounded bindings
to separately authorized local inputs without containing/reconstructing development
procedures, role/persona bodies, prompts or exclusive rubrics. Small size/extension,
native schema or independent runtime loading is not proof.

Independent portable project configuration has a real schema/purpose and actual
readers independent of development instructions and agent/role packages: product
runtime, independent build/test tools or qualified product-use capabilities can
consume it without those packages or their development procedures. A native loader
reading developer role instructions is not an independent configuration consumer.
A native config carrying a developer persona, prompt or instruction body remains
a development template; role-only parameters/overlays follow that same purpose.
Shared files require real independent consumers and separated
content; a nominal link cannot legalize developer instructions.

Business source/tests/QA and substantive project documents retain their own rules.
A development instruction reading them does not change their ownership or eligibility.
A reference to existing business evidence is not an exclusive skill rubric.
Inspect actual content, purpose and consumers per file.

## Classification checklist

Before routing, import/update, candidate selection or publication review:

1. Identify the actual governed project/product and Source/Target role from
   governing instructions and substantive delivery facts; do not guess from paths.
2. Name the user task and actual already delivered function/surface for any use
   claim. Identify each step's object: user/business data or this project's
   requirements/design/code/QA/release/maintenance. Inspect actual effects.
3. Read complete skills, standalone roles/agents, native instruction fields and
   required direct/indirect references, conditions,
   overlays and wrappers to closure. Frontmatter or a sampled invocation is not
   enough; missing/unread required content leaves affected classification pending.
4. Assign product-use, development-only, mixed or unresolved to the whole package,
   including conditional/disabled branches and every dependency's actual role.
5. Classify exclusive developer references/overlays with the body. For shared assets
   or independent config, identify substantive independent readers, schema/purpose
   and separated content; inspect rather than trusting a label.
6. Define a real content/dependency split for mixed packages, then review the
   resulting use package. It must not pull developer instructions back via a
   wrapper, overlay or reference. Classification grants no rewrite authority.
7. Keep complete required local development/neutral input packages separate from
   eligible Git candidates and exact approved update-write paths. Independent native
   role loading without a skill is explicitly checked. Inspect actual
   content/index; native discovery or full projection supplies no exception.
8. Apply existing acceptance/migration/publication authority. Material new choices
   need exact-scope acceptance or a valid recorded exception. Existing tracked
   developer packages require separate exact-path tracking-only reconciliation,
   preserving local inputs, customizations and history. This rule alone does not
   untrack, move/delete, initialize, activate or publish.

Use the existing scoped review/adoption owner to record actual project/task/function,
body/effects/references, classification, independent-reader evidence, eligible paths
and unresolved actions for every instruction entity. No new machine schema, manifest, lock, report directory or
Source ADR runtime reader is required.

## Examples and counterexamples

| Case | Classification/outcome | Reason |
|---|---|---|
| Query a delivered order API and export a user's invoice | Product-use candidate | Actual delivered function/user task; own project rules still apply |
| Call a shipped diagnostic service's test-URL feature on user input | Product-use candidate | Test is the product feature, not validation of this project's code |
| Invoke a shipped release feature to release a user's reserved item | Product-use candidate | Business object/effect, not the command name |
| Write this project's requirements, design or code | Development-only; local-only template | Project names/bespoke prompts do not change purpose |
| Read-only review of this project's code or developer QA evidence | Development-only; local-only template | Read-only/verification labels are not use exceptions |
| Customized platform skill builds/deploys/patches this product | Development-only; local-only template | Release/maintenance workflow; full projection grants no exception |
| JSON overlay supplies paths/prompts solely for that developer skill | Exclusive developer support; local-only | A project-specific config label is not an independent reader |
| Companion rubric/reference only drives developer review | Exclusive developer support; local-only | Follows the body regardless of path |
| Use delivered reporting, then edit this project's source | Mixed; separate before use-part submission | Product-use branch cannot legalize developer instructions |
| Use wrapper retains a disabled dev branch or imports its prompt | Mixed/development content; split required | Branch flags/sidecars do not remove retained instructions |
| Call a shipped code-review product on a customer's code | Product-use candidate | Uses the delivered service; does not develop the review product itself |
| Compiler/test-runner config has a real independent reader and no developer instruction/persona/role body | Independent configuration candidate | Actual schema/consumer works without development instruction/role packages; project rules apply |
| Runtime discovery binding to optional local developer input contains no role/persona body and does not reconstruct it | Minimal adaptation candidate | Binding does not grant the referenced package Git eligibility |
| Generate a project ADR or contributor orientation document | Skill development-only; document separate | Substantive output and its generator template are different assets |
| Business source/tests/QA contain hashes, selectors or maintenance wording | Apply actual project rules | Keywords do not make them skill templates/process pollution |
| Standalone Target TOML role has developer_instructions for this project's coding/review and invokes no skill | Development-only role; local-only template | Native schema/loading and lack of SKILL.md dependency provide no exception |
| Native role's developer_instructions only calls a delivered invoice feature for a user task, with no project development branch | Product-use agent candidate | Actual delivered function/body decides; agent/role/field names do not exclude it |
| Native config loader reads a developer persona or role-only prompt overlay | Development instructions/support; local-only | Independent of skills alone is insufficient; loader consumes a developer role package |
| Only name/frontmatter/path is readable, with no body/function evidence | Unresolved; affected submission pending | Appearance does not prove product-use |
| CDD Source delivers developer skills/roles and complete projections | Source product assets | Source role differs from Target development; Source maintenance remains excluded |

## Local use, migration and governance

Placement inside/outside a repository is independent of Git content eligibility.
Preserve complete required developer packages, references and neutral inputs at
usable paths. Ordinary authorized use of complete installed inputs needs no local
maintenance reader/lock, Source ADR fetch or live Source availability. Missing
required inputs leave the affected CDD workflow pending. A fresh Target clone may
need developer packages and neutral originals provisioned separately.

Review does not accept laws/ADRs, establish execution freshness, advance stages or
grant write/commit/publication effects. Apply [decision synchronization](notes-adr-sync.md)
and [evidence lifecycle](evidence-lifecycle.md). [Adapter boundaries](../adapters/README.md)
separate local closure from Git candidates; [directory roles](directory-structure.md)
record ownership/placement without an exception to the purpose rule.
