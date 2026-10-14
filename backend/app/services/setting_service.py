from typing import Optional
from app.models.setting import SystemSetting
from app.repositories.setting_repository import SettingRepository
from app.services.base import BaseService


class SettingService(BaseService[SystemSetting, dict, dict]):
    def __init__(self, setting_repo: SettingRepository):
        super().__init__(setting_repo)
        self.setting_repo = setting_repo

    async def get_by_key(self, key: str) -> Optional[SystemSetting]:
        return await self.setting_repo.get_by_key(key)
