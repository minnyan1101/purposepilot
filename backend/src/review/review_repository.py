import sqlite3
from datetime import datetime
from .model import Review


class ReviewRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn

    def save(self, review: Review) -> None:
        pass

    def find(self, review_id, user_id, purpose_id) -> Review | None:
        cur = self.conn.cursor()
        res = cur.execute(
            '''
           SELECT review_id, user_id, purpose_id, reviewed_at, first_question_rating, second_question_rating,
           third_question_rating
                WHERE user_id = ?
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
