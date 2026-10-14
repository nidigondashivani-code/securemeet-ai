from typing import List
from app.models.audit import AuditLog
from app.repositories.audit_repository import AuditRepository
from app.services.base import BaseService


class AuditService(BaseService[AuditLog, dict, dict]):
    def __init__(self, audit_repo: AuditRepository):
        super().__init__(audit_repo)
        self.audit_repo = audit_repo

    async def get_org_audit_trail(self, org_id: str, skip: int = 0, limit: int = 100) -> List[AuditLog]:
        return await self.audit_repo.get_logs_by_org(org_id, skip=skip, limit=limit)
