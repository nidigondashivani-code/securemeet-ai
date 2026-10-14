from fastapi import APIRouter, Depends, status
from app.api.deps import get_org_service
from app.schemas.common import ApiResponse
from app.schemas.organization import OrganizationCreate, OrganizationResponse
from app.services.organization_service import OrganizationService

router = APIRouter(prefix="/organizations", tags=["Organization Management"])


@router.post("", response_model=ApiResponse[OrganizationResponse], status_code=status.HTTP_201_CREATED)
async def create_organization(
    payload: OrganizationCreate,
    org_service: OrganizationService = Depends(get_org_service),
) -> ApiResponse[OrganizationResponse]:
    """Provisions a new tenant organization."""
    org = await org_service.create(payload)
    return ApiResponse(message="Organization provisioned successfully", data=OrganizationResponse.model_validate(org))


@router.get("/{org_id}", response_model=ApiResponse[OrganizationResponse], status_code=status.HTTP_200_OK)
async def get_organization(
    org_id: str,
    org_service: OrganizationService = Depends(get_org_service),
) -> ApiResponse[OrganizationResponse]:
    """Retrieves tenant organization details."""
    org = await org_service.get(org_id)
    return ApiResponse(data=OrganizationResponse.model_validate(org))
