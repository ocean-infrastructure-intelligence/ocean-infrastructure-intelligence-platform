"""Services for spatial bathymetry validation and slope penalization metrics."""

from backend.app.analytics.models import BathymetryProfile


class BathymetryAnalysisService:
    """Evaluates seafloor morphology constraints and pipe-laying distance penalties."""

    MAX_ECONOMIC_DISTANCE_M: float = 10000.0  # 10 km is the limit for laying CWP
    IDEAL_DISTANCE_M: float = 1000.0  # 1 km — ideal steep slope

    @classmethod
    def calculate_distance_score(cls, profile: BathymetryProfile) -> float:
        """Apply a non-linear penalty function to the distance to the 1000m isobath.

        Returns a normalized score between 0.0 (impossible) and 1.0 (perfect).
        """
        dist = profile.distance_to_1000m_m

        if dist <= cls.IDEAL_DISTANCE_M:
            return 1.0
        if dist >= cls.MAX_ECONOMIC_DISTANCE_M:
            return 0.0

        # Linear decay between the ideal and critical distances
        normalized_penalty = (dist - cls.IDEAL_DISTANCE_M) / (
            cls.MAX_ECONOMIC_DISTANCE_M - cls.IDEAL_DISTANCE_M
        )
        return round(1.0 - normalized_penalty, 2)
