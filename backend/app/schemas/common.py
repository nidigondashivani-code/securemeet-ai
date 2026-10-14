from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class BaseSchema(BaseModel):
    """Base Pydantic v2 schema with ORM mode configuration."""
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class ApiResponse(BaseSchema, Generic[T]):
    """Consistent enterprise API response envelope."""
    success: bool = True
    message: str = "Operation completed successfully"
    data: Optional[T] = None
    error_code: Optional[str] = None
    details: Optional[dict] = None


class PaginationParams(BaseModel):
    """Query parameters for pagination."""
    page: int = Field(default=1, ge=1, description="Page number starting at 1")
    page_size: int = Field(default=20, ge=1, le=100, description="Items per page")


class PaginatedResponse(BaseSchema, Generic[T]):
    """Standardized paginated list response."""
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
