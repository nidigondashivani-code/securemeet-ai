from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.security import SecurityPolicy, SecurityIncident
from app.repositories.base import BaseRepository
from app.schemas.security import SecurityPolicyCreate, SecurityPolicyUpdate


class SecurityPolicyRepository(BaseRepository[SecurityPolicy, SecurityPolicyCreate, SecurityPolicyUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(SecurityPolicy, db)

    async def get_active_policies_by_org(self, org_id: str) -> List[SecurityPolicy]:
        query = select(SecurityPolicy).where(
            SecurityPolicy.organization_id == org_id,
            SecurityPolicy.is_active == True  # noqa: E712
        )
        result = await self.db.execute(query)
        return list(result.scalars().all())
