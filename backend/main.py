"""Application entrypoint for Ocean Infrastructure Intelligence Platform (OIIP)."""

from typing import Any
from fastapi import FastAPI

from backend.app.api.site import router as site_router

app = FastAPI(
    title="Ocean Infrastructure Intelligence Platform",
    description="Backend API for managing spatial data of ocean infrastructure and OTEC sites.",
    version="0.1.0",
)


@app.get("/", summary="Health check")
def root() -> dict[str, Any]:
    """Health endpoint to verify the application status."""
    return {
        "application": "OIIP",
        "status": "running",
    }


# Include routers for application entities
app.include_router(site_router)
