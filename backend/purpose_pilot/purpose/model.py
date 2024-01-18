from datetime import datetime
from pydantic import BaseModel, validator

class Purpose(BaseModel):
    purpose_id: int | None = None
    user_id: str | None = None
    title: str
    description: str
    created_at: datetime | None = None
    due_at: datetime | None = None
    status: str
    completed_at: datetime | None = None

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
        self.completed_at = new.completed_at

    def is_completed(self):
        return self.status == 'completed'
    
    def asdict(self):
        if self.created_at is None:
            created_at = None
        else:
            created_at = self.created_at.isoformat()
            
        if self.due_at is None:
            due_at = None
        else:
            due_at = self.due_at.isoformat()
            
        if self.completed_at is None:
            completed_at = None
        else:
            completed_at = self.completed_at.isoformat()
        
        return {        
            "purpose_id": self.purpose_id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "created_at": created_at,
            "due_at": due_at,
            "is_completed": self.is_completed(),
            "completed_at": completed_at,
        }

