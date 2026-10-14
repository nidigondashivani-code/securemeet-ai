from typing import List
from fastapi import APIRouter, Depends, Query, status
from app.api.deps import get_user_service
from app.schemas.common import ApiResponse
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["User Management"])


@router.post("", response_model=ApiResponse[UserResponse], status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: UserCreate,
    user_service: UserService = Depends(get_user_service),
) -> ApiResponse[UserResponse]:
    """Registers a new user within an organization."""
    user = await user_service.register_user(payload)
    return ApiResponse(message="User created successfully", data=UserResponse.model_validate(user))


@router.get("/{user_id}", response_model=ApiResponse[UserResponse], status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_id: str,
    user_service: UserService = Depends(get_user_service),
) -> ApiResponse[UserResponse]:
    """Retrieves user profile details by UUID."""
    user = await user_service.get(user_id)
    return ApiResponse(data=UserResponse.model_validate(user))
