from typing import List, Union

from fastapi import Response, FastAPI, Cookie, HTTPException, Depends

from .auth import AuthManager, AuthRepository, SessionRepository, SessionState, LoginUser
from .user import UserRepository, UserManager, User, RegisterUser
import sqlite3
import datetime

app = FastAPI()


def connect_sqlite(path):
    return sqlite3.connect(path, check_same_thread=False)


def make_auth_manager(db_conn):
    session_repository = SessionRepository(db_conn)
    auth_repository = AuthRepository(db_conn)
    auth_manager = AuthManager(session_repository, auth_repository)
    return auth_manager


def make_user_manager(db_conn):
    user_repository = UserRepository(db_conn)
    user_manager = UserManager(user_repository)
    return user_manager


db_conn = connect_sqlite("purpose_pilot.db")
auth_manager = make_auth_manager(db_conn)
user_manager = make_user_manager(db_conn)


def check_current_active_user(ssid: Union[str, None] = Cookie(default=None)):
    if not (ssid and auth_manager.is_authenticated(ssid)):
        raise HTTPException(
            status_code=401,
        )
    
    return auth_manager.find(ssid)


# 認証
@app.post("/api/auth/login")
def login(login_info: LoginUser, res: Response):
    try:
        session = auth_manager.login(login_info)
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
    else:
        res.set_cookie(
            key="ssid",
            value=session.session_id,
            expires=session.expired_at.astimezone(datetime.timezone.utc),
            secure=True,
            httponly=True,
            samesite="strict"
            )
        return {}


@app.post("/api/auth/logout")
def logout(res: Response, session: Union[SessionState, None] = Depends(check_current_active_user)):
    auth_manager.logout(session.session_id)
    res.set_cookie(
        key="ssid",
        value="",
        expires=datetime.datetime(1, 1, 1, tzinfo=datetime.timezone.utc),
        secure=True,
        httponly=True,
        samesite="strict"
        )
    return {}


# ユーザー
@app.post("/api/users")
def register_user_account(register_user: RegisterUser):
    if not auth_manager.register(register_user):
        raise HTTPException(
            409,
            "すでにユーザーが存在しています",
        )
    return {}


@app.get("/api/users/me")
def fetch_user_profile(session: Union[SessionState, None] = Depends(check_current_active_user)):
    return user_manager.get_profile(session.user_id)


@app.put("/api/users/me")
def modify_user_profile():
    pass


@app.delete("/api/users/me")
def delete_user_account():
    pass


# 目標
@app.get("/api/purposes")
def fetch_purpose_list(status: Union[str, None]):
    pass


@app.post("/api/purposes")
def create_purpose():
    pass


@app.get("/api/purposes/{id}")
def fetch_purpose(id: int):
    pass


@app.put("/api/purposes/{id}")
def modify_purpose(id: int):
    pass


@app.put("/api/purposes/{id}")
def delete_purpose(id: int):
    pass


# 行動
#行動の一覧の取得
@app.get("/api/actions",status_code=200)
def fetch_actions_list(purpose_ids: List[str], From:str, to:str):
    pass


@app.get("/api/actions",status_code=401)
def fetch_actions_list(purpose_ids: List[str], From:str, to:str):
    return {"error":"認証情報が不正です"}


@app.get("/api/actions",status_code=422)
def fetch_actions_list(purpose_ids: List[str], From:str, to:str):
    return {"error":"クエリパラメータの値が不正です"}


#行動記録の作成
@app.post("/api/actions",status_code=200)
def create_actions():
    pass


@app.post("/api/actions",status_code=401)
def create_actions():
    return {"error":"認証情報が不正です"}


@app.post("/api/actions",status_code=422)
def create_actions():
    return {"error":"クエリパラメータの値が不正です"}


#行動記録の取得
@app.get("/api/actions/{id}",status_code=200)
def fetch_actions(id: int):
    pass


@app.get("/api/actions/{id}",status_code=401)
def fetch_actions(id: int):
    return {"error":"認証情報が不正です"}


@app.get("/api/actions/{id}",status_code=404)
def fetch_actions(id: int):
    return {"error":"指定したaction_idは存在しません"}


#行動記録の修正
@app.put("/api/actions/{id}",status_code=200)
def modify_actions(id: int):
    pass


@app.post("/api/actions",status_code=401)
def modify_actions():
    return {"error":"認証情報が不正です"}


@app.post("/api/actions",status_code=422)
def modify_actions():
    return {"error":"指定したaction_idは存在しません"}


#行動記録の削除
@app.put("/api/actions/{id}",status_code=200)
def delete_actions(id: int):
    pass


@app.put("/api/actions/{id}",status_code=401)
def delete_actions(id: int):
    return {"error":"認証情報が不正です"}


@app.put("/api/actions/{id}",status_code=404)
def delete_actions(id: int):
    return {"error":"指定したaction_idは存在しません"}
