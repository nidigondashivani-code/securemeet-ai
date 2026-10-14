from typing import List
from app.models.notification import Notification
from app.repositories.notification_repository import NotificationRepository
from app.services.base import BaseService


class NotificationService(BaseService[Notification, dict, dict]):
    def __init__(self, notification_repo: NotificationRepository):
        super().__init__(notification_repo)
        self.notification_repo = notification_repo

    async def get_user_alerts(self, user_id: str, unread_only: bool = False) -> List[Notification]:
        return await self.notification_repo.get_user_notifications(user_id, unread_only=unread_only)
