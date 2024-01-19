from pydantic import BaseModel, validator
from datetime import datetime


class Review(BaseModel):
    review_id: int | None = None
    user_id: str
    purpose_id: int
    reviewed_at: datetime | None = None
    first_question_rating: float
    second_question_rating: float
    third_question_rating: float

    @validator('first_question_rating')
    def check_first(cls, v):
        if v > 1 or v < -1:
            raise ValueError('値が不正です。')
        return v

    @validator('second_question_rating')
    def check_second(cls, v):
        if v > 1 or v < -1:
            raise ValueError('値が不正です。')
        return v

    @validator('third_question_rating')
    def check_third(cls, v):
        if v > 1 or v < -1:
            raise ValueError('値が不正です。')
        return v

    def format_reviewed_at(self):
        return datetime.isoformat(self.reviewed_at)
