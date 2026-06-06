"""Base generic service layer infrastructure handling entity persistence layer."""

from typing import Generic, TypeVar, cast
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from backend.app.domain.base import Entity

T = TypeVar("T", bound=Entity)


class BaseService(Generic[T]):
    """Generic foundation providing clean data access and atomic transaction isolation."""

    model: type[T]

    def _commit_and_refresh(self, db: Session, obj: T) -> T:
        try:
            db.commit()
            db.refresh(obj)
            return obj
        except SQLAlchemyError:
            db.rollback()
            raise

    def _persist(self, db: Session, obj: T) -> T:
        """Low-level database write primitive. Replaces ambiguous public 'create'."""
        db.add(obj)
        return self._commit_and_refresh(db, obj)

    def get_all(self, db: Session, limit: int = 100, offset: int = 0) -> list[T]:
        """Fetches a paginated list of entities. Returns empty list if no records found."""
        stmt = select(self.model).order_by(self.model.id).limit(limit).offset(offset)
        return cast(list[T], db.scalars(stmt).all())

    def get_by_id(self, db: Session, obj_id: int) -> T | None:
        """Fetches an entity by its unique identifier. Returns None if not found."""
        return db.get(self.model, obj_id)

    def delete(self, db: Session, obj_id: int) -> bool:
        """Deletes an entity by ID. Returns True if deletion was successful, False if not found."""
        obj = self.get_by_id(db, obj_id)
        if obj is None:
            return False
        db.delete(obj)
        try:
            db.commit()
            return True
        except SQLAlchemyError:
            db.rollback()
            raise
