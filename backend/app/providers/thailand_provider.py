"""Scientific data provider simulation calibrated for the Thailand maritime region."""

import math
from datetime import datetime
from backend.app.analytics.models import OceanObservation
from .base import BaseOceanDataProvider, ObservationNotFoundError


class ThailandOceanDataProvider(BaseOceanDataProvider):
    """Simulates real Copernicus/GEBCO grid data for the Andaman Sea & Gulf of Thailand."""

    # Approximate territorial marine boundaries for validation
    MIN_LON, MAX_LON = 92.0, 106.0
    MIN_LAT, MAX_LAT = 5.0, 14.0

    def fetch_observation(
        self, longitude: float, latitude: float, timestamp: datetime
    ) -> OceanObservation:
        """Simulates data fetch with strict bounds checking and lineage tracking."""
        if not (
            self.MIN_LON <= longitude <= self.MAX_LON
            and self.MIN_LAT <= latitude <= self.MAX_LAT
        ):
            raise ObservationNotFoundError(
                f"Coordinates ({longitude}, {latitude}) are outside the Thailand marine territory."
            )

        # We simulate a sharp drop in depth in the Andaman Sea when moving west
        base_depth = 200.0
        if longitude > 98.0:
            base_depth = 1200.0 + (longitude - 98.0) * 800.0

        # We simulate a small seasonal fluctuation in surface temperature (SST)
        month_factor = math.sin((timestamp.month / 12.0) * 2 * math.pi)
        sst = 28.5 + (month_factor * 1.5)

        # Temperature horizons (stable at 1000m deep)
        depth_temps = {100: round(sst - 6.0, 2), 500: 8.2, 1000: 4.5}

        return OceanObservation(
            longitude=longitude,
            latitude=latitude,
            timestamp=timestamp,
            surface_temperature_c=round(sst, 2),
            temperature_at_depths_c=depth_temps,
            seafloor_depth_m=round(base_depth, 2),
            source="mock-thailand",  # Фиксируем происхождение данных для трассировки
        )
