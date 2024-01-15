from datetime import datetime, timedelta
from pydantic import BaseModel, validator


class Action(BaseModel):
    action_id: int | None = None
    user_id: str | None = None
    purpose_id: int
    action_detail: str
    started_at: datetime
    finished_at: datetime

    @validator('action_detail')
    def check_length(cls, v, values):
        if not (len(v) < 500 and len(v) > 1):
            raise ValueError("行動内容は1文字以上500字以内で入力してください")
        return v

    def running_time(self) -> timedelta:
        return self.finished_at - self.started_at
    
    def update(self, new):
        self.action_detail = new.action_detail
    
    def asdict(self):
        return {
            "action_id": self.action_id,
            "user_id": self.user_id,
            "purpose_id": self.purpose_id,
            "action_detail": self.action_detail,
            "started_at": self.started_at.isoformat(),
            "finished_at": self.finished_at.isoformat(),
        }