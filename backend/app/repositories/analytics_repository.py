from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.analytics import MeetingMetricSnapshot
from app.repositories.base import BaseRepository


class AnalyticsRepository(BaseRepository[MeetingMetricSnapshot, dict, dict]):
    def __init__(self, db: AsyncSession):
        super().__init__(MeetingMetricSnapshot, db)

    async def get_latest_snapshot(self, org_id: str) -> Optional[MeetingMetricSnapshot]:
        query = (
            select(MeetingMetricSnapshot)
            .where(MeetingMetricSnapshot.organization_id == org_id)
            .order_by(MeetingMetricSnapshot.created_at.desc())
        )
        result = await self.db.execute(query)
        return result.scalars().first()
