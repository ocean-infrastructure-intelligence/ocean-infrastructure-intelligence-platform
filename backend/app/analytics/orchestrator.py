"""Orchestrates pure domain entities, bathymetry constraints, and MCDA scoring rules."""

from backend.app.analytics.models import (
    HydroclimatologyProfile,
    BathymetryProfile,
    ScoreComponent,
    SiteOtecAssessment,
)
from backend.app.analytics.otec import OtecAnalysisService
from backend.app.analytics.site_scoring import SiteScoringService
from backend.app.analytics.bathymetry import BathymetryAnalysisService
from backend.app.analytics.models import OtecSuitabilityReport


class SiteIntelligenceOrchestrator:
    """High-level domain orchestrator compiling multi-disciplinary site metrics."""

    # Business thresholds for normalizing the temperature gradient
    MIN_VIABLE_DELTA_T: float = 20.0
    EXCELLENT_DELTA_T: float = 24.0

    # Замените метод evaluate_site в backend/app/analytics/orchestrator.py

    @classmethod
    def evaluate_site_climatology(
        cls,
        site_id: int,
        site_name: str,
        hydro_profile: HydroclimatologyProfile,
        bathymetry_profile: BathymetryProfile,
        base_cable_score: float,
        base_risk_score: float,
    ) -> SiteOtecAssessment:
        """Execute seasonal climate-aware analytics to compile SiteOtecAssessment."""

        # 1. Extract the worst-case scenario (conservative engineering approach for OTEC)
        worst_case_profile = hydro_profile.get_worst_month_profile()
        physics = OtecAnalysisService.analyze_profile(worst_case_profile)

        # 2. Calculate the spatial bathymetric penalty for logistics
        spatial_logistics_score = BathymetryAnalysisService.calculate_distance_score(
            bathymetry_profile
        )

        # 3. Thermal score based on the worst month + seasonal stability coefficient
        thermal_range = cls.EXCELLENT_DELTA_T - cls.MIN_VIABLE_DELTA_T
        raw_thermal_score = (physics.delta_t_c - cls.MIN_VIABLE_DELTA_T) / thermal_range

        stability_factor = OtecAnalysisService.evaluate_climatology_stability(
            hydro_profile
        )

        # Integral thermal indicator with climate stability consideration
        final_thermal_score = max(0.0, min(1.0, raw_thermal_score * stability_factor))

        # 4. Form the components
        components = [
            ScoreComponent(name="thermal", score=final_thermal_score, weight=0.40),
            ScoreComponent(
                name="logistics", score=spatial_logistics_score, weight=0.25
            ),
            ScoreComponent(name="cable", score=base_cable_score, weight=0.15),
            ScoreComponent(name="risk", score=base_risk_score, weight=0.20),
        ]

        # 5. Calculate the index
        investment_score = SiteScoringService.compute_index(components)

        return SiteOtecAssessment(
            site_id=site_id,
            site_name=site_name,
            physics_assessment=physics,
            bathymetry_profile=bathymetry_profile,
            investment_score=investment_score,
        )

    @classmethod
    def compile_suitability_report(
        cls,
        site_id: int,
        site_name: str,
        hydro_profile: HydroclimatologyProfile,
        bathymetry_profile: BathymetryProfile,
        base_cable_score: float,
        base_risk_score: float,
    ) -> OtecSuitabilityReport:
        """Execute all engines and build the final investor-ready suitability report."""
        # Прогоняем через наш существующий климатический оркестратор
        assessment = cls.evaluate_site_climatology(
            site_id=site_id,
            site_name=site_name,
            hydro_profile=hydro_profile,
            bathymetry_profile=bathymetry_profile,
            base_cable_score=base_cable_score,
            base_risk_score=base_risk_score,
        )

        inv_score = assessment.investment_score
        stability = OtecAnalysisService.evaluate_climatology_stability(hydro_profile)

        return OtecSuitabilityReport(
            site_id=site_id,
            site_name=site_name,
            worst_month_delta_t_c=assessment.physics_assessment.delta_t_c,
            max_carnot_efficiency_pct=assessment.physics_assessment.carnot_efficiency_pct,
            estimated_net_efficiency_pct=assessment.physics_assessment.net_efficiency_estimate_pct,
            distance_to_1000m_isobath_m=bathymetry_profile.distance_to_1000m_m,
            seafloor_accessibility_score=inv_score.get_component_score("logistics")
            or 0.0,
            seasonal_stability_factor=stability,
            overall_investment_index=inv_score.overall_score,
            final_investment_grade=inv_score.grade,
        )
