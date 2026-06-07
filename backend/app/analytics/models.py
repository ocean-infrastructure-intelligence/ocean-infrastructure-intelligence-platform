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
