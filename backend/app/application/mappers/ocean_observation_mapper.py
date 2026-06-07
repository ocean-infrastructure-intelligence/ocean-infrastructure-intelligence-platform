"""Transforms raw multi-temporal observations into analytical climatology profiles."""

from collections import defaultdict
from backend.app.analytics.models import (
    OceanObservation,
    HydroclimatologyProfile,
    MonthlyThermalObservation,
)


class OceanObservationMapper:
    """Anti-corruption layer separating physical data acquisition from analytics core."""

    @staticmethod
    def to_hydroclimatology_profile(
        observations: list[OceanObservation],
    ) -> HydroclimatologyProfile:
        """Aggregates a historical time series of observations into a 12-month profile.

        Extracts baseline deep-sea parameters and computes monthly average SST.

        Raises:
            ValueError: If the input observations list is empty or lacks deep sea horizons.
        """
        if not observations:
            raise ValueError(
                "Cannot map empty observation dataset to hydroclimatology profile."
            )

        # 1. Extract stable parameters of the deep layer from the last or reference observation
        reference_obs = observations[-1]
        if not reference_obs.temperature_at_depths_c:
            raise ValueError("Observations missing deep sea temperature horizons.")

        max_depth = max(reference_obs.temperature_at_depths_c.keys())
        deep_temp = reference_obs.temperature_at_depths_c[max_depth]

        # 2. Group SST by calendar months for calculating monthly averages
        monthly_sst_accumulator = defaultdict(list)
        for obs in observations:
            monthly_sst_accumulator[obs.timestamp.month].append(
                obs.surface_temperature_c
            )

        # 3. Build annual profile (12 months)
        monthly_observations = []
        for month in sorted(monthly_sst_accumulator.keys()):
            temperatures = monthly_sst_accumulator[month]
            avg_sst = sum(temperatures) / len(temperatures)
            monthly_observations.append(
                MonthlyThermalObservation(
                    month=month, surface_temperature_c=round(avg_sst, 2)
                )
            )

        return HydroclimatologyProfile(
            deep_temperature_c=deep_temp,
            deep_water_depth_m=float(max_depth),
            monthly_observations=monthly_observations,
        )
