from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, event, func, orm
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.sql.functions import current_timestamp

from logging import getLogger

# from app.core.utils import get_ulid

logger = getLogger(__name__)


class Base(DeclarativeBase):
    pass


class ModelBaseMixin:
    # id: Mapped[str] = mapped_column(String(32), primary_key=True, default=get_ulid)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=current_timestamp(),
        onupdate=func.utc_timestamp(),
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime)


class ModelBaseMixinWithoutDeletedAt:
    # id: Mapped[str] = mapped_column(String(32), primary_key=True, default=get_ulid)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=current_timestamp(),
        onupdate=func.utc_timestamp(),
    )


@event.listens_for(Session, "do_orm_execute")
def _add_filtering_deleted_at(execute_state: Any) -> None:
    """
    Applys logical delete (soft delete) automatically.
    You can get deleted data too if you query like the following:

    select(...).filter(...).execution_options(include_deleted=True).
    """
    if (
        execute_state.is_select
        and not execute_state.is_column_load
        and not execute_state.is_relationship_load
        and not execute_state.execution_options.get("include_deleted", False)
    ):
        execute_state.statement = execute_state.statement.options(
            orm.with_loader_criteria(  # ignore[mypy]
                ModelBaseMixin,
                lambda cls: cls.deleted_at.is_(None),
                include_aliases=True,
            ),
        )
