"""
Refresh Token management with rotation and revocation capabilities.
Interface placeholder ready for implementation in next phase.
"""
from typing import Optional


class RefreshTokenManager:
    @staticmethod
    async def issue_refresh_token(user_id: str) -> str:
        raise NotImplementedError("Authentication logic will be implemented in the next phase.")

    @staticmethod
    async def rotate_refresh_token(old_token: str) -> str:
        raise NotImplementedError("Authentication logic will be implemented in the next phase.")

    @staticmethod
    async def revoke_refresh_token(token: str) -> bool:
        raise NotImplementedError("Authentication logic will be implemented in the next phase.")
