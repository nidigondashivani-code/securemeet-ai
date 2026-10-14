from datetime import datetime
from typing import Optional, Dict, Any
from app.schemas.common import BaseSchema


class SecurityPolicyBase(BaseSchema):
    organization_id: str
    name: str
    description: Optional[str] = None
    is_active: bool = True
    rules: Dict[str, Any] = {}


class SecurityPolicyCreate(SecurityPolicyBase):
    pass


class SecurityPolicyUpdate(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    rules: Optional[Dict[str, Any]] = None


class SecurityPolicyResponse(SecurityPolicyBase):
    id: str
    created_at: datetime
    updated_at: datetime


class SecurityIncidentResponse(BaseSchema):
    id: str
    meeting_id: str
    organization_id: str
    severity: str
    incident_type: str
    description: str
    remediation_status: str
    created_at: datetime
