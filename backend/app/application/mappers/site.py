"""Data mappers translating Web Pydantic schemas into Application DTOs."""

from backend.app.application.dtos.site import CoordinatesDTO, SiteCreateDTO, SiteUpdateDTO
from backend.app.domain.exceptions import SpatialValidationError
# from backend.app.application.dtos.site import SiteCreateDTO, SiteUpdateDTO, CoordinatesDTO
from backend.app.schemas.site import (
    SiteCreate,
    SiteUpdate,
)  # Ваши Pydantic-схемы веб-слоя


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
        lat_sent = "latitude" in fields_set
        lon_sent = "longitude" in fields_set

        # Единое место для XOR-проверки. Защищает все входящие транспортные потоки.
        if lat_sent != lon_sent:
            raise SpatialValidationError(
                "Both longitude and latitude must be provided together for a spatial update."
            )

        coordinates = None
        if lat_sent and lon_sent:
            if payload.longitude is None or payload.latitude is None:
                raise SpatialValidationError(
                    "Geographic coordinates cannot be null values."
                )
            coordinates = CoordinatesDTO(
                longitude=payload.longitude, latitude=payload.latitude
            )

        return SiteUpdateDTO(
            name=payload.name if "name" in fields_set else None,
            description=payload.description if "description" in fields_set else None,
            status=payload.status if "status" in fields_set else None,
            coordinates=coordinates,
        )
