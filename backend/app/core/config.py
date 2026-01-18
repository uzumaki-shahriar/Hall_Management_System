
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    DATABASE_URL: str
    
    # JWT Configuration
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10

    SYSTEM_EMAIL: str
    SYSTEM_EMAIL_PASSWORD: str
    
    
    
    # Environment
    ENVIRONMENT: str = "development"  # development, production
    
    # CORS Settings
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:8000",
    ]
    
    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Application Info
    APP_NAME: str = "Hall Management System"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "System for managing hall operations"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
