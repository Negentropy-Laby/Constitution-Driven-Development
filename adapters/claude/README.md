# Claude Adapter

This directory documents Claude Code adapter boundaries.

Common CDD assets live in neutral roots such as `workflow/`, `templates/`,
`standards/`, and `skill_testing/`. Canonical skills, agents, hooks, and root
instructions live in `skills/`, `agents/`, `hooks/`, and `INSTRUCTIONS.md`.

The `.claude/` directory is runtime-facing: settings, hooks, rules, agents,
skills, and small compatibility pointers needed by Claude Code. The
`.claude/skills/`, `.claude/agents/`, `.claude/hooks/`, `.claude/rules/`, and
`CLAUDE.md` files are generated from the canonical roots in the designated Source.
Source changes use separately supplied authorized rendering; do not hand-edit
generated copies. An installed target reads its reviewed platform files directly,
retains project differences and does not need a local maintenance kit. Per-directory
nested guidance also generates `CLAUDE.md` siblings under `src/`, `design/`, and `docs/`.

These developer templates and complete projections are CDD Source framework product
assets. A Target copy keeps its CDD ownership and does not gain Source authority.
Apply `standards/skill-purpose.md` after establishing actual provenance, ownership
and delivery role; project-owned runtime skills, roles, tools, configuration and
documents retain project rules, including their development use.

**Confirm asset ownership before instruction purpose.** First establish actual CDD
framework provenance, ownership and delivery role for the complete package and its
required support. Apply instruction-purpose classification only within that confirmed
CDD asset collection. Project-owned skills, agents/roles, tools, configuration and
documents follow their project's rules; development use, native instruction fields
and skill-directory placement do not make them CDD assets. Renaming or tailoring a
CDD template does not itself change its ownership. Unresolved ownership stays pending.

**Target Git separation preserves authorized local use.** CDD framework assets and
maintenance tools are excluded from Target Git tracking, staging, commits and delivery/
publication contents. This does not prohibit their authorized local retention,
discovery, loading, effect or use. Keep complete required inputs at usable paths.
Ordinary template use must not depend on the local maintenance toolkit. Ignore and
runtime loading are separate; existing tracked content requires separately authorized,
recoverable tracking-only migration that leaves local files and required references intact.

Within confirmed CDD packages, independent portable configuration must neither carry
nor reconstruct CDD instruction bodies or exclusive support, and must have substantive
readers independent of those packages. A native loader alone does not qualify.

Keep canonical CDD workflow catalogs, document templates, shared standards and
skill testing specs in their declared neutral roots when preparing Source projections.
This Source layout does not prohibit authorized local Target copies or project-owned
assets in runtime directories.
