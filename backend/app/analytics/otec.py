"""Analytical services processing oceanographic profiles into pure thermodynamic metrics."""

from backend.app.analytics.models import TemperatureProfile, OtecAssessment


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
