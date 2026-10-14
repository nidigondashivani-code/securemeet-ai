from datetime import datetime
from typing import List, Optional
from app.schemas.common import BaseSchema


class AISummaryRequest(BaseSchema):
    meeting_id: str
    transcript: str


class AISummaryResponse(BaseSchema):
    id: str
    meeting_id: str
    summary_text: str
    action_items: List[str]
    key_decisions: List[str]
    sentiment_score: Optional[str] = None
    pii_redacted: bool
    created_at: datetime
