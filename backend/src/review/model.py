from pydantic import BaseModel, validator
from datetime import datetime


class Review(BaseModel):
    review_id: str
    user_id: str
    purpose_id: str
    reviewed_at: datetime
    first_question_rating: float
    second_question_rating: float
    third_question_rating: float


@validator('first_question_rating')
def check_first(cls,v):
  	if v > 1 or v <-1:
      raise ValueError('値が不正です。')
	  return v

