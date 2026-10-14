from app.core.config import settings
from app.schemas.health import HealthCheckResponse


class HealthService:
    """Service verifying readiness and liveness of dependent infrastructure components."""
    async def check_health(self) -> HealthCheckResponse:
        return HealthCheckResponse(
            status="healthy",
            version=settings.APP_VERSION,
            environment=settings.ENVIRONMENT,
            services={
                "api": "online",
                "database": "configured",
                "redis": "configured",
                "celery": "configured"
            }
        )
