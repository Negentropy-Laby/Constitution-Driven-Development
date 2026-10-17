# Architecture Finding Formats

## Phase 4: Dependency-order display

5. **Output recommended implementation order**:
   ```
   ### Recommended ADR Implementation Order (topologically sorted)
   Foundation (no dependencies):
     1. ADR-0001: [title]
     2. ADR-0003: [title]
   Depends on Foundation:
     3. ADR-0002: [title] (requires ADR-0001)
     4. ADR-0005: [title] (requires ADR-0003)
   Feature layer:
     5. ADR-0004: [title] (requires ADR-0002, ADR-0005)
   ```

## Phase 4: Conflicts

For each conflict found:

```
## Conflict: [ADR-NNNN] vs [ADR-MMMM]
Type: [Data ownership / Integration / Performance / Dependency / Pattern / State]
ADR-NNNN claims: [...]
ADR-MMMM claims: [...]
Impact: [What breaks if both are implemented as written]
Resolution options:
  1. [Option A]
  2. [Option B]
```


## Phase 5: Technology audit

Output format:
```
### Technology Audit Results
Technology: [name + version]
ADRs with Technology Compatibility section: X / Y total

Deprecated API References:
  - ADR-0002: uses [deprecated API] — deprecated since [version]

Stale Version References:
  - ADR-0001: written for [older version] — current project version is [version]

Post-Cutoff API Conflicts:
  - ADR-0004 and ADR-0007 both use [API] with incompatible assumptions
```

## Phase 5b: CDD revision flags

For each conflict found, record it in the CDD Revision Flags table:

```
### CDD Revision Flags (Architecture → Design Feedback)
These CDD assumptions conflict with verified technology behaviour or accepted ADRs.
The CDD should be revised before its module enters implementation.

| CDD | Assumption | Reality (from ADR/technology-reference) | Action |
|-----|-----------|--------------------------------------|--------|
| reporting.md | "Run large exports in the request/response path" | Framework request timeout is capped — ADR-0003 | Revise CDD |
```
