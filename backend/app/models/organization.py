from sqlalchemy import Boolean, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class Organization(IdentifiableBase):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    settings: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
