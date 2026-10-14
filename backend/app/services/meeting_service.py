from typing import List, Optional
from app.models.meeting import Meeting
from app.repositories.meeting_repository import MeetingRepository
from app.schemas.meeting import MeetingCreate, MeetingUpdate
from app.services.base import BaseService


class MeetingService(BaseService[Meeting, MeetingCreate, MeetingUpdate]):
    def __init__(self, meeting_repo: MeetingRepository):
        super().__init__(meeting_repo)
        self.meeting_repo = meeting_repo

    async def get_org_meetings(self, org_id: str, skip: int = 0, limit: int = 50) -> List[Meeting]:
        return await self.meeting_repo.get_by_organization(org_id, skip=skip, limit=limit)
