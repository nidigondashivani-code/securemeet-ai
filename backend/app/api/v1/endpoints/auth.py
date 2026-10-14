from fastapi import APIRouter, Depends, status
from app.api.deps import get_auth_service
from app.schemas.auth import LoginRequest, TokenResponse, RefreshTokenRequest
from app.schemas.common import ApiResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=ApiResponse[TokenResponse], status_code=status.HTTP_200_OK)
async def login(
    login_data: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponse[TokenResponse]:
    """Authenticates user credentials and issues JWT token pair."""
    tokens = await auth_service.authenticate_user(login_data)
    return ApiResponse(message="Login successful", data=tokens)


@router.post("/refresh", response_model=ApiResponse[TokenResponse], status_code=status.HTTP_200_OK)
async def refresh_token(
    refresh_data: RefreshTokenRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> ApiResponse[TokenResponse]:
    """Issues a new access token using a valid refresh token."""
    tokens = await auth_service.refresh_access_token(refresh_data)
    return ApiResponse(message="Token refreshed successfully", data=tokens)
