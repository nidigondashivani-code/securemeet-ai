from typing import Optional
from app.models.analytics import MeetingMetricSnapshot
from app.repositories.analytics_repository import AnalyticsRepository
from app.services.base import BaseService


class AnalyticsService(BaseService[MeetingMetricSnapshot, dict, dict]):
    def __init__(self, analytics_repo: AnalyticsRepository):
        super().__init__(analytics_repo)
        self.analytics_repo = analytics_repo

    async def get_overview_metrics(self, org_id: str) -> Optional[MeetingMetricSnapshot]:
        return await self.analytics_repo.get_latest_snapshot(org_id)
