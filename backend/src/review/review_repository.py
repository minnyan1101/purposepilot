import sqlite3
from datetime import datetime
from .model import Review


class ReviewRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn

    def find(self, review_id, user_id, purpose_id) -> Review | None:
        cur = self.conn.cursor()
        res = cur.execute(
            '''
           SELECT review_id, user_id, purpose_id, reviewed_at, first_question_rating, second_question_rating,
           third_question_rating
                WHERE user_id = ? AND review_id = ? AND purpose_id = ?
            ''',
            (review_id,)
        )
        result = res.fetchone()
        if result is None:
            return None
        return Review(
            review_id=result[0],
            user_id=result[1],
            purpose_id=result[2],
            reviewed_at=datetime.fromisoformat(result[3]),
            first_question_rating=result[4],
            second_question_rating=result[5],
            third_question_rating=result[6]
        )

    def findAll(self, user_id, purpose_ids: 'tuple[str]', to: datetime, _from: datetime) -> 'list[Review]':
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
                Review(
                    review_id=result[0],
                    user_id=result[1],
                    purpose_id=result[2],
                    eviewed_at=datetime.fromisoformat(result[3]),
                    first_question_rating=result[4],
                    second_question_rating=result[5],
                    third_question_rating=result[6]
                    )
                )

        cur.close()
        return results
