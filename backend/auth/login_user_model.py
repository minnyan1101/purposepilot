from pydantic import BaseModel, validator

from .utils import validate_password, validate_user_id

class LoginUser(BaseModel):
    user_id: str
    password: str
    
    @validator("user_id")
    def _(cls, v):
        validate_user_id(v)
        
        return v
    
    @validator("password")
    def _(cls, v, values):
        validate_password(v)
    