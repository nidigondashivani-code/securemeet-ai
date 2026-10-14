from typing import List, Optional
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.services.base import BaseService


class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, user_repo: UserRepository):
        super().__init__(user_repo)
        self.user_repo = user_repo

    async def get_by_email(self, email: str) -> Optional[User]:
        return await self.user_repo.get_by_email(email)

    async def register_user(self, schema: UserCreate) -> User:
        raise NotImplementedError("User registration logic will be implemented in subsequent phase.")
