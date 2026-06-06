"""Application service managing business orchestration for Ocean Infrastructure Sites."""

from sqlalchemy.orm import Session
from backend.app.application.dtos.site import SiteCreateDTO, SiteUpdateDTO
from backend.app.infrastructure.gis import create_wkb_point
from backend.app.domain.models.site import Site

from backend.app.application.services.base import BaseService


class SiteService(BaseService[Site]):
    """Pure domain processor operating exclusively on Type-Safe application DTOs."""

    model = Site

    def create(self, db: Session, dto: SiteCreateDTO) -> Site:
        """Orchestrate new Site execution from a validated application data profile."""
        site = Site(
            name=dto.name,
            country_code=dto.country_code,
            description=dto.description,
            geom=create_wkb_point(dto.longitude, dto.latitude),
        )
        return self._persist(db, site)

    def update(self, db: Session, site_id: int, dto: SiteUpdateDTO) -> Site | None:
        """Apply type-safe state mutations against an existing infrastructure Site."""
        db_site = self.get_by_id(db, site_id)
        if db_site is None:
            return None

        # Обрабатываем изменение геометрии (если блок координат присутствует)
        if dto.coordinates is not None:
            db_site.geom = create_wkb_point(
                dto.coordinates.longitude, dto.coordinates.latitude
            )

        # Никакого dict[str, Any] и setattr. Явный, безопасный накат полей с полной поддержкой IDE.
        if dto.name is not None:
            db_site.name = dto.name
        if dto.description is not None:
            db_site.description = dto.description
        if dto.status is not None:
            db_site.status = dto.status

        return self._commit_and_refresh(db, db_site)
