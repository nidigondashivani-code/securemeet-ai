from sqlalchemy import Boolean, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class Notification(IdentifiableBase):
    __tablename__ = "notifications"

    user_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(String(1000), nullable=False)
    channel: Mapped[str] = mapped_column(String(50), default="IN_APP", nullable=False)
    is_read: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    metadata_info: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
