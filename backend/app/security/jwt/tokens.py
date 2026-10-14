"""
JWT token creation, validation, and payload handling.
Interface placeholder ready for implementation in next phase.
"""
from typing import Any, Dict, Optional


class JWTHandler:
    @staticmethod
    def create_access_token(subject: str, claims: Optional[Dict[str, Any]] = None) -> str:
        raise NotImplementedError("Authentication logic will be implemented in the next phase.")

    @staticmethod
    def decode_access_token(token: str) -> Dict[str, Any]:
        raise NotImplementedError("Authentication logic will be implemented in the next phase.")
