import sqlite3
from datetime import datetime
from .model import Review


class ReviewRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn

    def get_active_purpose_ids(self, user_id) -> list[int]:
        cur = self.conn.cursor()
        res = cur.execute(
            """
            SELECT purpose_id FROM Purpose
                WHERE user_id = ? AND is_completed = false
            """,
            (user_id,),
        )
        result = res.fetchall()
        ids = []
        for i in result:
            ids.append(i[0])
        return ids

    def find(self, review_id) -> Review | None:
        cur = self.conn.cursor()
        res = cur.execute(
            """
           SELECT review_id, user_id, purpose_id, reviewed_at, first_question_rating, second_question_rating,
           third_question_rating
                WHERE user_id = ? AND review_id = ? AND purpose_id = ?
            """,
            (review_id,),
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
            third_question_rating=result[6],
        )

    def findAll(
        self, user_id, purpose_ids: list[int], to: datetime, _from: datetime
    ) -> list[Review]:
        if not purpose_ids:
            return []

        cur = self.conn.cursor()
        res = cur.execute(
            f"""
            SELECT review_id, user_id, purpose_id, reviewed_at, first_question_rating, second_question_rating, third_question_rating FROM Review
            WHERE purpose_id IN ( {','.join(['?'] * len(purpose_ids))} ) AND user_id = ? AND reviewed_at BETWEEN ? AND ?;
            """,
            (*purpose_ids, user_id, to.isoformat(), _from.isoformat()),
        )

        results = []
        for result in res.fetchall():
            results.append(
                Review(
                    review_id=result[0],
                    user_id=result[1],
                    purpose_id=result[2],
                    reviewed_at=datetime.fromisoformat(result[3]),
                    first_question_rating=result[4],
                    second_question_rating=result[5],
                    third_question_rating=result[6],
                )
            )

        cur.close()
        return results

    def insert(self, review: Review):
        cur = self.conn.cursor()
        response = cur.execute(
            """
            INSERT INTO Review (user_id, purpose_id, reviewed_at, first_question_rating, second_question_rating, third_question_rating)
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (
                review.user_id,
                review.purpose_id,
                review.format_reviewed_at(),
                review.first_question_rating,
                review.second_question_rating,
                review.third_question_rating,
            ),
        )

        row_id = response.lastrowid
        print(row_id)

        new_item_response = cur.execute(
            """
            SELECT
                review_id,
                user_id,
                purpose_id,
                reviewed_at,
                first_question_rating,
                second_question_rating,
                third_question_rating
             FROM Review
                WHERE (
                    rowid = ?
                )
            """,
            (row_id,),
        )
        new_item = new_item_response.fetchone()

        new_review = Review(
            review_id=new_item[0],
            user_id=new_item[1],
            purpose_id=new_item[2],
            reviewed_at=datetime.fromisoformat(new_item[3]),
            first_question_rating=new_item[4],
            second_question_rating=new_item[5],
            third_question_rating=new_item[6],
        )

        return new_review

    def update(self, review: Review) -> Review:
        cur = self.conn.cursor()

        cur.execute(
            """
            UPDATE Review 
                SET 
                    user_id=?,
                    purpose_id=?,
                    reviewed_at=?,
                    first_question_rating=?,
                    second_question_rating=?,
                    third_question_rating=?
                WHERE
                    review_id=?
            """,
            (
                review.user_id,
                review.purpose_id,
                review.format_reviewed_at(),
                review.first_question_rating,
                review.second_question_rating,
                review.third_question_rating,
                review.review_id,
            ),
        )
        self.conn.commit()
        res = self.find(review.review_id)
        cur.close()
        return res

    def save(self, review: Review) -> Review:
        if review.review_id is None:
            return self.insert(review)

        else:
            return self.update(review)
