from datetime import datetime
from typing import Optional, Dict, Any
from app.schemas.common import BaseSchema


class MeetingBase(BaseSchema):
    title: str
    platform: str
    external_meeting_id: str
    host_id: str
    organization_id: str
    scheduled_start: datetime
    scheduled_end: datetime
    status: str = "SCHEDULED"
    security_metadata: Dict[str, Any] = {}


class MeetingCreate(MeetingBase):
    pass


class MeetingUpdate(BaseSchema):
    title: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    status: Optional[str] = None
    security_metadata: Optional[Dict[str, Any]] = None


class MeetingResponse(MeetingBase):
    id: str
    created_at: datetime
    updated_at: datetime
