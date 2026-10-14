from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.exceptions.handlers import register_exception_handlers
from app.middleware.audit_middleware import AuditLoggingMiddleware
from app.middleware.request_id import RequestContextMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Application startup: configure structured logging & connection pools
    setup_logging()
    yield
    # Application shutdown: close resource pools


def create_application() -> FastAPI:
    """FastAPI application factory with Clean Architecture and middleware stacks."""
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # 1. Register Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestContextMiddleware)
    app.add_middleware(AuditLoggingMiddleware)

    # 2. Register Custom Global Exception Handlers
    register_exception_handlers(app)

    # 3. Mount API Routers
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # 4. Prometheus Metrics Instrumentator
    Instrumentator().instrument(app).expose(app, endpoint="/metrics")

    return app


app = create_application()
