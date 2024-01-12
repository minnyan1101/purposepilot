from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Review(BaseModel):
  review_id: str
  user_id: str
  purpose_id: str
  reviewed_at: str
  first_question_rating: float
  second_question_rating: float
  third_question_rating: float