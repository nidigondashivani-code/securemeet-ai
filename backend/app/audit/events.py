from typing import Any, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.core.constants import AuditActionType


class AuditEventPayload(BaseModel):
    action: AuditActionType
    actor_id: Optional[str] = None
    organization_id: Optional[str] = None
    resource_type: str
    resource_id: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    status: str = "SUCCESS"
    details: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AuditServiceTracker:
    """Async logger for compliance-grade tamper-evident audit logs."""
    async def record_event(self, event: AuditEventPayload) -> None:
        raise NotImplementedError("Audit logging service will be implemented in subsequent phase.")
