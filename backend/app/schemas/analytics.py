from typing import Dict, Any
from app.schemas.common import BaseSchema


class AnalyticsOverviewResponse(BaseSchema):
    total_meetings_monitored: int
    security_alerts_triggered: int
    data_leakage_prevented_count: int
    compliance_score_percentage: float
    platform_distribution: Dict[str, int]
