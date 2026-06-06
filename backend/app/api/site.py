"""REST API endpoints for Site entity."""

from typing import Sequence
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from backend.app.application.mappers.site import SiteMapper
from backend.app.domain.exceptions import SpatialValidationError
from backend.app.infrastructure.database import get_db
from backend.app.domain.models.site import Site
from backend.app.schemas.site import SiteCreate, SiteRead, SiteUpdate
from backend.app.application.services.site_service import SiteService
from backend.app.core.constants import MAX_PAGE_SIZE, DEFAULT_PAGE_SIZE

router = APIRouter(
    prefix="/sites",
    tags=["Sites"],
)


def get_site_service() -> SiteService:
    """Dependency provider for SiteService instance."""
    return SiteService()


@router.get(
    "",
    response_model=list[SiteRead],
    summary="Get all sites",
)
def get_sites(
    db: Session = Depends(get_db),
    service: SiteService = Depends(get_site_service),
    # Fail-Fast подход: валидация происходит на уровне входящих параметров
    limit: int = Query(
        default=DEFAULT_PAGE_SIZE,
        ge=1,
        le=MAX_PAGE_SIZE,
        description="Maximum number of records to return",
    ),
    offset: int = Query(default=0, ge=0, description="Number of records to skip"),
) -> Sequence[Site]:
    """Return ordered and paginated sites from the system."""
    return service.get_all(db, limit=limit, offset=offset)


@router.get(
    "/{site_id}",
    response_model=SiteRead,
    summary="Get site by ID",
)
def get_site(
    site_id: int,
    db: Session = Depends(get_db),
    service: SiteService = Depends(get_site_service),
):
    """Return a single site by its unique identifier."""
    site = service.get_by_id(db, site_id)
    if site is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Site not found",
        )
    return site


@router.post(
    "",
    response_model=SiteRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new site",
)
def create_site(
    payload: SiteCreate,
    db: Session = Depends(get_db),
    service: SiteService = Depends(get_site_service),
):
    """Create a new ocean infrastructure site and generate PostGIS geometry."""
    dto = SiteMapper.to_create_dto(payload)
    return service.create(db, dto)


@router.patch(
    "/{site_id}",
    response_model=SiteRead,
    summary="Partially update a site",
)
def update_site(
    site_id: int,
    payload: SiteUpdate,
    db: Session = Depends(get_db),
    service: SiteService = Depends(get_site_service),
):
    """Partially update an existing ocean infrastructure site by its ID."""
    try:
        # Трансляция + Валидация инвариантов на уровне маппера приложения
        dto = SiteMapper.to_update_dto(payload)
        db_site = service.update(db, site_id=site_id, dto=dto)
    except SpatialValidationError as err:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(err)
        ) from err

    if db_site is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Site with ID {site_id} not found.",
        )

    return db_site


@router.delete(
    "/{site_id}",
    summary="Delete site",
)
def delete_site(
    site_id: int,
    db: Session = Depends(get_db),
    service: SiteService = Depends(get_site_service),
):
    """Delete site from the system with rollback protection."""
    if not service.delete(db, site_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Site not found",
        )
    return {"message": "Site deleted"}
