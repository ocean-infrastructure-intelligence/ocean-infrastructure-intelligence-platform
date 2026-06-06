"""Pydantic schemas for Site entities.

Contains request and response schemas used by the API layer
for ocean infrastructure site management.
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator

from backend.app.domain.models.site import SiteStatus

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PointUpdateDTO:
    """Pure domain DTO for passing entity updates independently
    of transport layers like Pydantic."""

    update_values: dict[str, Any]
    spatial_updated: bool = False
    longitude: float | None = None
    latitude: float | None = None


class SiteBase(BaseModel):
    """Common Site fields shared across API schemas."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Name of the infrastructure site.",
    )
    country_code: str = Field(..., description="ISO 3166-1 alpha-2 country code.")
    description: str | None = Field(
        None, max_length=1000, description="Optional description of the site."
    )

    @field_validator("country_code")
    @classmethod
    def validate_country_code(cls, value: str) -> str:
        """Validate that the country code conforms to ISO 3166-1 alpha-2."""
        if len(value) != 2:
            raise ValueError(
                "Country code must be exactly 2 characters long (ISO-3166 alpha-2)."
            )
        return value.upper()


class SiteCreate(SiteBase):
    """Schema used when creating a new Site."""

    latitude: float = Field(
        ..., ge=-90.0, le=90.0, description="Latitude in degrees (-90 to 90)."
    )
    longitude: float = Field(
        ..., ge=-180.0, le=180.0, description="Longitude in degrees (-180 to 180)."
    )


class SiteUpdate(BaseModel):
    """Schema used when updating an existing Site."""

    name: str | None = Field(None, min_length=1, max_length=255)
    country_code: str | None = Field(None, min_length=2, max_length=2)
    description: str | None = Field(None, max_length=1000)
    status: SiteStatus | None = None
    latitude: float | None = Field(default=None, ge=-90.0, le=90.0)
    longitude: float | None = Field(default=None, ge=-180.0, le=180.0)

    @field_validator("country_code")
    @classmethod
    def validate_country_code(cls, value: str | None) -> str | None:
        """Validate that the country code conforms to ISO 3166-1 alpha-2 if provided."""
        if value is not None:
            return value.upper()
        return value


class SiteRead(SiteBase):
    """Schema returned by API responses."""

    id: int
    status: SiteStatus
    latitude: float | None = None
    longitude: float | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
