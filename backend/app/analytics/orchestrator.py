"""Orchestrates pure domain entities, bathymetry constraints, and MCDA scoring rules."""

from backend.app.analytics.models import (
    TemperatureProfile,
    BathymetryProfile,
    ScoreComponent,
    SiteOtecAssessment,
)
from backend.app.analytics.otec import OtecAnalysisService
from backend.app.analytics.site_scoring import SiteScoringService
from backend.app.analytics.bathymetry import BathymetryAnalysisService


class SiteIntelligenceOrchestrator:
    """High-level domain orchestrator compiling multi-disciplinary site metrics."""

    # Business thresholds for normalizing the temperature gradient
    MIN_VIABLE_DELTA_T: float = 20.0
    EXCELLENT_DELTA_T: float = 24.0

    @classmethod
    def evaluate_site(
        cls,
        site_id: int,
        site_name: str,
        thermal_profile: TemperatureProfile,
        bathymetry_profile: BathymetryProfile,
        base_cable_score: float,
        base_risk_score: float,
    ) -> SiteOtecAssessment:
        """Execute cross-layer analytics to compile a comprehensive SiteOtecAssessment."""
        # 1. Calculate the pure thermodynamic physics
        physics = OtecAnalysisService.analyze_profile(thermal_profile)

        # 2. Calculate the spatial bathymetric penalty for logistics
        spatial_logistics_score = BathymetryAnalysisService.calculate_distance_score(
            bathymetry_profile
        )

        # 3. Modify the thermal score based on the delta T
        # Normalize the delta from 20°C (0.0) to 24°C (1.0)
        thermal_range = cls.EXCELLENT_DELTA_T - cls.MIN_VIABLE_DELTA_T
        raw_thermal_score = (physics.delta_t_c - cls.MIN_VIABLE_DELTA_T) / thermal_range
        normalized_thermal_score = max(0.0, min(1.0, raw_thermal_score))

        # 4. Form the components for the MCDA engine
        components = [
            ScoreComponent(name="thermal", score=normalized_thermal_score, weight=0.40),
            ScoreComponent(
                name="logistics", score=spatial_logistics_score, weight=0.25
            ),
            ScoreComponent(name="cable", score=base_cable_score, weight=0.15),
            ScoreComponent(name="risk", score=base_risk_score, weight=0.20),
        ]

        # 5. Calculate the integrated investment index
        investment_score = SiteScoringService.compute_index(components)

        return SiteOtecAssessment(
            site_id=site_id,
            site_name=site_name,
            physics_assessment=physics,
            bathymetry_profile=bathymetry_profile,
            investment_score=investment_score,
        )
