"""Pydantic schemas for Site entities.

Contains request and response schemas used by the API layer
for ocean infrastructure site management.
"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from backend.app.models.site import SiteStatus

class SiteBase(BaseModel):
    """Common Site fields shared across API schemas."""

    name: str
    country_code: str
    description: str | None = None

class SiteCreate(SiteBase):
    """Schema used when creating a new Site."""

    latitude: float
    longitude: float

class SiteUpdate(BaseModel):
    """Schema used when updating an existing Site."""

    name: str | None = None
    description: str | None = None
    status: SiteStatus | None = None

class SiteRead(SiteBase):
    """Schema returned by API responses."""

    id: int

    status: SiteStatus

    latitude: float | None
    longitude: float | None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )