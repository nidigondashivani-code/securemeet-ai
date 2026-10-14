from datetime import datetime
from typing import Optional, Dict, Any
from app.schemas.common import BaseSchema


class OrganizationBase(BaseSchema):
    name: str
    slug: str
    is_active: bool = True
    settings: Dict[str, Any] = {}


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(BaseSchema):
    name: Optional[str] = None
    is_active: Optional[bool] = None
    settings: Optional[Dict[str, Any]] = None


class OrganizationResponse(OrganizationBase):
    id: str
    created_at: datetime
    updated_at: datetime
