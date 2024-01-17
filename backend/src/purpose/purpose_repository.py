import sqlite3
from datetime import datetime

from .model import Purpose


class PurposeRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn

    def find(self, purpose_id, user_id) -> Purpose | None:
        cur = self.conn.cursor()
        res = cur.execute(
            """
            SELECT purpose_id, user_id, title, description, created_at, due_at, is_completed, completed_at FROM Purpose
                WHERE purpose_id = ? AND user_id = ?
            """,
            (purpose_id, user_id)
            )

        result = res.fetchone()
        if result is None:
            return None
        cur.close()

        return convert_result_to_purpose(result)

    def findAll(self, user_id, show_completed: bool, show_uncompleted: bool) -> list[Purpose]:
        cur = self.conn.cursor()
        res = cur.execute(
            """
            SELECT purpose_id, user_id, title, description, created_at, due_at, is_completed, completed_at FROM Purpose
                WHERE user_id = ? AND (is_completed == ? OR is_completed != ?)
            """,
            (user_id, show_completed, show_uncompleted)
            )
        results = [convert_result_to_purpose(row) for row in res.fetchall()]
        cur.close()
        return results

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
                SELECT purpose_id, user_id, title, description, created_at, due_at, is_completed, completed_at FROM Purpose
                    WHERE ROWID = ?
                """,
                (cur.lastrowid,)
            )
            result = last_row.fetchone()
            res = convert_result_to_purpose(result)

        self.conn.commit()
        return res


def convert_result_to_purpose(result):
    if result[7] is None:
        completed_at = None
    else:
        completed_at = datetime.fromisoformat(result[7])
    
    return Purpose(
        purpose_id=result[0],
        user_id=result[1],
        title=result[2],
        description=result[3],
        created_at=datetime.fromisoformat(result[4]),
        due_at=datetime.fromisoformat(result[5]),
        status=convert_status(result[6]),
        completed_at=completed_at
    )


def convert_status(is_active):
    if is_active:
        return 'completed'
    else:
        return 'uncompleted'