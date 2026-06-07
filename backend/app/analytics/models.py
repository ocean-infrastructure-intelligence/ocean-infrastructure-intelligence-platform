"""Domain data structures for Ocean Thermal Energy Conversion (OTEC) analytics.
Domain structures for multi-criteria site suitability intelligence."""

from dataclasses import dataclass
from enum import Enum
from typing import List


class ScoreGrade(str, Enum):
    """Qualitative grade assigned to a computed score."""

    TIER_1 = "TIER_1"  # Ideal location by all parameters
    TIER_2 = "TIER_2"  # Highly attractive with minor restrictions
    TIER_3 = "TIER_3"  # High risks or capital expenditures
    REJECT = "REJECT"  # Not suitable for investment


@dataclass(frozen=True)
class TemperatureProfile:
    """Raw oceanographic thermal observation profile at a specific coordinate."""

    surface_temperature_c: float  # Surface water temperature (usually 0-50m)
    deep_temperature_c: float  # Deep water temperature
    deep_water_depth_m: float  # Cold water depth (m)


@dataclass(frozen=True)
class OtecAssessment:
    """Immutable scientific payload capturing computed thermodynamic efficiency parameters."""

    delta_t_c: float
    carnot_efficiency_pct: float  # Store as a percentage (e.g., 7.94)
    net_efficiency_estimate_pct: float  # Store as a percentage (e.g., 2.38)


class OtecViabilityStatus(str, Enum):
    """Contextual classification of an ocean site's thermal energy potential."""

    EXCELLENT = "EXCELLENT"  # Excellent potential, high delta, and accessible depth
    VIABLE = "VIABLE"  # Commercially viable site
    MARGINAL = "MARGINAL"  # On the brink of breakeven, high technological risks
    NON_VIABLE = "NON_VIABLE"  # Unsuitable (too low delta or prohibitive depth)


@dataclass(frozen=True)
class ScoreComponent:
    """Dynamic, scalable component of the multi-criteria decision matrix."""

    name: str
    score: float  # From 0.0 to 1.0
    weight: float  # Share in the overall index (for example, 0.40)


@dataclass(frozen=True)
class SiteScore:
    """Immutable vector of dynamic score components and computed overall index."""

    components: List[ScoreComponent]
    overall_score: float
    grade: ScoreGrade

    def get_component_score(self, name: str) -> float | None:
        """Helper to quickly extract a specific score by its component name."""
        for comp in self.components:
            if comp.name == name:
                return comp.score
        return None


@dataclass(frozen=True)
class BathymetryProfile:
    """Distance profile from the site coordinate to key ocean depth contours (isobaths)."""

    distance_to_500m_m: float  # Distance to 500m depth in meters
    distance_to_1000m_m: float  # Distance to 1000m depth (critical for OTEC pipeline)
    distance_to_1500m_m: float  # Distance to 1500m depth


@dataclass(frozen=True)
class SiteOtecAssessment:
    """The core link tying a physical Site entity to its analytical and physics-based scores."""

    site_id: int
    site_name: str
    physics_assessment: OtecAssessment
    bathymetry_profile: BathymetryProfile
    investment_score: SiteScore


@dataclass(frozen=True)
class MonthlyThermalObservation:
    """Thermal parameters captured for a specific month (1-12)."""

    month: int
    surface_temperature_c: float


@dataclass(frozen=True)
class HydroclimatologyProfile:
    """Historical seasonal temperature profile aggregated from Copernicus/NOAA."""

    deep_temperature_c: (
        float  # Temperature at depth (usually stable all year round, ~4-5°C)
    )
    deep_water_depth_m: float  # Deep water depth
    monthly_observations: List[
        MonthlyThermalObservation
    ]  # Historical profile for 12 months

    def get_worst_month_profile(self) -> TemperatureProfile:
        """Extracts the profile with the minimum surface temperature
        (worst-case design scenario)."""
        if not self.monthly_observations:
            raise ValueError(
                "Hydroclimatology profile must contain monthly observations."
            )

        worst_obs = min(
            self.monthly_observations, key=lambda x: x.surface_temperature_c
        )
        return TemperatureProfile(
            surface_temperature_c=worst_obs.surface_temperature_c,
            deep_temperature_c=self.deep_temperature_c,
            deep_water_depth_m=self.deep_water_depth_m,
        )


@dataclass(frozen=True)
class OtecSuitabilityReport:
    """The ultimate analytical artifact summarizing physics, spatial, and financial triage."""

    site_id: int
    site_name: str
    worst_month_delta_t_c: float
    max_carnot_efficiency_pct: float
    estimated_net_efficiency_pct: float
    distance_to_1000m_isobath_m: float
    seafloor_accessibility_score: float
    seasonal_stability_factor: float
    overall_investment_index: float
    final_investment_grade: ScoreGrade


@dataclass(frozen=True)
class AiDatacenterProfile:
    """Requirements and constraints for co-locating an AI Compute Cluster with OTEC."""

    target_compute_power_mw: float # Planned data center capacity (e.g. 50 MW)
    distance_to_backbone_pop_km: (
        float  # Distance to the nearest backbone network (affects latency)
    )
    required_pue_limit: (
        float  # Maximum allowable PUE according to investor specifications (e.g., 1.2)
    )


@dataclass(frozen=True)
class AiDatacenterAssessment:
    """Computed thermodynamic and network metrics for the AI host component."""

    achievable_pue: float  # Calculated PUE taking into account OTEC ice water
    cooling_energy_savings_pct: float  # Calculated energy savings on cooling in %
    network_latency_penalty: float  # Penalty for distance from the network node (0.0 - 1.0)
