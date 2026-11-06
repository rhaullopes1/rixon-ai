from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str = "RIX-ON AI"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    SECRET_KEY: str = "change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    DATABASE_URL: str = "sqlite:///./rixon.db"
    
    OPENAI_API_KEY: str | None = None
    XAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None
    
    DEFAULT_MODEL_PROVIDER: str = "mock"
    DEFAULT_MODEL_NAME: str = "gpt-4o-mini"
    
    ENVIRONMENT: str = "production"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
