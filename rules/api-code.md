---
paths:
  - "src/api/**"
---

# Product API Code Rules
Apply to actual matching capabilities in Game or Product; the title does not make
a shared path Product-only. Read `standards/technical-preferences.md` for domain/
capability evidence and `standards/notes-adr-sync.md` for decision disposition.


- Public endpoints must have documented request, response, error, auth, and compatibility behavior.
- Schema changes must be versioned or explicitly marked backward-compatible.
- Validate all external input at the boundary; do not rely on downstream code to reject invalid data.
- Error responses must be stable and testable: status code, error code, message shape, and retry semantics.
- Do not leak secrets, internal stack traces, database identifiers, or implementation-only fields.
- Endpoint contract/integration evidence covers success, validation failure and
  relevant edge cases. Auth failures apply to actual auth boundaries; an
  unauthenticated public endpoint records its governing rationale. Absent
  execution is not PASS and does not justify inventing credentials.
- Breaking changes require release notes, migration guidance and governing CDD/
  Accepted ADR or justified local disposition; a link alone is not acceptance.
- Before using framework or SDK APIs, consult `docs/reference/<stack>/` for the pinned version.
