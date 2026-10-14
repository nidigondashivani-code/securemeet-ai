from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.role import Role
from app.repositories.base import BaseRepository
from app.schemas.role import RoleCreate, RoleUpdate


class RoleRepository(BaseRepository[Role, RoleCreate, RoleUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Role, db)

    async def get_by_name(self, name: str) -> Optional[Role]:
        query = select(Role).where(Role.name == name)
        result = await self.db.execute(query)
        return result.scalars().first()
