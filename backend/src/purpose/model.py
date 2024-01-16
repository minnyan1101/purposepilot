from datetime import datetime
from pydantic import BaseModel, validator

class Purpose(BaseModel):
    purpose_id: int | None = None
    user_id: str
    title: str
    description: str
    created_at: datetime | None = None
    due_at: datetime | None
    status: str
    completed_at: datetime | None

    @validator('title')
    def check_title_length(cls, v):
        if not (len(v) < 50 and len(v) > 1):
            raise ValueError("目標タイトルは1文字以上50字以内で入力してください")
        return v

    @validator('description')
    def check_description_length(cls, v):
        if len(v) > 500:
            raise ValueError("目標内容は500字以内で入力してください")
        return v
    
    @validator('status')
    def check_status(cls, v):
        if v not in ('completed', 'uncompleted'):
            raise ValueError("statusがcompleted, uncompletedではありません")
        return v
    
    @validator('completed_at')
    def check_completed_at(cls, v, values):
        if v is None and values['status'] == 'uncompleted':
            return v
        if v is not None and values['status'] == 'completed':
            return v
        raise ValueError("Statusとcompleted_atの状態が不正です")

    def update(self, new):
        self.title = new.title
        self.description = new.description
        self.due_at = new.due_at
        self.status = new.status
        self.completed_at = new.completed

    def is_active(self):
        return self.status == 'completed'

