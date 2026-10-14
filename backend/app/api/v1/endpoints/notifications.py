from typing import List
from fastapi import APIRouter, Depends, Query, status
from app.api.deps import get_notification_service
from app.schemas.common import ApiResponse
from app.schemas.notification import NotificationResponse
from app.services.notification_service import NotificationService

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("", response_model=ApiResponse[List[NotificationResponse]], status_code=status.HTTP_200_OK)
async def list_notifications(
    user_id: str = Query(..., description="Target User UUID"),
    unread_only: bool = Query(False),
    notification_service: NotificationService = Depends(get_notification_service),
) -> ApiResponse[List[NotificationResponse]]:
    """Fetches user notifications and security violation alerts."""
    notifications = await notification_service.get_user_alerts(user_id, unread_only=unread_only)
    return ApiResponse(data=[NotificationResponse.model_validate(n) for n in notifications])
