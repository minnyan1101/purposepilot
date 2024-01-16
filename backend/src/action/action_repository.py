import sqlite3
from .model import Action
from datetime import datetime


class ActionRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn

    def find(self, action_id, user_id) -> Action | None:
        cur = self.conn.cursor()
        res = cur.execute(
            """
            SELECT action_id, user_id, purpose_id, action_detail, started_at, finished_at FROM Action
                WHERE action_id = ? AND user_id = ?
            """,
            (action_id, user_id)
            )

        result = res.fetchone()
        if result is None:
            return None

        cur.close()

        return Action(
            action_id=result[0],
            user_id=result[1],
            purpose_id=result[2],
            action_detail=result[3],
            started_at=datetime.fromisoformat(result[4]),
            finished_at=datetime.fromisoformat(result[5]),
            )

    def findAll(self, user_id, purpose_ids: 'tuple[str]', to: datetime, _from: datetime) -> 'list[Action]':
        if not purpose_ids:
            return []

        cur = self.conn.cursor()
        res = cur.execute(
            f"""
            SELECT action_id, user_id, purpose_id, action_detail, started_at, finished_at FROM Action
            WHERE purpose_id IN ( {','.join(['?'] * len(purpose_ids))} ) AND user_id = ? AND started_at BETWEEN ? AND ?;
            """,
            (
                *purpose_ids,
                user_id,
                to.isoformat(),
                _from.isoformat()
            )
            )

        results = []
        for result in res.fetchall():
            results.append(
                Action(
                    action_id=result[0],
                    user_id=result[1],
                    purpose_id=result[2],
                    action_detail=result[3],
                    started_at=datetime.fromisoformat(result[4]),
                    finished_at=datetime.fromisoformat(result[5]),
                    )
                )

        cur.close()
        return results

    def user_purpose_ids(self, user_id: str) -> list[str]:
        cur = self.conn.cursor()
        res = cur.execute(
            """
            SELECT purpose_id FROM Purpose
                WHERE user_id = ?;
            """,
            (
                user_id,
            )
            )
        results = []
        for result in res.fetchall():
            results.append(result[0])

        return results

    def delete(self, action_id, user_id) -> None:
        cur = self.conn.cursor()
        cur.execute(
            """
            DELETE FROM Action
                WHERE action_id = ? AND user_id = ?
            """,
            (
                action_id,
                user_id,
            )
        )
        self.conn.commit()

    def save(self, action: Action) -> Action:
        cur = self.conn.cursor()
        res = None
        if self.find(action.action_id, action.user_id):
            cur.execute(
                """
                UPDATE Action SET
                    action_id = :action_id,
                    user_id = :user_id,
                    purpose_id = :purpose_id,
                    action_detail = :action_detail,
                    started_at = :started_at,
                    finished_at = :finished_at

                    WHERE action_id = :action_id AND user_id = :user_id
                """,
                action.asdict()
                )
            res = action
        else:
            cur.execute(
                """
                INSERT INTO Action (
                    user_id,
                    purpose_id,
                    action_detail,
                    started_at,
                    finished_at
                ) VALUES (
                    :user_id,
                    :purpose_id,
                    :action_detail,
                    :started_at,
                    :finished_at
                )
                """,
                action.asdict()
            )
            last_row = cur.execute(
                """
                SELECT action_id, user_id, purpose_id, action_detail, started_at, finished_at FROM Action
                    WHERE ROWID = ?
                """,
                (cur.lastrowid,)
            )
            result = last_row.fetchone()
            res = Action(
                action_id=result[0],
                user_id=result[1],
                purpose_id=result[2],
                action_detail=result[3],
                started_at=datetime.fromisoformat(result[4]),
                finished_at=datetime.fromisoformat(result[5]),
            )

        self.conn.commit()
        return res
