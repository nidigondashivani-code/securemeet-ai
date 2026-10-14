from sqlalchemy import Boolean, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class SecurityPolicy(IdentifiableBase):
    __tablename__ = "security_policies"

    organization_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    rules: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)


class SecurityIncident(IdentifiableBase):
    __tablename__ = "security_incidents"

    meeting_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    severity: Mapped[str] = mapped_column(String(50), nullable=False)
    incident_type: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    remediation_status: Mapped[str] = mapped_column(String(50), default="OPEN", nullable=False)
