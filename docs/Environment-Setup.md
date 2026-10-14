# Environment Setup Guide

Follow this guide to get the **SecureMeet AI** development stack running on your local machine.

---

## Prerequisites

1. **Python 3.13+** installed and available in your PATH.
2. **Node.js 20+** and `npm` installed.
3. **Docker** and **Docker Compose** installed and daemon running.
4. **Git** configured.

---

## 1. Automated Setup

### Linux / macOS
```bash
chmod +x scripts/*.sh
./scripts/setup.sh
```

### Windows (PowerShell)
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\setup.ps1
```

---

## 2. Docker Compose (Full Stack)

To run the entire ecosystem (Frontend, Backend, Postgres, Redis, Celery, Nginx) in Docker:

```bash
# 1. Create your local environment file
cp .env.example .env

# 2. Boot up all containers
docker compose up -d --build

# 3. View service status
docker compose ps

# 4. View logs
docker compose logs -f backend
```

Services will be accessible at:
- **Web App**: http://localhost:3000
- **FastAPI Docs (Swagger UI)**: http://localhost:8000/docs
- **API ReDoc**: http://localhost:8000/redoc
- **Nginx Gateway**: http://localhost:80
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

---

## 3. Manual Local Development (Without Full Docker)

If you prefer to run Postgres & Redis in Docker and execute backend/frontend on the host:

```bash
# Run databases only
docker compose up -d postgres redis

# Terminal 1: Backend
cd backend
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm run dev
```
