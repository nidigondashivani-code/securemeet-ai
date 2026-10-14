from typing import Any, Dict, List


class LLMClient:
    """Wrapper around LLM providers with retry, telemetry, and fallback."""
    def __init__(self):
        pass

    async def generate_response(self, prompt: str, system_prompt: str) -> str:
        raise NotImplementedError("AI engine integration will be implemented in subsequent phase.")


class MeetingSummarizer:
    """Generates structured executive summaries and action items from transcripts."""
    async def summarize_meeting(self, transcript: str) -> Dict[str, Any]:
        raise NotImplementedError("AI engine integration will be implemented in subsequent phase.")


class SensitiveDataRedactor:
    """Detects and redacts PII, credentials, PCI-DSS data, and trade secrets."""
    async def redact_pii(self, content: str) -> str:
        raise NotImplementedError("AI engine integration will be implemented in subsequent phase.")
