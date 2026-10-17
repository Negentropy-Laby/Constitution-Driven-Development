# Product Test Evidence by Story Type

**[通用产品]** Product evidence table:

Resolve automated evidence from the Story's exact paths and actual configured test
roots, naming and runner discovery, including tests outside `tests/`. Read required
originals and verify matching actual PASS results for the named ACs and inputs.
Conventional directories are discovery examples, not prerequisites. A missing
required original remains visible; fallback discovery does not waive it or erase
a failure. Where the owning workflow permits an alternate location, reconcile
that exact path with its owner before closure and verify the same required checks.

| Story Type | Required Evidence | Gate Level |
|---|---|---|
| **API** | Contract test at the exact Story-bound configured path — must exist and pass | BLOCKING |
| **CLI** | Smoke command output in `production/qa/evidence/smoke/` — `--help` + core command | ADVISORY |
| **Data/Migration** | Migration test against fresh instance at the exact Story-bound configured path — must exist and pass | BLOCKING |
| **Auth/Permission** | Permission test at the exact Story-bound configured path — must exist and pass | BLOCKING |
| **Workflow** | Integration test at the exact Story-bound configured path — must exist and pass | BLOCKING |
| **UI** | Walkthrough doc OR screenshot in `production/qa/evidence/` | ADVISORY |
| **Integration** | Integration test OR API contract test OR documented playtest, as selected by the AC/DoD owner | BLOCKING |
| **Ops/Deployment** | Deployment smoke in `production/qa/smoke-*.md` | BLOCKING |
| **Config** | Config validation test OR smoke check | ADVISORY |

**Product evidence checks:**

- **API**: read the Story's exact Test Evidence path first, then search actual
  configured roots/discovered paths for contract tests covering its endpoint,
  schema and TR-ID (`tests/api/` is an example). Verify actual matching PASS;
  missing required evidence or incomplete required checks are **BLOCKING**.
- **CLI**: check `production/qa/evidence/smoke/`, `production/qa/evidence/manual/`, or
  `production/qa/smoke-*.md` for command output covering `--help` and the core
  command path. If none found, flag **ADVISORY**.
- **Data/Migration**: read the exact Test Evidence path first, then search
  actual configured roots/discovered paths for migration or fresh-instance tests
  (`tests/integration/` is an example). Verify actual matching PASS; missing
  required evidence or incomplete required checks are **BLOCKING**.
- **Auth/Permission**: first read the Story's exact Test Evidence files and
  actual test configuration. Verify the configured runner discovers those files,
  that their behavioral assertions cover the required role, token and access
  boundaries (including required allow/deny and invalid/expired cases), and that
  matching actual execution passes. Search actual configured roots/discovered
  paths for additional candidates only as needed; `tests/unit/auth/` and
  `tests/api/` are conventional examples. Missing required evidence, failed tests
  or incomplete required boundary coverage/execution remain **BLOCKING**.
- **Workflow**: read the exact Test Evidence path first, then search actual
  configured roots/discovered paths for required workflow coverage
  (`tests/integration/[module]/` is an example). Verify actual matching PASS;
  missing required evidence or incomplete required checks are **BLOCKING**.
- **UI**: check `production/qa/evidence/` for walkthrough or screenshot evidence,
  or an interaction test named in the story. If none found, flag **ADVISORY**.
- **Integration**: read the AC/DoD owner's selected method and exact Test Evidence
  paths first. For integration or API contract tests, search actual configured
  roots/discovered paths for required service, webhook, queue or contract
  coverage (`tests/integration/` and `tests/api/` are examples). For a documented
  playtest (Product user/workflow session), read the original record and verify
  observer, steps, exact build/input identity, time, actual results and required
  sign-offs against every required AC, including required retry/timeout/error
  cases. Preserve explicitly sourced stricter automated or combined obligations;
  manual evidence cannot replace those required tests. Verify actual matching
  PASS for the selected method; missing required evidence or incomplete required
  checks remain **BLOCKING**.
For Ops/Deployment, resolve the actual conventional smoke report, confirmed CI evidence or exact Story-named deployment artifact used by this review. Read its original source and verify the required matching PASS deployment evidence; no route bypasses that requirement. Unresolved source selection remains Unknown.

- **Ops/Deployment**: check for `production/qa/smoke-*.md`, CI evidence, or a
  deployment smoke artifact named in the story. If none found, flag **BLOCKING**.
- **Config**: check for a config validation test, smoke report, or evidence doc
  covering the changed environment variable, feature flag, or setting. If none
  found, flag **ADVISORY**.
