"""
Configuration management for Coca-Cola Sales AI Agent Framework.
"""

import os
from typing import List
try:
    from pydantic_settings import BaseSettings
except ImportError:
    # Fallback for older pydantic versions
    from pydantic import BaseSettings
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Azure OpenAI Configuration
    azure_openai_api_key: str = Field(..., env="AZURE_OPENAI_API_KEY")
    azure_openai_endpoint: str = Field(..., env="AZURE_OPENAI_ENDPOINT")
    azure_openai_deployment_name: str = Field(default="gpt-4o", env="AZURE_OPENAI_DEPLOYMENT_NAME")
    azure_openai_api_version: str = Field(default="2024-05-01-preview", env="AZURE_OPENAI_API_VERSION")
    
    # Database Configuration
    database_url: str = Field(default="sqlite:///./coke_sales.db", env="DATABASE_URL")
    
    # API Configuration
    api_host: str = Field(default="0.0.0.0", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")
    debug: bool = Field(default=True, env="DEBUG")
    
    # Security
    secret_key: str = Field(..., env="SECRET_KEY")
    
    # CORS Configuration
    cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://127.0.0.1:3000"],
        env="CORS_ORIGINS"
    )
    
    # Semantic Kernel Configuration
    max_tokens: int = Field(default=4000, env="MAX_TOKENS")
    temperature: float = Field(default=0.7, env="TEMPERATURE")
    
    # Data Generation Settings
    generate_sample_data: bool = Field(default=True, env="GENERATE_SAMPLE_DATA")
    sample_accounts_count: int = Field(default=50, env="SAMPLE_ACCOUNTS_COUNT")
    sample_opportunities_count: int = Field(default=200, env="SAMPLE_OPPORTUNITIES_COUNT")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()
