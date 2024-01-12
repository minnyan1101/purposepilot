from fastapi import FastAPI
from pydantic import BaseModel ,validator
import re


e = re.compile('[a-z]+')
n = re.compile('[0-9]+')

class User(BaseModel):
  user_id : str
  created_at : str
  updated_at : str
  avater_image_url : str
  
  @validator('user_id')
  def check_length(cls, v, values):
      if not ( len(v) < 17 and len(v) > 0 ) :
        raise ValueError('値が不正です。1~16文字の英数字または_(アンダーバー)のみ使用してください。')
      return v
  
  @validator('user_id')  
  def check_str(cls, v, values):
    if not(n.search(v) and e.search(v) and '_' in v):
      raise ValueError('値が不正です。1~16文字の英数字または_(アンダーバー)のみ使用してください。')
    return v

    
  
app = FastAPI():
  


