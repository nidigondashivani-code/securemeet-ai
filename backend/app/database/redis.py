from typing import AsyncGenerator
import redis.asyncio as aioredis
from app.core.config import settings

redis_pool = aioredis.ConnectionPool.from_url(
    str(settings.REDIS_URL),
    max_connections=50,
    decode_responses=True,
)


async def get_redis_client() -> AsyncGenerator[aioredis.Redis, None]:
    """Dependency that yields an active Redis client from connection pool."""
    client = aioredis.Redis(connection_pool=redis_pool)
    try:
        yield client
    finally:
        await client.aclose()
