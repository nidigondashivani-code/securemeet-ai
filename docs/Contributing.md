# Contributing to SecureMeet AI

Thank you for contributing to SecureMeet AI. To ensure enterprise software excellence, all engineers must adhere to the following standards.

---

## 1. Development Principles

- **SOLID & Clean Architecture**: Keep layers decoupled. Do NOT write SQL in routers or services.
- **Async First**: All FastAPI endpoints and database transactions must be asynchronous (`async def`, `await session.execute(...)`).
- **Strict Typing**: Type annotations are mandatory across backend (`mypy --strict`) and frontend (`tsc --noEmit`).
- **Consistent Responses**: Always return `ApiResponse[T]` envelopes from endpoints.
- **Test-Driven Reliability**: Every bug fix or feature must include unit and integration tests.

---

## 2. Git Branch Strategy

We follow a **Trunk-Based / Gitflow Hybrid** optimized for continuous integration and high-security releases:

| Branch Name | Purpose | Protection Rules |
| :--- | :--- | :--- |
| `main` | Production-ready code | Requires 2 senior approvals, signed commits, passing CI |
| `develop` | Integration branch for staging releases | Requires 1 approval, passing CI |
| `feature/<module>-<short-description>` | New feature development | Merged to `develop` via PR |
| `fix/<issue-id>-<short-description>` | Bug fixes | Merged to `develop` via PR |
| `hotfix/<version>` | Production emergency patches | Branched from `main`, merged to `main` & `develop` |
| `release/<version>` | Release hardening and QA validation | Merged to `main` and tagged |

---

## 3. Commit Message Conventions (Conventional Commits)

Commit messages must follow the [Conventional Commits v1.0.0](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <short description in present tense>

[optional body explaining motivation and context]

[optional footer(s) like Closes #123, BREAKING CHANGE: ...]
```

### Allowed Types:
- `feat`: A new feature (e.g., `feat(security): add screen share DLP rule evaluator`)
- `fix`: A bug fix (e.g., `fix(auth): correct refresh token expiry calculation`)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `docs`: Documentation only changes
- `chore`: Changes to build process, dependency updates, tooling
- `perf`: A code change that improves performance
- `ci`: CI/CD configuration files and scripts changes

---

## 4. Pre-Commit Quality Gates

Run quality verification before pushing:

```bash
# Formatter & Linter check
./scripts/lint.sh

# Run test suite
./scripts/test.sh
```
