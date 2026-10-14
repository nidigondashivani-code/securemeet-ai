from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseNotificationChannel(ABC):
    """Abstract interface for enterprise alerts and notification channels."""
    @abstractmethod
    async def send(self, recipient: str, title: str, message: str, metadata: Dict[str, Any]) -> bool:
        pass


class EmailNotificationChannel(BaseNotificationChannel):
    async def send(self, recipient: str, title: str, message: str, metadata: Dict[str, Any]) -> bool:
        raise NotImplementedError("Notification channel will be implemented in subsequent phase.")


class SlackNotificationChannel(BaseNotificationChannel):
    async def send(self, recipient: str, title: str, message: str, metadata: Dict[str, Any]) -> bool:
        raise NotImplementedError("Notification channel will be implemented in subsequent phase.")


class WebhookNotificationChannel(BaseNotificationChannel):
    async def send(self, recipient: str, title: str, message: str, metadata: Dict[str, Any]) -> bool:
        raise NotImplementedError("Notification channel will be implemented in subsequent phase.")
