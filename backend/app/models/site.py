"""A module for describing spatial models of ocean infrastructure.

Contains SQLAlchemy ORM models for working with sites, their geographic coordinates, and lifecycle.
"""

import enum
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Enum, CheckConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, validates
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from backend.app.core.base import Base


class SiteStatus(str, enum.Enum):
    """Life cycle of a site."""

    CANDIDATE = "CANDIDATE"
    RESEARCH = "RESEARCH"
    VALIDATED = "VALIDATED"
    REJECTED = "REJECTED"
    SELECTED = "SELECTED"


class Site(Base):
    """A site model for ocean infrastructure deployment.

    Stores metadata about potential locations, including their geographic
    location (PostGIS POINT), validation status, and timestamps.
    """

    __tablename__ = "site"

    __table_args__ = (
        CheckConstraint("length(country_code) = 2", name="check_country_code_length"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    # Updated with index=True in the previous migration
    country_code: Mapped[str] = mapped_column(String(2), index=True)

    geom = mapped_column(
        Geometry(geometry_type="POINT", srid=4326, spatial_index=False)
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
        comment="OTEC candidate. Near deep-water coast. Fiber landing nearby.",
    )

    status: Mapped[SiteStatus] = mapped_column(
        Enum(SiteStatus, name="sitestatus", native_enum=True),
        nullable=False,
        default=SiteStatus.CANDIDATE,
        server_default=SiteStatus.CANDIDATE.value,
        comment="Lifecycle status: candidate, research, validated, rejected, selected",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    )

    @validates("country_code")
    def validate_country_code(self, _, value):
        """Validate country code before saving."""
        if not value or len(value) != 2:
            raise ValueError(
                f"Country code '{value}' must be exactly 2 characters long (ISO 3166-1 alpha-2)."
            )
        return value.upper()

    # --- СВОЙСТВА ГЕОМЕТРИИ ДЛЯ PYTHON / PYDANTIC ---

    @property
    def longitude(self) -> float | None:
        """Extract longitude (X) from the PostGIS spatial geometry object."""
        if self.geom is not None:
            shape = to_shape(self.geom)
            return shape.x  # type: ignore
        return None

    @property
    def latitude(self) -> float | None:
        """Extract latitude (Y) from the PostGIS spatial geometry object."""
        if self.geom is not None:
            shape = to_shape(self.geom)
            return shape.y  # type: ignore
        return None
