import sqlite3
from enum import StrEnum, auto

from .model import Purpose


class PurposeFilter(StrEnum):
    COMPLETED = auto()
    UNCOMPLETED = auto()
    ALL = auto()


class PurposeRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.db_conn = db_conn

    def find(self, purpose_id) -> Purpose:
        pass

    def findAll(self, user_id, status: PurposeFilter) -> list[Purpose]:
        pass

    def delete(self, user_id) -> None:
        pass

    def save(self, purpose: Purpose) -> Purpose:
        pass