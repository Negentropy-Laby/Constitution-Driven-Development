# T2 Execution

T2 is the execution control layer. It mirrors or indexes workflow, gate,
roadmap, framework, and standards documents while leaving canonical sources in
their existing paths.

## Files

- `workflow_contract.md` — workflow catalog contract.
- `phase_checklists.md` / `gate_required_artifacts.md` — generated workflow views.
- `current_roadmap.md` — mirror of `production/project-roadmap.md`.
- `framework_contract.md` — index of the canonical -> generated adapter contract
  (manifest, generator, runtimes, generated outputs, mixed-ownership roots).
- `adapter_state.yaml` — reserved adapter generation freshness state; the
  template remains uninitialized until lifecycle automation is implemented.

Do not hand-edit generated mirrors. Update `workflow/workflow-catalog.yaml`
or the owning source document, then regenerate or resync the T2 view.
Lifecycle automation for `framework_contract.md` and `adapter_state.yaml` is not
yet wired into `/constitute` or `/constitute-check`. Maintainers own these files
until that follow-up lands; do not present an uninitialized state as fresh.
