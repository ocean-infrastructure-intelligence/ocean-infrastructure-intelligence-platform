"""Database configuration and session management.

Provides:

- SQLAlchemy engine
- Session factory
- FastAPI dependency for database sessions
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from backend.app.core.config import settings


# SQLAlchemy engine.
#
# echo=True:
#     Log all generated SQL statements.
#
# future=True:
#     Use SQLAlchemy 2.x behavior.
engine = create_engine(
    settings.database_url,
    echo=settings.debug,
    future=True,
)


# Factory for creating database sessions.
SessionLocal = sessionmaker(  # pylint: disable=invalid-name
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def get_db() -> Generator[Session, None, None]:
    """Provide a transactional database session.

    Used as a FastAPI dependency.

    Yields:
        Active SQLAlchemy session.
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
