import sqlite3
from datetime import datetime
from .model import User


class UserRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn

    def save(self, user: User) -> None:
        pass

    def find(self, user_id: str) -> User | None:
        cur = self.conn.cursor()
        res = cur.execute(
            '''
            SELECT user_id, created_at, updated_at, avater_image_url FROM User
                WHERE user_id = ?
            ''',
            (user_id,)
        )
        result = res.fetchone()
        if result is None:
            return None

        return User(
            user_id=result[0],
            created_at=datetime.fromisoformat(result[1]),
            updated_at=datetime.fromisoformat(result[2]),
            avater_image_url=result[3],
        )

    def delete(self, user_id: str) -> None:
        pass
