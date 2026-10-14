from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import IdentifiableBase


class Role(IdentifiableBase):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    permissions: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
