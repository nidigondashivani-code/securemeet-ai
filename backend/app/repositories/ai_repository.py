from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.ai import MeetingAISummary
from app.repositories.base import BaseRepository


class AISummaryRepository(BaseRepository[MeetingAISummary, dict, dict]):
    def __init__(self, db: AsyncSession):
        super().__init__(MeetingAISummary, db)

    async def get_by_meeting_id(self, meeting_id: str) -> Optional[MeetingAISummary]:
        query = select(MeetingAISummary).where(MeetingAISummary.meeting_id == meeting_id)
        result = await self.db.execute(query)
        return result.scalars().first()
