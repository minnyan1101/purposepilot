from typing import Union

from fastapi import Response, FastAPI, Cookie, HTTPException, Depends, status

from purpose_pilot.auth import AuthManager, AuthRepository, SessionRepository, SessionState, LoginUser
from purpose_pilot.review import ReviewRepository, Review, ReviewManager
from purpose_pilot.user import UserRepository, UserManager, User, RegisterUser
from purpose_pilot.purpose import Purpose, PurposeRepository, PurposeManager, PurposeFilter
from purpose_pilot.action import Action, ActionRepository, ActionManager
import sqlite3
import datetime

app = FastAPI()


def connect_sqlite(path):
    conn = sqlite3.connect(path, check_same_thread=False)
    # conn.set_trace_callback(print)
    return conn


db_conn = connect_sqlite("purpose_pilot.db")

session_repository = SessionRepository(db_conn)
auth_repository = AuthRepository(db_conn)
auth_manager = AuthManager(session_repository, auth_repository)

user_repository = UserRepository(db_conn)
user_manager = UserManager(user_repository)


purpose_repository = PurposeRepository(db_conn)
purpose_manager = PurposeManager(purpose_repository)


action_repository = ActionRepository(db_conn)
action_manager = ActionManager(action_repository)


review_repository = ReviewRepository(db_conn)
review_manager = ReviewManager(review_repository, purpose_repository)


def check_current_active_user(ssid: Union[str, None] = Cookie(default=None)):
    if not (ssid and auth_manager.is_authenticated(ssid)):
        raise HTTPException(
            status_code=401,
        )
    result = auth_manager.find(ssid)
    return result


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
def logout(res: Response, session: SessionState = Depends(check_current_active_user)):
    if session is None:
        return {}

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
@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def register_user_account(register_user: RegisterUser):
    if not auth_manager.register(register_user):
        raise HTTPException(
            409,
            "すでにユーザーが存在しています",
        )
    return {}


@app.get("/api/users/me")
def fetch_user_profile(session: SessionState = Depends(check_current_active_user)):
    return user_manager.get_profile(session.user_id)


@app.put("/api/users/me")
def modify_user_profile(user: User, session: SessionState = Depends(check_current_active_user)):
    user = user_manager.change_profile(user, session.user_id)
    return user


@app.delete("/api/users/me")
def delete_user_account(session: SessionState = Depends(check_current_active_user)):
    user_manager.delete(session.user_id)


# 目標
@app.get("/api/purposes")
def fetch_purpose_list(status: Union[str, None] = "all",
                       session: SessionState = Depends(check_current_active_user)):
    if status == PurposeFilter.COMPLETED:
        status = PurposeFilter.COMPLETED

    elif status == PurposeFilter.UNCOMPLETED:
        status = PurposeFilter.UNCOMPLETED

    else:
        status = PurposeFilter.ALL

    purposes = purpose_manager.get_purpose_list(session.user_id, status)
    return purposes


# 目標の作成
@app.post("/api/purposes", status_code=status.HTTP_201_CREATED)
def create_purpose(purpose: Purpose, session: SessionState = Depends(check_current_active_user)):
    purpose.purpose_id = None
    purpose.user_id = session.user_id

    try:
        purpose = purpose_manager.new_purpose(
            current_user=session.user_id,
            title=purpose.title,
            description=purpose.description,
            due_at=purpose.due_at,
            status=purpose.status,
            completed_at=purpose.completed_at
            )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )
    return purpose


@app.get("/api/purposes/{id}")
def fetch_purpose(id: int, session: SessionState = Depends(check_current_active_user)):
    purpose = purpose_manager.get_purpose(id, session.user_id)
    if purpose is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="この目標IDは存在しません"
        )
    return purpose


@app.put("/api/purposes/{id}")
def modify_purpose(id: int, purpose: Purpose, session: SessionState = Depends(check_current_active_user)):
    if id != purpose.purpose_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="パスで指定されたIDとリクエストボディのIDが異なっています"
        )
    purpose = purpose_manager.change_purpose(purpose, session.user_id)
    return purpose


@app.delete("/api/purposes/{id}")
def delete_purpose(id: int, session: SessionState = Depends(check_current_active_user)):
    purpose_manager.delete_purpose(id, session.user_id)


# 行動
# 行動の一覧の取得
@app.get("/api/actions", status_code=200)
def fetch_actions_list(to: str | None = None, _from: str | None = None, purpose_ids: int = None, session: SessionState = Depends(check_current_active_user)):
    to = datetime.datetime.fromisoformat(to)
    _from = datetime.datetime.fromisoformat(_from)
    
    if isinstance(purpose_ids, int):
        purpose_ids = [purpose_ids]
    
    actions = action_manager.get_actions_list(session.user_id, purpose_ids, to, _from)
    return actions


# 行動記録の作成
@app.post("/api/actions", status_code=status.HTTP_201_CREATED)
def create_actions(action: Action, session: SessionState = Depends(check_current_active_user)):
    action.action_id = None
    action.user_id = session.user_id

    try:
        action = action_manager.new_action(action, session.user_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )
    return action


# 行動記録の取得
@app.get("/api/actions/{id}", status_code=200)
def fetch_actions(id: int, session: SessionState = Depends(check_current_active_user)):
    action = action_manager.get_action(id, session.user_id)
    if action is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="この行動IDは存在しません"
        )
    return action


# 行動記録の修正
@app.put("/api/actions/{id}", status_code=200)
def modify_actions(id: int, action: Action, session: SessionState = Depends(check_current_active_user)):
    action = action_manager.change_action(id, session.user_id, action)
    return action


# 行動記録の削除
@app.delete("/api/actions/{id}", status_code=200)
def delete_actions(id: int, session: SessionState = Depends(check_current_active_user)):
    action_manager.delete(id, session.user_id)


# 振り返りAPI
@app.get("/api/reviews/need_weekly_reviews")
def get_need_weekly_reviews(session: SessionState = Depends(check_current_active_user)):
    need_weekly_reviews = review_manager.get_need_weekly_reviews(current_user=session.user_id)
    return need_weekly_reviews


@app.post("/api/reviews", status_code=status.HTTP_201_CREATED)
def create_review(review: Review, session: SessionState = Depends(check_current_active_user)):
    if review.user_id != session.user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )

    review.reviewed_at = datetime.datetime.now(datetime.timezone.utc)
    return review_manager.new_review(review, session.user_id)


@app.get("/api/reviews/{id}")
def get_review(id, session: SessionState = Depends(check_current_active_user)):
    r = review_manager.get_review(id, session.user_id)
    if r is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return r

