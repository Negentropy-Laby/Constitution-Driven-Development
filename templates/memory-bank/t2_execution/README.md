# T2 Execution

T2 is the execution control layer. It mirrors or indexes workflow, gate,
roadmap, framework, and standards documents while leaving canonical sources in
their existing paths.

## Files

- `workflow_contract.md` — workflow catalog contract.
- `phase_checklists.md` / `gate_required_artifacts.md` — generated workflow views.
- `current_roadmap.md` — mirror of `production/project-roadmap.md`.
- `framework_contract.md` — binding of actual installed platform paths, required
  neutral inputs, sole CDD Source and project customizations; records Source and
  consumer ownership separately.
- `adapter_state.yaml` — recorded adapter freshness state. `/constitute`
  initializes it as `uninitialized`, `/constitute-check` records checks after
  approval, and `/cdd-status` reads it without taking ownership.

Do not hand-edit generated mirrors. Update `workflow/workflow-catalog.yaml`
or the owning source document, then regenerate or resync the T2 view. Never
present an uninitialized or previously recorded adapter state as a live check;
run `/constitute-check` for current installed-input observations and any available
applicable comparison. An unavailable Source/check preserves recorded state and
does not prevent authorized offline use of complete installed inputs.
