"""Analytical services processing oceanographic profiles into pure thermodynamic metrics."""

from backend.app.analytics.models import (
    HydroclimatologyProfile,
    TemperatureProfile,
    OtecAssessment,
)


class OtecAnalysisService:
    """Pure mathematical physics engine evaluating thermal energy extraction limits."""

    CELSIUS_TO_KELVIN_OFFSET: float = 273.15
    NET_TO_CARNOT_RATIO: float = 0.30  # 30% от лимита Карно уходит в чистую генерацию

    @classmethod
    def calculate_delta_t(cls, profile: TemperatureProfile) -> float:
        """Compute flat temperature gradient between surface and deep sea layers."""
        return profile.surface_temperature_c - profile.deep_temperature_c

    @classmethod
    def calculate_carnot_efficiency_pct(cls, profile: TemperatureProfile) -> float:
        """Evaluate the ideal thermodynamic limit based on Carnot theorem (returned as %)."""
        t_hot_k = profile.surface_temperature_c + cls.CELSIUS_TO_KELVIN_OFFSET
        t_cold_k = profile.deep_temperature_c + cls.CELSIUS_TO_KELVIN_OFFSET

        if t_hot_k <= 0 or t_cold_k <= 0 or t_cold_k >= t_hot_k:
            return 0.0

        efficiency_fraction = 1.0 - (t_cold_k / t_hot_k)
        return round(efficiency_fraction * 100.0, 2)

    @classmethod
    def analyze_profile(cls, profile: TemperatureProfile) -> OtecAssessment:
        """Transform raw profile into pure physical constraints."""
        delta_t = cls.calculate_delta_t(profile)
        carnot_pct = cls.calculate_carnot_efficiency_pct(profile)
        net_pct = round(carnot_pct * cls.NET_TO_CARNOT_RATIO, 2)

        return OtecAssessment(
            delta_t_c=round(delta_t, 2),
            carnot_efficiency_pct=carnot_pct,
            net_efficiency_estimate_pct=net_pct,
        )

    @classmethod
    def evaluate_climatology_stability(
        cls, hydro_profile: HydroclimatologyProfile
    ) -> float:
        """Compute thermal stability factor (0.0 to 1.0).

        Fluctuations up to 2°C are considered perfect and carry no penalty.
        """
        temps = [
            obs.surface_temperature_c for obs in hydro_profile.monthly_observations
        ]
        if not temps:
            return 0.0

        temp_delta_year = max(temps) - min(temps)

        # If the fluctuations are within the normal range for the equatorial zone
        if temp_delta_year <= 2.0:
            return 1.0

        # If the fluctuations are greater than 6°C, stability drops to zero
        if temp_delta_year >= 6.0:
            return 0.0

        # Linear penalty only for the range from 2.0 to 6.0 degrees
        normalized_penalty = (temp_delta_year - 2.0) / (6.0 - 2.0)
        return round(1.0 - normalized_penalty, 2)
