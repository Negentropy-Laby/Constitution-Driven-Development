# Tech Context

## Technology Stack

| Layer | Choice | Version | Rationale |
|-------|--------|---------|-----------|
| **Language** | [Python / TypeScript / Rust / Go / ...] | [version] | [why] |
| **Framework** | [FastAPI / React / Tauri / ...] | [version] | [why] |
| **Database** | [PostgreSQL / SQLite / DuckDB / ...] | [version] | [why] |
| **Platform** | [Web / Desktop / Mobile / CLI / Server] | — | [why] |
| **Build System** | [pip / npm / cargo / make / ...] | — | — |
| **CI/CD** | [GitHub Actions / GitLab CI / ...] | — | — |

## Performance Budgets

| Metric | Target | Measurement |
|--------|--------|-------------|
| **API latency** | [ms] | p95 |
| **Memory** | [MB/GB] | peak RSS |
| **Throughput** | [req/s or ops/s] | sustained |
| **Startup time** | [s] | cold start |
| **Build time** | [s] | clean build |

## External Dependencies

| Dependency | Purpose | Version | Risk if unavailable |
|------------|---------|---------|---------------------|
| [name] | [what it does] | [version] | [impact / mitigation] |
| [name] | [what it does] | [version] | [impact / mitigation] |

## Development Environment

- **OS:** [Windows / macOS / Linux — all three?]
- **Shell:** [bash / PowerShell / zsh]
- **Required tools:** [list — Node.js, Python, Docker, etc.]
- **Setup command:** `[one command to get started]`

## Constraints

- [Any regulatory, compliance, or organizational constraints]
- [Any license restrictions on dependencies]
- [Any deployment environment constraints (air-gapped, specific cloud, etc.)]
