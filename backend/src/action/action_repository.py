import sqlite3
from .model import Action
from datetime import datetime


class ActionRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.db_conn = db_conn

    def find(self, purpose_id) -> Action:
        pass

    def findAll(self, user_id, to: datetime, _from: datetime) -> list[Action]:
        pass

    def delete(self, user_id) -> None:
        pass

    def save(self, purpose: Action) -> Action:
        pass