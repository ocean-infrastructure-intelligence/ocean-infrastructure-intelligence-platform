"""Data mappers translating Web Pydantic schemas into Application DTOs."""

from backend.app.application.dtos.site import (
    CoordinatesDTO,
    SiteCreateDTO,
    SiteUpdateDTO,
)
from backend.app.domain.exceptions import SpatialValidationError
from backend.app.schemas.site import SiteCreate, SiteUpdate


class SiteMapper:
    """Orchestrates transformation boundaries for the Site entity context."""

    @staticmethod
    def to_create_dto(payload: SiteCreate) -> SiteCreateDTO:
        """Map incoming API payload into strict creation DTO."""
        return SiteCreateDTO(
            name=payload.name,
            country_code=payload.country_code,
            longitude=payload.longitude,
            latitude=payload.latitude,
            description=payload.description,
        )

    @staticmethod
    def to_update_dto(payload: SiteUpdate) -> SiteUpdateDTO:
        """Map incoming API payload into strict update DTO, enforcing spatial invariants."""
        fields_set = payload.model_fields_set

        # Определяем, были ли координаты отправлены и не являются ли они пустыми
        lon_val = payload.longitude if "longitude" in fields_set else None
        lat_val = payload.latitude if "latitude" in fields_set else None

        # Жесткая XOR-защита: если заполнено только одно из полей
        if (lon_val is not None) != (lat_val is not None):
            raise SpatialValidationError(
                "Both longitude and latitude must be provided together for a spatial update."
            )

        coordinates = None
        if lon_val is not None and lat_val is not None:
            coordinates = CoordinatesDTO(longitude=lon_val, latitude=lat_val)

        return SiteUpdateDTO(
            name=payload.name if "name" in fields_set else None,
            description=payload.description if "description" in fields_set else None,
            status=payload.status if "status" in fields_set else None,
            coordinates=coordinates,
        )
