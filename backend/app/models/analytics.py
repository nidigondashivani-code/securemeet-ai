from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class MeetingMetricSnapshot(IdentifiableBase):
    __tablename__ = "meeting_metrics_snapshots"

    organization_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    period: Mapped[str] = mapped_column(String(50), nullable=False)  # daily, weekly, monthly
    total_meetings: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    security_violations_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    metrics_data: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
