# Context and Registry Presentation Formats

## Phase 2d: Context summary

Before starting design work, present a brief summary to the user:

> **Designing: [System Name]**
> - Priority: [from index] | Layer: [from index]
> - Depends on: [list, noting which have CDDs vs. undesigned]
> - Depended on by: [list, noting which have CDDs vs. undesigned]
> - Existing decisions to respect: [key constraints from dependency CDDs]
> - Pillar alignment: [which pillar(s) this system primarily serves]
> - **Known cross-system facts (from registry):**
>   - [entity_name]: [attribute]=[value], [attribute]=[value] (owned by [source CDD])
>   - [item_name]: [attribute]=[value], [attribute]=[value] (owned by [source CDD])
>   - [formula_name]: variables=[list], output=[min–max] (owned by [source CDD])
>   - [constant_name]: [value] [unit] (owned by [source CDD])
>   *(These values are locked — if this CDD needs different values, surface
>   the conflict before writing. Do not silently use different numbers.)*
>
> If no registry entries are relevant: omit the "Known cross-system facts" section.


## Phase 5b: Registry candidates

Present a summary:
```
Registry candidates from this CDD:
  NEW (not yet registered):
    - [entity_name] [entity]: [attribute]=[value], [attribute]=[value]
    - [item_name] [item]: [attribute]=[value], [attribute]=[value]
    - [formula_name] [formula]: variables=[list], output=[min–max]
   ALREADY REGISTERED (referenced_by update proposed):
    - [constant_name] [constant]: value=[N] ← matches registry ✅
```
