"""Configuration module for the Ocean Infrastructure Intelligence Platform (OIIP).

Handles environment variable parsing, database connection strings,
and application-wide settings using Pydantic Settings.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings mapped to environment variables."""

    # Provide a default fallback or use Field(default=...) to satisfy static type checkers
    database_url: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/oiip",
        description="The connection string for the PostgreSQL/PostGIS database.",
    )

    debug: bool = Field(
        default=False,
        description="Global debug flag. Controls SQL echoing and verbose logging.",
    )

    # Modern Pydantic v2 configuration style
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Instantiate settings. Type checker is now happy because all fields have defaults.
settings = Settings()
