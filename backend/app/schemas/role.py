from datetime import datetime
from typing import List, Optional
from app.schemas.common import BaseSchema


class RoleBase(BaseSchema):
    name: str
    description: Optional[str] = None
    permissions: List[str] = []


class RoleCreate(RoleBase):
    pass


class RoleUpdate(BaseSchema):
    description: Optional[str] = None
    permissions: Optional[List[str]] = None


class RoleResponse(RoleBase):
    id: str
    created_at: datetime
    updated_at: datetime
