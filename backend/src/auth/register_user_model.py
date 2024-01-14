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

    @validator("password", "password_confirm")
    def check_password(cls, v):
        validate_password(v)

        return v

    @validator("password_confirm")
    def check_password_confirm(cls, v, values):
        if "password" in values and values["password"] != v:
            raise ValueError("パスワードと確認用パスワードが一致しません")

        return v
