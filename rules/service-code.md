---
paths:
  - "src/services/**"
  - "src/jobs/**"
  - "src/workers/**"
---

# Product Service Code Rules
Apply to actual matching capabilities in Game or Product; the title does not make
a shared path Product-only. Read `standards/technical-preferences.md` for domain/
capability evidence and `standards/notes-adr-sync.md` for decision disposition.


- Service boundaries must be explicit: inputs, outputs, side effects, retries, timeouts, and ownership.
- External calls must use dependency injection or adapters so tests can isolate network, database, queue, and filesystem behavior.
- Retried operations must be idempotent or document why duplication is impossible.
- Actual background jobs define scheduling, concurrency, cancellation, backoff
  and observability; dead-letter applies where a queue supports it. Record
  justified N/A for absent capabilities without fictitious infrastructure.
- Log enough context for support and incident response without logging secrets or sensitive user data.
- Partial failure behavior must be documented in the CDD and covered by tests.
- Before using framework, queue, database, or cloud APIs, consult `docs/reference/<stack>/` for the pinned version.
