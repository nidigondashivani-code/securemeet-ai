from typing import Dict
from app.schemas.common import BaseSchema


class HealthCheckResponse(BaseSchema):
    status: str
    version: str
    environment: str
    services: Dict[str, str]
