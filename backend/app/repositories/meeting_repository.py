from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.meeting import Meeting
from app.repositories.base import BaseRepository
from app.schemas.meeting import MeetingCreate, MeetingUpdate


class MeetingRepository(BaseRepository[Meeting, MeetingCreate, MeetingUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Meeting, db)

    async def get_by_organization(self, org_id: str, skip: int = 0, limit: int = 50) -> List[Meeting]:
        query = (
            select(Meeting)
            .where(Meeting.organization_id == org_id)
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(query)
        return list(result.scalars().all())
