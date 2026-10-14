from typing import Any, Generic, List, Optional, TypeVar
from app.repositories.base import BaseRepository

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Base Service layer encapsulating domain business logic.
    Communicates strictly with repositories and external adapters.
    """
    def __init__(self, repository: BaseRepository[ModelType, CreateSchemaType, UpdateSchemaType]):
        self.repository = repository

    async def get(self, id: Any) -> Optional[ModelType]:
        return await self.repository.get_by_id(id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return await self.repository.get_multi(skip=skip, limit=limit)

    async def create(self, schema: CreateSchemaType) -> ModelType:
        return await self.repository.create(schema)

    async def remove(self, id: Any) -> Optional[ModelType]:
        return await self.repository.delete(id=id)
