from typing import Optional
from app.models.organization import Organization
from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization import OrganizationCreate, OrganizationUpdate
from app.services.base import BaseService


class OrganizationService(BaseService[Organization, OrganizationCreate, OrganizationUpdate]):
    def __init__(self, org_repo: OrganizationRepository):
        super().__init__(org_repo)
        self.org_repo = org_repo

    async def get_by_slug(self, slug: str) -> Optional[Organization]:
        return await self.org_repo.get_by_slug(slug)
