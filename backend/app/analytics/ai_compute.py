"""Analytical services for evaluating AI Datacenter co-location metrics and PUE optimization."""

from backend.app.analytics.models import (
    AiDatacenterAssessment,
    AiDatacenterProfile,
    HydroclimatologyProfile,
)


class AiComputeAnalysisService:
    """Evaluates cooling efficiency gains and network constraints for marine AI hubs."""

    MAX_ACCEPTABLE_LATENCY_DIST_KM: float = 100.0  # Затухание сигнала после 100 км

    @classmethod
    def evaluate_datacenter(
        cls, ai_profile: AiDatacenterProfile, hydro_profile: HydroclimatologyProfile
    ) -> "AiDatacenterAssessment":
        """Compute PUE reduction via OTEC cold-water cooling and assess latency risks."""
        # 1. Считаем PUE на основе температуры глубинной воды
        # Идеальная вода (~4°C) дает базовый PUE = 1.03. Каждый градус выше ухудшает охлаждение.
        t_cold = hydro_profile.deep_temperature_c

        achievable_pue = 1.03 + max(0.0, (t_cold - 4.0) * 0.02)
        achievable_pue = round(achievable_pue, 2)

        # Традиционный дата-центр имеет PUE около 1.4. Считаем экономию:
        traditional_cooling_overhead = 0.40
        current_cooling_overhead = achievable_pue - 1.0
        savings_pct = round(
            (1.0 - (current_cooling_overhead / traditional_cooling_overhead)) * 100.0, 2
        )

        # 2. Оценка задержки сети (Network Latency Penalty)
        if ai_profile.distance_to_backbone_pop_km >= cls.MAX_ACCEPTABLE_LATENCY_DIST_KM:
            latency_penalty = 0.0
        else:
            # Линейное падение от 1.0 (0 км) до 0.0 (100 км)
            latency_penalty = 1.0 - (
                ai_profile.distance_to_backbone_pop_km
                / cls.MAX_ACCEPTABLE_LATENCY_DIST_KM
            )

        return AiDatacenterAssessment(
            achievable_pue=achievable_pue,
            cooling_energy_savings_pct=max(0.0, savings_pct),
            network_latency_penalty=round(latency_penalty, 2),
        )
