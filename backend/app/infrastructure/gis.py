"""GIS utilities and spatial data transformations for ocean infrastructure data."""

from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from backend.app.core.constants import SRID_WGS84


def create_wkb_point(
    longitude: float, latitude: float, srid: int = SRID_WGS84
) -> WKBElement:
    """Create a PostGIS WKBElement Point from longitude and latitude."""
    spatial_point = Point(longitude, latitude)
    return from_shape(spatial_point, srid=srid)
