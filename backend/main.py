from typing import List, Union

from fastapi import Response,FastAPI

from .session import SessionManager, SessionRepository, SessionState
import sqlite3

app = FastAPI()

def connect_sqlite(path):
    return sqlite3.connect(path)
    

def make_session_manager(db_conn):
    session_repository = SessionRepository(db_conn)
    session_manager = SessionManager(session_repository)
    return session_manager

db_conn = connect_sqlite("purpose_pilot.db")
session_manager = make_session_manager(db_conn)


# 認証
@app.post("/api/auth/login")
def login(response: Response):
    pass

@app.post("/api/auth/logout")
def logout():
    pass


# ユーザー
@app.post("/api/users")
def register_user_account():
    pass

@app.get("/api/users/me")
def fetch_user_profile():
    pass

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

