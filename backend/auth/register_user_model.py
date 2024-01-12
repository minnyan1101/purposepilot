from pydantic import BaseModel, validator

from .utils import validate_password, validate_user_id

class RegisterUser(BaseModel):
    user_id: str
    password: str
    password_confirm: str
    
    @validator("user_id")
    def _(cls, v):
        validate_user_id(v)
        
        return v
    
    @validator("password")
    def _(cls, v, values):
        validate_password(v)
        
        if "password_confirm" in values and values["password_confirm"] != v:
            raise ValueError("パスワードと確認用パスワードが一致しません")
        
        return v
    
    @validator("password_confirm")
    def _(cls, v, values):
        validate_password(v)
        
        return v
    