from typing import Dict, Any, Optional
from app.schemas.common import BaseSchema


class SettingResponse(BaseSchema):
    key: str
    value: Dict[str, Any]
    description: Optional[str] = None


class SettingUpdate(BaseSchema):
    value: Dict[str, Any]
