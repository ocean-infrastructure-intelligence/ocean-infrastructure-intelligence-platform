"""Abstract data provider interfaces for the Ocean Data Ingestion Layer."""

from abc import ABC, abstractmethod
from datetime import datetime
from backend.app.analytics.models import OceanObservation


class BaseOceanDataProvider(ABC):
    """Abstract interface for multi-source oceanographic data ingestion."""

    @abstractmethod
    def fetch_observation(
        self, longitude: float, latitude: float, timestamp: datetime
    ) -> OceanObservation:
        """Retrieve physical and spatial data for a specific coordinate and time."""
        pass
