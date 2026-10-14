from fastapi import APIRouter, Depends, status
from app.api.deps import get_setting_service
from app.schemas.common import ApiResponse
from app.schemas.setting import SettingResponse, SettingUpdate
from app.services.setting_service import SettingService

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("/{key}", response_model=ApiResponse[SettingResponse], status_code=status.HTTP_200_OK)
async def get_setting(
    key: str,
    setting_service: SettingService = Depends(get_setting_service),
) -> ApiResponse[SettingResponse]:
    """Retrieves system or organization governance setting."""
    setting = await setting_service.get_by_key(key)
    return ApiResponse(data=SettingResponse.model_validate(setting))
