from fastapi import APIRouter, Depends, status
from app.api.deps import get_health_service
from app.schemas.common import ApiResponse
from app.schemas.health import HealthCheckResponse
from app.services.health_service import HealthService

router = APIRouter(prefix="/health", tags=["Health Check"])


@router.get("", response_model=ApiResponse[HealthCheckResponse], status_code=status.HTTP_200_OK)
async def check_health(
    health_service: HealthService = Depends(get_health_service),
) -> ApiResponse[HealthCheckResponse]:
    """Liveness and readiness health probe endpoint."""
    health_status = await health_service.check_health()
    return ApiResponse(message="System operational", data=health_status)
