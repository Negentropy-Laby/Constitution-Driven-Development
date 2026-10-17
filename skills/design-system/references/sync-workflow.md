# Existing-Document Synchronization

**Detect synchronization mode:** `/design-system sync <scope>` reconciles
implementation-first changes with existing CDDs as one bounded batch. Existing
module/`retrofit`/CDD-path invocations remain supported. Resolve the user's scope
to actual paths/effects before writing: implementation inputs, affected CDD
sections, Notes/ADRs, registry/traceability/module-index effects if authorized,
exclusions, writer and required independent reviewer.

1. Collect a fixed source commit and exact committed/staged/unstaged diffs plus
   full hashes/sizes/original-path identities for untracked, ignored and external
   relied-on inputs. A commit or `HEAD` alone is not the working-tree baseline.
   Retain recoverable before/after bytes for changed documents and evidence.
2. Read affected source, tests, governing CDDs, Accepted ADRs and their required
   indirect attachments to the minimum closure. Record unresolved or unknown
   paths without writing them. Do not read sensitive settings for discovery.
3. Map actual bodies to the resolved document kind's owner set in
   `design/INSTRUCTIONS.md` (semantic eight for module CDDs), including existing aliases. Separate As-Is behavior from Target requirements; show
   mismatches and evidence. Preserve unaffected content and original Game examples.
4. Classify decisions under `standards/notes-adr-sync.md`. Resolve material
   `adr-required`/`conflict` choices before affected implementation proceeds;
   documentation synchronization does not accept an ADR.
5. Show concrete old/new sections and the complete named path/effect list when
   approval is missing. Continue within existing approved batch scope; ask only
   unresolved material choices/new effects. Apply incremental edits; never
   replace existing files with new skeletons.
6. Read back exact resulting bytes and required closure. Record author self-checks
   separately from independent review. Bind a non-writing reviewer's required
   semantic review to the exact manifest/inputs; any repair changes the baseline
   and requires fresh review of affected inputs. Missing required review stays
   incomplete. Batch completion reports written paths, findings, dispositions,
   verification limits and remaining owners; no implicit Story/phase/publication
   completion or index/session updates.


After these steps, report the batch result and return from the skill.
