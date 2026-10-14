from typing import Any, Dict, Optional
from app.exceptions.base import UnauthorizedException, ForbiddenException


class InvalidCredentialsException(UnauthorizedException):
    def __init__(self, message: str = "Invalid email or password"):
        super().__init__(message=message, details={"hint": "Verify credentials and retry"})


class TokenExpiredException(UnauthorizedException):
    def __init__(self, message: str = "Token has expired"):
        super().__init__(message=message, details={"hint": "Refresh token or re-authenticate"})


class InvalidTokenException(UnauthorizedException):
    def __init__(self, message: str = "Token is invalid or malformed"):
        super().__init__(message=message, details={"hint": "Provide a valid Bearer token"})


class InsufficientPermissionsException(ForbiddenException):
    def __init__(self, required_permission: Optional[str] = None):
        super().__init__(
            message="You do not have permission to perform this action",
            details={"required_permission": required_permission} if required_permission else {},
        )
