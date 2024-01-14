import sqlite3

from .user_model import User, convert_user


class AuthRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn

    def find(self, user_id: str) -> User:
        res = None
        result = self.conn.execute(
            """
                SELECT user_id, hash, created_at, updated_at, avater_image_url FROM User
                    WHERE user_id = ?
            """,
            (user_id, )
            )
        res = result.fetchone()

        if res is None:
            return None
        user = convert_user(*res)

        return user

    def save(self, user: User):
        cur = self.conn.cursor()
        try:
            cur.execute(
                '''
                INSERT INTO User
                    VALUES (:user_id, :hash, :created_at, :updated_at, :avater_image_url)
                ''',
                user.asdict()
            )

        except sqlite3.IntegrityError:
            self.conn.rollback()
            raise ValueError("ユーザーIDがすでに存在しています")

        else:
            self.conn.commit()

        finally:
            cur.close()
