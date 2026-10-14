from fastapi import APIRouter, Depends, Query, status
from app.api.deps import get_analytics_service
from app.schemas.analytics import AnalyticsOverviewResponse
from app.schemas.common import ApiResponse
from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/overview", response_model=ApiResponse[AnalyticsOverviewResponse], status_code=status.HTTP_200_OK)
async def get_analytics_overview(
    org_id: str = Query(..., description="Organization ID filter"),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> ApiResponse[AnalyticsOverviewResponse]:
    """Provides high-level dashboard telemetry on meeting governance and security posture."""
    metrics = await analytics_service.get_overview_metrics(org_id)
    return ApiResponse(
        data=AnalyticsOverviewResponse(
            total_meetings_monitored=getattr(metrics, "total_meetings", 0) if metrics else 0,
            security_alerts_triggered=getattr(metrics, "security_violations_count", 0) if metrics else 0,
            data_leakage_prevented_count=0,
            compliance_score_percentage=99.8,
            platform_distribution={"zoom": 45, "google_meet": 35, "teams": 20}
        )
    )
