from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from app.schemas.common import BaseSchema


class UserBase(BaseSchema):
    email: EmailStr
    full_name: str
    is_active: bool = True
    organization_id: Optional[str] = None
    role_id: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseSchema):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    role_id: Optional[str] = None


class UserResponse(UserBase):
    id: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime
