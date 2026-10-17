# Retrofit an Existing Module CDD

**Detect retrofit mode (dispatcher selected retrofit only):**
If the argument starts with `retrofit` or the argument is a file path to an
existing `.md` file in `design/cdd/`, enter **retrofit mode**:

1. Read the existing CDD file.
2. Verify from workflow/provenance and the full body that the existing target
   is a **module CDD** under `design/INSTRUCTIONS.md`'s kind routing before any
   retrofit edit. For Concept, Module Index, Quick Spec or another non-module
   kind, report its actual owner route (/brainstorm, /map-systems, /quick-design
   or the resolved owner), show legal module retrofit usage and return without
   edits. Unknown kind requests clarification, never defaults to Module8.
   For a verified Game/Product module, map its substantive bodies to the semantic
   eight roles, retaining existing headings/aliases. The separate sync batch
   route may handle multiple kinds through their own resolved owner sets.
3. Identify missing/placeholder/unresolved roles through actual content and
   required evidence, not heading presence or single-line/length heuristics.
4. Present to the user before doing anything:
   ```
   ## Retrofit: [System Name]
   File: design/cdd/[filename].md

   Sections already written (preserved unless explicitly in the requested update):
   ✓ [section name]
   ✓ [section name]

   Missing or incomplete sections (will be authored):
   ✗ [section name] — missing
   ✗ [section name] — placeholder only
   ```
5. If authority is absent, show the named missing/selected sections and ask:
   "May I fill these gaps or revise these selected sections at [path]?" Reuse
   existing scope; preserve all other content.
6. Within approved scope, proceed to **Phase 2**; skip the existing-file
   skeleton in **Phase 3** and author only named missing/incomplete or explicitly
   selected substantive sections in **Phase 4**.
7. Preserve existing section content outside the authorized change. Fill
   placeholders or edit specifically approved substantive sections in place;
   never recreate a retrofit file as a skeleton.
