"""Global domain exceptions for the OIIP ecosystem."""


class SpatialValidationError(ValueError):
    """Raised when spatial coordinate updates or geometries violate GIS business rules."""
    