from typing import List
from app.models.security import SecurityPolicy
from app.repositories.security_repository import SecurityPolicyRepository
from app.schemas.security import SecurityPolicyCreate, SecurityPolicyUpdate
from app.services.base import BaseService


class SecurityService(BaseService[SecurityPolicy, SecurityPolicyCreate, SecurityPolicyUpdate]):
    def __init__(self, security_repo: SecurityPolicyRepository):
        super().__init__(security_repo)
        self.security_repo = security_repo

    async def get_active_policies(self, org_id: str) -> List[SecurityPolicy]:
        return await self.security_repo.get_active_policies_by_org(org_id)
