from typing import List, Union
from pydantic import AnyHttpUrl, PostgresDsn, RedisDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings powered by Pydantic v2.
    Reads environment variables from system and .env file.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    # Application
    APP_NAME: str = "SecureMeet AI"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "development_secret_key_change_in_production_32_bytes_min"
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "0.0.0.0"]
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    # Database (PostgreSQL)
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "securemeet_admin"
    POSTGRES_PASSWORD: str = "change_this_insecure_password"
    POSTGRES_DB: str = "securemeet_db"
    DATABASE_URL: Union[str, None] = None
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10

    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_connection(cls, v: Union[str, None], info) -> str:
        if isinstance(v, str) and v:
            return v
        data = info.data
        return (
            f"postgresql+asyncpg://{data.get('POSTGRES_USER', 'securemeet_admin')}:"
            f"{data.get('POSTGRES_PASSWORD', 'change_this_insecure_password')}@"
            f"{data.get('POSTGRES_SERVER', 'localhost')}:"
            f"{data.get('POSTGRES_PORT', 5432)}/"
            f"{data.get('POSTGRES_DB', 'securemeet_db')}"
        )

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Union[str, None] = None
    REDIS_DB: int = 0
    REDIS_URL: Union[str, None] = None

    @field_validator("REDIS_URL", mode="before")
    def assemble_redis_connection(cls, v: Union[str, None], info) -> str:
        if isinstance(v, str) and v:
            return v
        data = info.data
        password_str = (
            f":{data.get('REDIS_PASSWORD')}@" if data.get("REDIS_PASSWORD") else ""
        )
        return (
            f"redis://{password_str}{data.get('REDIS_HOST', 'localhost')}:"
            f"{data.get('REDIS_PORT', 6379)}/{data.get('REDIS_DB', 0)}"
        )

    # Celery
    CELERY_BROKER_URL: Union[str, None] = None
    CELERY_RESULT_BACKEND: Union[str, None] = None

    # Security & JWT
    JWT_SECRET_KEY: str = "dev_jwt_secret_key_must_be_changed_in_prod_64_bytes"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # External OAuth Integrations
    GOOGLE_CLIENT_ID: Union[str, None] = None
    GOOGLE_CLIENT_SECRET: Union[str, None] = None
    ZOOM_CLIENT_ID: Union[str, None] = None
    ZOOM_CLIENT_SECRET: Union[str, None] = None
    TEAMS_CLIENT_ID: Union[str, None] = None
    TEAMS_CLIENT_SECRET: Union[str, None] = None
    TEAMS_TENANT_ID: Union[str, None] = None

    # AI Service Config
    OPENAI_API_KEY: Union[str, None] = None
    ANTHROPIC_API_KEY: Union[str, None] = None
    AI_MODEL_NAME: str = "gpt-4o"
    AI_MAX_TOKENS: int = 4096
    AI_TEMPERATURE: float = 0.2

    # Audit & Compliance
    AUDIT_LOG_RETENTION_DAYS: int = 365
    ENABLE_STRICT_PII_MASKING: bool = True


settings = Settings()
