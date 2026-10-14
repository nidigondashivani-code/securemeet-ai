from typing import Optional
from app.models.ai import MeetingAISummary
from app.repositories.ai_repository import AISummaryRepository
from app.services.base import BaseService


class AIService(BaseService[MeetingAISummary, dict, dict]):
    def __init__(self, ai_repo: AISummaryRepository):
        super().__init__(ai_repo)
        self.ai_repo = ai_repo

    async def get_summary_for_meeting(self, meeting_id: str) -> Optional[MeetingAISummary]:
        return await self.ai_repo.get_by_meeting_id(meeting_id)
