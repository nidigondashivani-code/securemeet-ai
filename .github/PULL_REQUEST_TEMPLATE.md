## Description
<!-- Provide a brief description of the changes introduced in this PR -->

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Refactoring (no functional change, internal architecture improvements)
- [ ] Security fix / Governance policy update
- [ ] Documentation update

## Architecture & Code Quality Checklist
- [ ] My code adheres to Clean Architecture (Controller -> Service -> Repository -> Model).
- [ ] No business logic is inside controllers or routers.
- [ ] No direct SQL/ORM queries inside routers or services (abstracted via repository).
- [ ] Added unit and integration tests covering the new functionality.
- [ ] Code passes all linting (`black`, `isort`, `flake8`, `mypy`).
- [ ] Consistent API response schemas (`ApiResponse[T]`) are utilized.
- [ ] Custom exceptions are properly mapped to HTTP status codes.
- [ ] Audit events are triggered where security-sensitive state changes occur.

## Security Considerations
- [ ] Does this PR introduce or modify authentication / authorization logic?
- [ ] Does this PR handle PII or sensitive meeting transcript data?
- [ ] Are inputs properly validated via Pydantic schemas / Zod?
