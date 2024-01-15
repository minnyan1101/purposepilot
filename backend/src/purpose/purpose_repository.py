import sqlite3
from .model import Purpose
from datetime import datetime


class PurposeRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.db_conn = db_conn

    def find(self, purpose_id, user_id) -> Purpose:
        cur = self.conn.cursor()
        res = cur.execute(
            """
            SELECT purpose_id, user_id, title, description, created_at, due_at, is_completed, completed_at
                WHERE is_completed = ? AND user_id = ?
            """,
            (purpose_id, user_id)
            )

        result = res.fetchone()
        if result is None:
            return None
        cur.close()

        return Purpose(
            purpose_id=result[0],
            user_id=result[1],
            title=result[2],
            description=result[3],
            created_at=datetime.fromisoformat(result[4]),
            due_at=datetime.fromisoformat(result[5]),
            is_completed=result[6],
            completed_at=datetime.flomisoformat(result[7])
            )

    def findAll(self, user_id, show_completed: bool, show_uncompleted: bool) -> list[Purpose]:
        cur = self.conn.cursor()
        res = cur.execute(
            """
            SELECT purpose_id, user_id, title, description, created_at, due_at, is_completed, completed_at
                WHERE purpose_id = ? AND user_id = ? AND (is_completed == ? AND is_completed != ?)
            """,
            (user_id, show_completed, show_uncompleted)
            )
        result = res.fetchone()
        if result is None:
            return None
        cur.close()
        return Purpose(
            purpose_id=result[0],
            user_id=result[1],
            title=result[2],
            description=result[3],
            created_at=datetime.fromisoformat(result[4]),
            due_at=datetime.fromisoformat(result[5]),
            is_completed=result[6],
            completed_at=datetime.flomisoformat(result[7])
            )

    def delete(self, purpose_id, user_id) -> None:
        cur = self.conn.cursor()
        cur.execute(
            """
            DELETE FROM Purpose
                WHERE purpose_id = ? AND user_id = ?
            """,
            (
                purpose_id,
                user_id,
            )
        )
        self.conn.commit()

    def save(self, purpose: Purpose) -> Purpose:
        cur = self.conn.cursor()
        res = None
        if self.find(purpose.purpose_id, purpose.user_id):
            cur.execute(
                """
                UPDATE Purpose SET
                    purpose_id = :purpose_id,
                    user_id = :user_id,
                    title = :title,
                    description = :description,
                    created_at = :created_at,
                    due_at = :due_at,
                    is_completed = :is_completed,
                    completed_at = :completed_at

                    WHERE purpose_id = :purpose_id AND user_id = :user_id
                """,
                purpose.asdict()
                )
            res = purpose
        else:
            cur.execute(
                """
                INSERT INTO Purpose (
                    purpose_id,
                    user_id,
                    title,
                    description,
                    created_at,
                    due_at,
                    is_completed,
                    completed_at
                ) VALUES (
                    :purpose_id,
                    :user_id,
                    :title,
                    :description,
                    :created_at,
                    :due_at,
                    :is_completed,
                    :completed_at
                )
                """,
                purpose.asdict()
            )
            last_row = cur.execute(
                """
                SELECT purpose_id, user_id, title, description, created_at, due_at, is_completed, completed_at
                    WHERE ROWID = ?
                """,
                (cur.lastrowid,)
            )
            result = last_row.fetchone()
            res = Purpose(
                purpose_id=result[0],
                user_id=result[1],
                title=result[2],
                description=result[3],
                created_at=datetime.fromisoformat(result[4]),
                due_at=datetime.fromisoformat(result[5]),
                is_completed=result[6],
                completed_at=datetime.flomisoformat(result[7])
            )

        self.conn.commit()
        return res
