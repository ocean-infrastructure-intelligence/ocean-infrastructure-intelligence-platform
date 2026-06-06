"""Application layer DTOs for Site operations with strict type safety."""

from dataclasses import dataclass
from backend.app.domain.models.site import SiteStatus


@dataclass(frozen=True)
class CoordinatesDTO:
    """Immutable, fully-formed coordinate pair constraint."""

    longitude: float
    latitude: float


@dataclass(frozen=True)
class SiteCreateDTO:
    """Strict DTO schema for initiating Site creation."""

    name: str
    country_code: str
    longitude: float
    latitude: float
    description: str | None = None


@dataclass(frozen=True)
class SiteUpdateDTO:
    """Strict DTO schema for partial updates.

    Attributes with None mean 'no change requested'.
    """

    name: str | None = None
    description: str | None = None
    status: SiteStatus | None = None
    coordinates: CoordinatesDTO | None = None
