"""A module for describing spatial models of ocean infrastructure.

Contains SQLAlchemy ORM models for working with sites, their geographic coordinates, and lifecycle.
"""

import enum
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Enum, CheckConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, validates
from geoalchemy2 import Geometry
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
    country_code: Mapped[str] = mapped_column(String(2))

    # Note the spatial_index=False parameter.
    # As we learned earlier, this will prevent Alembic from trying to create the GIST index again.
    geom = mapped_column(
        Geometry(geometry_type="POINT", srid=4326, spatial_index=False)
    )

    # Description with a comment for the database
    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
        comment="OTEC candidate. Near deep-water coast. Fiber landing nearby.",
    )

    # Status with Enum validation and lifecycle comment
    status: Mapped[SiteStatus] = mapped_column(
        Enum(SiteStatus, name="sitestatus", native_enum=True),
        nullable=False,
        default=SiteStatus.CANDIDATE,
        server_default=SiteStatus.CANDIDATE.value,
        comment="Lifecycle status: candidate, research, validated, rejected, selected",
    )

    # Handled by PostgreSQL server-side using CURRENT_TIMESTAMP
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    # Handled by PostgreSQL for creation, and Python lambda for updates
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        # onupdate вычисляется на стороне сервера БД при каждом обновлении строки
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
