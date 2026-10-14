import pytest
from app.exceptions.auth_exceptions import InvalidCredentialsException, TokenExpiredException


def test_auth_exceptions_instantiation():
    """Validates standardized error codes and default messages on auth exceptions."""
    exc = InvalidCredentialsException()
    assert exc.status_code == 401
    assert exc.error_code == "UNAUTHORIZED"

    expired = TokenExpiredException()
    assert expired.status_code == 401
    assert expired.error_code == "UNAUTHORIZED"
