"""Core database declarations and strict domain entity hierarchy for OIIP."""

from datetime import datetime
from sqlalchemy import DateTime, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from geoalchemy2.shape import to_shape
from geoalchemy2.elements import WKBElement


class Base(DeclarativeBase):
    """Abstract base class for all internal ORM metadata."""


class Entity(Base):
    """Abstract base entity enforcing a uniform Primary Key and audit timestamps."""

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Global auto-incremented surrogate primary key.",
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


class SpatialEntity(Entity):
    """Abstract marker entity for all ocean assets requiring PostGIS spatial support.

    Concrete geometry types (POINT, LINESTRING, POLYGON) must be defined in child models.
    """

    __abstract__ = True


class PointGeometryMixin:
    """Mixin for spatial entities that utilize a standard Point geometry.

    Provides safe Python properties to extract flat coordinates for Pydantic/API serialization.
    """

    # Expected to be implemented by the target model
    geom: Mapped[WKBElement | None]

    @property
    def longitude(self) -> float | None:
        """Extract longitude (X) from the Point geometry safely."""
        if self.geom is not None:
            return to_shape(self.geom).x  # type: ignore
        return None

    @property
    def latitude(self) -> float | None:
        """Extract latitude (Y) from the Point geometry safely."""
        if self.geom is not None:
            return to_shape(self.geom).y  # type: ignore
        return None
