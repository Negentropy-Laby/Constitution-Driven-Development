# Behavior Context

## Collaboration Protocol

This project follows a **Question → Options → Decision → Draft → Approval**
pattern for all significant changes:

1. Ask clarifying questions before proposing solutions
2. Present 2-4 options with trade-offs
3. User makes the decision
4. Draft based on the decision
5. Request approval before writing

## Branching Strategy

**Primary branch:** `[main / master / develop]`

**Feature workflow:**
- Branch from: `[main]`
- Branch naming: `[feature/description / fix/description / chore/description]`
- Merge via: `[PR / direct push / rebase]`
- Delete branch after merge: `[yes / no]`

## Commit Conventions

| Type | When to use |
|------|-------------|
| `feat:` | New feature or capability |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `refactor:` | Code change that neither fixes nor adds |
| `test:` | Adding or updating tests |
| `chore:` | Build, CI, dependencies |

## Review Process

- **Who reviews:** [team lead / peer / anyone]
- **Review turnaround:** [hours / days target]
- **Required approvals:** [1 / 2]
- **Checklist:** [link to PR template or list key items]

## Workflow Rules

**Feature lifecycle:**
1. Spec written and reviewed → `[path to spec]`
2. Implementation → sources in `src/`
3. Tests pass → `[test command]`
4. Code review → at least [N] approval(s)
5. Merge → [merge strategy]

**Definition of Done:**
- [ ] Spec updated if design changed during implementation
- [ ] Tests added and passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] No new warnings or regressions

## Communication Norms

- **Where discussions happen:** [GitHub Issues / Discussions / Slack / ...]
- **Decision records:** ADRs in `docs/architecture/adr-*.md`
- **Design docs:** Specifications in `design/` or `docs/specs/`
- **Status tracking:** [sprint board / project tracker / production/sprints/]

## Conventions

- [Any naming conventions]
- [Any formatting rules (auto-formatter, linter config)]
- [Any testing conventions (test file location, naming)]
- [Any documentation conventions (docstring style, README template)]
