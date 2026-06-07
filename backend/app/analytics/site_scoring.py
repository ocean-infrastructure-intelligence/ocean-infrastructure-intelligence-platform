"""Core calculation engine for dynamic multi-criteria Site Suitability Indexing."""

from typing import List
from backend.app.analytics.models import SiteScore, ScoreComponent, ScoreGrade


class SiteScoringService:
    """Executes dynamic multi-criteria decision analysis (MCDA) for site triage."""

    # Критический порог отсечения: если базовые параметры ниже 0.3, площадка бракуется
    REJECT_THRESHOLD: float = 0.30

    @classmethod
    def compute_index(cls, components: List[ScoreComponent]) -> SiteScore:
        """Calculate weighted index across dynamic components and evaluate investment tier."""
        if not components:
            return SiteScore(components=[], overall_score=0.0, grade=ScoreGrade.REJECT)

        overall_score = 0.0
        total_weight = 0.0
        trigger_reject = False

        for comp in components:
            # Нормализуем входящие значения на всякий случай
            score = max(0.0, min(1.0, comp.score))

            # Накапливаем взвешенный скор
            overall_score += score * comp.weight
            total_weight += comp.weight

            # Проверяем критические маркеры (например, провал по термике или критический риск)
            if comp.name in ["thermal", "risk"] and score < cls.REJECT_THRESHOLD:
                trigger_reject = True

        # Корректируем общий балл, если сумма весов не равна 1.0 (защита от кривой конфигурации)
        if total_weight > 0:
            overall_score = overall_score / total_weight

        overall_score = round(overall_score, 3)

        # Определение категории
        if trigger_reject:
            grade = ScoreGrade.REJECT
        elif overall_score >= 0.80:
            grade = ScoreGrade.TIER_1
        elif overall_score >= 0.60:
            grade = ScoreGrade.TIER_2
        else:
            grade = ScoreGrade.TIER_3

        return SiteScore(
            components=components, overall_score=overall_score, grade=grade
        )
