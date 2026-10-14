from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseMeetingIntegrationClient(ABC):
    """
    Abstract interface for enterprise video conferencing platform integration.
    Standardizes meeting management, participant webhooks, and recording extraction.
    """
    @abstractmethod
    async def create_meeting(self, title: str, schedule_time: str, **kwargs: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def end_meeting(self, meeting_id: str) -> bool:
        pass

    @abstractmethod
    async def get_participants(self, meeting_id: str) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def fetch_transcript(self, meeting_id: str) -> str:
        pass
