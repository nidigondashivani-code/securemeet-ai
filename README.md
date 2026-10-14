# SecureMeet AI

> **AI-Powered Enterprise Meeting Security & Governance Platform**
> Integrates natively with Google Meet, Zoom, and Microsoft Teams to deliver real-time DLP, participant authentication, automated PII redaction, and compliance auditing.

---

## 🏛 System Architecture Overview

SecureMeet AI is designed with **Clean Architecture** to ensure testability, high maintainability, and loose coupling:

```
frontend/                 # React 18, TypeScript, Vite, Tailwind CSS, Redux Toolkit, React Query
backend/                  # Python 3.13, FastAPI, SQLAlchemy 2.0 Async, Celery, Redis, PostgreSQL
docs/                     # Architectural specs, contributing guides, security documentation
infrastructure/           # Nginx reverse proxy and deployment configs
docker/                   # Docker Compose manifests and entrypoints
scripts/                  # Environment bootstrap, linting, and automated test scripts
tests/                    # Pytest unit and integration test suites
.github/                  # CI/CD Workflows (Lint, Typecheck, Test, Build)
```

---

## 🚀 Quick Start

### 1. Clone & Configure
```bash
git clone <repo-url>
cd multiplatform_app
cp .env.example .env
```

### 2. Launch with Docker Compose
```bash
docker compose up -d --build
```

- **Frontend Console**: [http://localhost:3000](http://localhost:3000)
- **FastAPI OpenAPI Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Probe**: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)

---

## 📋 Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React 18, TypeScript, Vite, Tailwind CSS, React Router v6, Redux Toolkit, Axios, React Query |
| **Backend API** | Python 3.13, FastAPI (Async), SQLAlchemy 2.0 (Async), Alembic, Pydantic v2 |
| **Data & Cache** | PostgreSQL 16 (AsyncPG), Redis 7 (aioredis) |
| **Async Tasks** | Celery 5.4 with Redis Broker |
| **Security & Auth** | JWT (RS256/HS256), Refresh Tokens, RBAC, OAuth2, Passlib/Bcrypt |
| **Integrations** | Google Meet API, Zoom API / Webhooks, Microsoft Teams Graph API |
| **Infra & DevOps** | Docker, Docker Compose, Nginx 1.27, GitHub Actions |

---

## 📖 Documentation Links

- [Detailed Architecture Specification](docs/Architecture.md)
- [Environment Setup Instructions](docs/Environment-Setup.md)
- [Contributing Guidelines & Git Workflow](docs/Contributing.md)
