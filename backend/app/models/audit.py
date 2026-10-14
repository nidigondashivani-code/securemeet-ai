from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class AuditLog(IdentifiableBase):
    __tablename__ = "audit_logs"

    action: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    actor_id: Mapped[str] = mapped_column(String(36), index=True, nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), index=True, nullable=True)
    resource_type: Mapped[str] = mapped_column(String(100), nullable=False)
    resource_id: Mapped[str] = mapped_column(String(36), nullable=True)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=True)
    payload: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
