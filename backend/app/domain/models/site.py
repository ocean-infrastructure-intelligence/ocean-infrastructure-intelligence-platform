"""A module describing spatial models of ocean infrastructure."""

import enum
from sqlalchemy import String, Enum, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, validates
from geoalchemy2 import Geometry
from geoalchemy2.elements import WKBElement

from backend.app.domain.base import SpatialEntity, PointGeometryMixin


class SiteStatus(str, enum.Enum):
    """Life cycle of a site."""

    CANDIDATE = "CANDIDATE"
    RESEARCH = "RESEARCH"
    VALIDATED = "VALIDATED"
    REJECTED = "REJECTED"
    SELECTED = "SELECTED"


class Site(SpatialEntity, PointGeometryMixin):
    """A site model for ocean infrastructure deployment (e.g., OTEC, Aquaculture)."""

    __tablename__ = "site"

    __table_args__ = (
        CheckConstraint("length(country_code) = 2", name="check_country_code_length"),
    )

    name: Mapped[str] = mapped_column(String(255))
    country_code: Mapped[str] = mapped_column(String(2), index=True)
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    # Специфичная для Site геометрия - строго POINT
    geom: Mapped[WKBElement | None] = mapped_column(
        Geometry(geometry_type="POINT", srid=4326, spatial_index=False),
        nullable=True,
    )

    status: Mapped[SiteStatus] = mapped_column(
        Enum(SiteStatus, name="sitestatus", native_enum=True),
        nullable=False,
        default=SiteStatus.CANDIDATE,
        server_default=SiteStatus.CANDIDATE.value,
    )

    @validates("country_code")
    def validate_country_code(self, _, value):
        """Ensure country code is exactly 2 characters and uppercase."""
        if not value or len(value) != 2:
            raise ValueError("Country code must be exactly 2 characters long.")
        return value.upper()
