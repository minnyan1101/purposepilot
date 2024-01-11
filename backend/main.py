from typing import List, Union

from fastapi import FastAPI

app = FastAPI()


# 認証
@app.post("/api/auth/login")
def login():
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
@app.get("/api/actions")
def fetch_actions_list(purpose_ids: list[str]):
    pass

@app.post("/api/actions")
def create_actions():
    pass

@app.get("/api/actions/{id}")
def fetch_actions(id: int):
    pass

@app.put("/api/actions/{id}")
def modify_actions(id: int):
    pass

@app.put("/api/actions/{id}")
def delete_actions(id: int):
    pass