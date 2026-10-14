from datetime import datetime
from typing import Optional, Dict, Any
from app.schemas.common import BaseSchema


class AuditLogResponse(BaseSchema):
    id: str
    action: str
    actor_id: Optional[str] = None
    organization_id: Optional[str] = None
    resource_type: str
    resource_id: Optional[str] = None
    ip_address: Optional[str] = None
    payload: Dict[str, Any]
    created_at: datetime
