from datetime import datetime
from typing import Dict, Any
from app.schemas.common import BaseSchema


class NotificationResponse(BaseSchema):
    id: str
    user_id: str
    title: str
    content: str
    channel: str
    is_read: bool
    metadata_info: Dict[str, Any]
    created_at: datetime
