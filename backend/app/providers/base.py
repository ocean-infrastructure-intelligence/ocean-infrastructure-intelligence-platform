"""Contracts and exceptions for the Ocean Data Ingestion Layer."""

from abc import ABC, abstractmethod
from datetime import datetime
from backend.app.analytics.models import OceanObservation


class OceanDataException(Exception):
    """Base exception for all oceanographic data acquisition errors."""

    pass


class ObservationNotFoundError(OceanDataException):
    """Raised when no ocean data is available for the given spatial-temporal window."""

    pass


class BaseOceanDataProvider(ABC):
    """Abstract interface for multi-source oceanographic data ingestion."""

    @abstractmethod
    def fetch_observation(
        self, longitude: float, latitude: float, timestamp: datetime
    ) -> OceanObservation:
        """Retrieve physical and spatial data for a specific coordinate and time.

        Raises:
            ObservationNotFoundError: If the coordinates are out of bounds or missing.
            OceanDataException: For underlying infrastructure or parse errors.
        """
        pass
