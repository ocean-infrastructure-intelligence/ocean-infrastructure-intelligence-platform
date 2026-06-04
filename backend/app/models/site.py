from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from geoalchemy2 import Geometry

from backend.app.core.base import Base


class Site(Base):

    __tablename__ = "site"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(255)
    )

    country_code: Mapped[str] = mapped_column(
        String(2)
    )

    geom = mapped_column(
        Geometry(
            geometry_type="POINT",
            srid=4326
        )
    )
