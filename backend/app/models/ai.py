from sqlalchemy import String, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class MeetingAISummary(IdentifiableBase):
    __tablename__ = "meeting_ai_summaries"

    meeting_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    summary_text: Mapped[str] = mapped_column(Text, nullable=False)
    action_items: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    key_decisions: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    sentiment_score: Mapped[str] = mapped_column(String(50), nullable=True)
    pii_redacted: Mapped[bool] = mapped_column(default=True, nullable=False)
