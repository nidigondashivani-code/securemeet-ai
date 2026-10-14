from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.audit import AuditLog
from app.repositories.base import BaseRepository


class AuditRepository(BaseRepository[AuditLog, dict, dict]):
    def __init__(self, db: AsyncSession):
        super().__init__(AuditLog, db)

    async def get_logs_by_org(self, org_id: str, skip: int = 0, limit: int = 100) -> List[AuditLog]:
        query = (
            select(AuditLog)
            .where(AuditLog.organization_id == org_id)
            .order_by(AuditLog.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(query)
        return list(result.scalars().all())
