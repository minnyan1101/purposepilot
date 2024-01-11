from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
  user_id : str
  created_at : str
  updated_at : str
  avater_image_url : str
class Purpose(BaseModel):
  purpose_id: str
  user_id: str
  title: str
  description: str
  created_at: str
  due_at: str
  status: str
  completed_at: str
class Action(BaseModel):
  action_id: str
  user_id: str
  purpose_id: str
  action_detail: str
  run_duration_sec: int
  started_at: str
  finished_at: str
class Review(BaseModel):
  review_id: str
  user_id: str
  purpose_id: str
  reviewed_at: str
  first_question_rating: float
  second_question_rating: float
  third_question_rating: float

  