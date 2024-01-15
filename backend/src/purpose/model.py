from pydantic import BaseModel, validator


class Purpose(BaseModel):
    purpose_id: int
    user_id: str
    title: str
    description: str
    created_at: str
    due_at: str
    status: str
    completed_at: str

    @validator('title')
    def check_title_length(cls, v, values):
        if not (len(v) < 50 and len(v) > 1):
            raise ValueError("目標タイトルは1文字以上50字以内で入力してください")
        return v

    @validator('description')
    def check_description_length(cls, v, values):
        if len(v) > 500:
            raise ValueError("目標内容は500字以内で入力してください")
        return v

    def change_title(self, new_title):
        self.title = new_title

    def change_description(self, new_description):
        self.description = new_description
