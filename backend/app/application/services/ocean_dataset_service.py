"""Application service for orchestrating and assembling multi-temporal oceanographic datasets."""

from datetime import datetime
from backend.app.analytics.models import OceanObservation
from backend.app.providers.base import BaseOceanDataProvider


class OceanDatasetService:
    """Orchestrates temporal data acquisition to construct clean historical records."""

    def __init__(self, data_provider: BaseOceanDataProvider):
        """Injects the underlying data provider source."""
        self._provider = data_provider

    def build_dataset(
        self,
        longitude: float,
        latitude: float,
        timestamps: list[datetime],
    ) -> list[OceanObservation]:
        """Assembles an oceanographic dataset for an arbitrary list of timestamps.

        This serves as the core foundational engine for multi-year, seasonal,
        or custom temporal analysis windowing.
        """
        dataset = []
        for ts in timestamps:
            observation = self._provider.fetch_observation(
                longitude=longitude, latitude=latitude, timestamp=ts
            )
            dataset.append(observation)
        return dataset

    def build_historical_dataset(
        self,
        longitude: float,
        latitude: float,
        year: int,
    ) -> list[OceanObservation]:
        """Convenient facade method to assemble a standardized continuous 12-month series."""
        timestamps = [datetime(year, month, 1) for month in range(1, 13)]

        return self.build_dataset(
            longitude=longitude,
            latitude=latitude,
            timestamps=timestamps,
        )
