from typing import List
from fastapi import APIRouter, Depends, Query, status
from app.api.deps import get_meeting_service
from app.schemas.common import ApiResponse
from app.schemas.meeting import MeetingCreate, MeetingResponse
from app.services.meeting_service import MeetingService

router = APIRouter(prefix="/meetings", tags=["Meeting Integration"])


@router.get("", response_model=ApiResponse[List[MeetingResponse]], status_code=status.HTTP_200_OK)
async def list_meetings(
    org_id: str = Query(..., description="Organization ID filter"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    meeting_service: MeetingService = Depends(get_meeting_service),
) -> ApiResponse[List[MeetingResponse]]:
    """Retrieves synced meetings across Google Meet, Zoom, and MS Teams."""
    meetings = await meeting_service.get_org_meetings(org_id, skip=skip, limit=limit)
    return ApiResponse(data=[MeetingResponse.model_validate(m) for m in meetings])


@router.post("", response_model=ApiResponse[MeetingResponse], status_code=status.HTTP_201_CREATED)
async def schedule_meeting(
    payload: MeetingCreate,
    meeting_service: MeetingService = Depends(get_meeting_service),
) -> ApiResponse[MeetingResponse]:
    """Schedules and hooks security monitoring onto a meeting."""
    meeting = await meeting_service.create(payload)
    return ApiResponse(message="Meeting scheduled with security guardrails", data=MeetingResponse.model_validate(meeting))
