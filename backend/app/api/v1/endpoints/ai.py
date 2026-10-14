from fastapi import APIRouter, Depends, status
from app.api.deps import get_ai_service
from app.schemas.ai import AISummaryResponse
from app.schemas.common import ApiResponse
from app.services.ai_service import AIService

router = APIRouter(prefix="/ai", tags=["AI Services"])


@router.get("/meetings/{meeting_id}/summary", response_model=ApiResponse[AISummaryResponse], status_code=status.HTTP_200_OK)
async def get_meeting_summary(
    meeting_id: str,
    ai_service: AIService = Depends(get_ai_service),
) -> ApiResponse[AISummaryResponse]:
    """Retrieves AI-generated summary, key decisions, action items, and redacted PII."""
    summary = await ai_service.get_summary_for_meeting(meeting_id)
    return ApiResponse(data=AISummaryResponse.model_validate(summary))
