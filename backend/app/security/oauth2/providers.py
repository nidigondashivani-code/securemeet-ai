"""
OAuth2 Provider Integrations (Google, Zoom, Microsoft Teams).
Interface placeholder ready for implementation in next phase.
"""
from typing import Dict, Any


class OAuth2ProviderService:
    @staticmethod
    async def get_authorization_url(provider: str) -> str:
        raise NotImplementedError("Authentication logic will be implemented in the next phase.")

    @staticmethod
    async def exchange_code_for_tokens(provider: str, code: str) -> Dict[str, Any]:
        raise NotImplementedError("Authentication logic will be implemented in the next phase.")
