from typing import List
from fastapi import APIRouter, Depends, status
from app.api.deps import get_role_service
from app.schemas.common import ApiResponse
from app.schemas.role import RoleCreate, RoleResponse
from app.services.role_service import RoleService

router = APIRouter(prefix="/roles", tags=["Roles & Permissions"])


@router.get("", response_model=ApiResponse[List[RoleResponse]], status_code=status.HTTP_200_OK)
async def list_roles(
    role_service: RoleService = Depends(get_role_service),
) -> ApiResponse[List[RoleResponse]]:
    """Lists enterprise RBAC roles and their associated permissions."""
    roles = await role_service.get_all()
    return ApiResponse(data=[RoleResponse.model_validate(r) for r in roles])


@router.post("", response_model=ApiResponse[RoleResponse], status_code=status.HTTP_201_CREATED)
async def create_role(
    payload: RoleCreate,
    role_service: RoleService = Depends(get_role_service),
) -> ApiResponse[RoleResponse]:
    """Creates a custom security role with granular permission flags."""
    role = await role_service.create(payload)
    return ApiResponse(message="Role created successfully", data=RoleResponse.model_validate(role))
