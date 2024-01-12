from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel,validator

class Action(BaseModel):
  action_id: str
  user_id: str
  purpose_id: str
  action_detail: str
  started_at: str
  finished_at: str
  
  @validator('action_datail')
  def check_length(cls, v, values):
      if not (len(v) < 500 and len(v) > 1):
          raise ValueError("行動内容は1文字以上500字以内で入力してください")
      return v
      
app=FastAPI()