import logging
import os
import typing

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from celery_utils.db.tables._base import BaseTable


LOGGER = logging.getLogger(__name__)


class SessionNotSet(Exception):
    def __init__(self) -> None:
        super().__init__("SessionNotSet: session is not set")


# will be used for sharing engine between all database objects.
_DB_URL: str = ""
_ENGINE: typing.Optional[Engine] = None


# setting db_url and create db engine based on this url.
def set_db_url(database_url: str) -> None:
    global _DB_URL, _ENGINE
    _DB_URL = database_url
    _ENGINE = create_engine(_DB_URL, pool_size=10, max_overflow=20)
    BaseTable.metadata.create_all(_ENGINE)


# creating new session on each request
def get_session() -> Session:
    if _ENGINE is None:
        raise SessionNotSet()
    session = sessionmaker(bind=_ENGINE)()
    return session
