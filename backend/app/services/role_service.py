from typing import Optional
from app.models.role import Role
from app.repositories.role_repository import RoleRepository
from app.schemas.role import RoleCreate, RoleUpdate
from app.services.base import BaseService


class RoleService(BaseService[Role, RoleCreate, RoleUpdate]):
    def __init__(self, role_repo: RoleRepository):
        super().__init__(role_repo)
        self.role_repo = role_repo

    async def get_by_name(self, name: str) -> Optional[Role]:
        return await self.role_repo.get_by_name(name)
