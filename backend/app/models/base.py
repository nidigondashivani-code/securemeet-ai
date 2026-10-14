import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class IdentifiableBase(Base):
    """
    Abstract model with a primary UUID identifier.
    Subclasses define their respective enterprise domain columns.
    """
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
