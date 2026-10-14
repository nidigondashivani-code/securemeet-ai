from typing import Any, Dict, Optional


class AppException(Exception):
    """Base application exception for all domain and service errors."""
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        error_code: str = "INTERNAL_SERVER_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=404, error_code="NOT_FOUND", details=details)


class BadRequestException(AppException):
    def __init__(self, message: str = "Bad request", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=400, error_code="BAD_REQUEST", details=details)


class UnauthorizedException(AppException):
    def __init__(self, message: str = "Unauthorized access", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=401, error_code="UNAUTHORIZED", details=details)


class ForbiddenException(AppException):
    def __init__(self, message: str = "Access forbidden", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=403, error_code="FORBIDDEN", details=details)


class ConflictException(AppException):
    def __init__(self, message: str = "Resource conflict", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=409, error_code="CONFLICT", details=details)
