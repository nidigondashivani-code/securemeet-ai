from datetime import datetime
from sqlalchemy import DateTime, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class Meeting(IdentifiableBase):
    __tablename__ = "meetings"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    platform: Mapped[str] = mapped_column(String(50), nullable=False)  # google_meet, zoom, teams
    external_meeting_id: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    host_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    scheduled_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    scheduled_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="SCHEDULED", nullable=False)
    security_metadata: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
