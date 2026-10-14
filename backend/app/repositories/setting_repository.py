from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.setting import SystemSetting
from app.repositories.base import BaseRepository


class SettingRepository(BaseRepository[SystemSetting, dict, dict]):
    def __init__(self, db: AsyncSession):
        super().__init__(SystemSetting, db)

    async def get_by_key(self, key: str) -> Optional[SystemSetting]:
        query = select(SystemSetting).where(SystemSetting.key == key)
        result = await self.db.execute(query)
        return result.scalars().first()
