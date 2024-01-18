from pydantic import BaseModel, validator
from datetime import datetime
import re


e = re.compile('[a-z]+')
n = re.compile('[0-9]+')


class User(BaseModel):
    user_id: str
    created_at: datetime
    updated_at: datetime
    avater_image_url: str

    @validator('user_id')
    def check_length(cls, v):
        if not (0 < len(v) < 17):
            raise ValueError('値が不正です。1~16文字の英数字または_(アンダーバー)のみ使用してください。')
        return v

    @validator('user_id')
    def check_str(cls, v):
        if not (n.search(v) or e.search(v) or '_' in v):
            raise ValueError('値が不正です。1~16文字の英数字または_(アンダーバー)のみ使用してください。')
        return v

    def change_avater_image_url(self, new_url):
        self.avater_image_url = new_url

    def change_updated_at(self, now_datetime):
        self.updated_at = now_datetime
