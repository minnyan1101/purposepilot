import json
from purpose_pilot.main import app, login
from scripts.init_test_db import main
from fastapi.testclient import TestClient
from httpx import Cookies

# main()

client = TestClient(app)
login_cookie = Cookies()


def test_login_set_cookie():
    res = client.post("/api/auth/login", json={"user_id": "test_1", "password": "masterpassword"})
    assert res.status_code == 200
    assert res.cookies.get("ssid") is not None
    global login_cookie
    login_cookie.set("ssid", res.cookies["ssid"])


def test_logout_session_disabled():
    res = client.post("/api/auth/login", json={"user_id": "test_1", "password": "masterpassword"})
    c = res.cookies
    client.post("/api/auth/logout", cookies=c, json={})
    res = client.get("/api/users/me", cookies=c)
    assert res.status_code == 401


def test_register_new_user():
    res = client.post("/api/users", json={"user_id": "test_new_user", "password": "passtest", "password_confirm": "passtest"})
    assert res.status_code == 201


def test_register_exists_user():
    res = client.post("/api/users", json={"user_id": "test_1", "password": "passtest", "password_confirm": "passtest"})
    assert res.status_code == 409


def test_get_user_profile_succuess():
    res = client.get("/api/users/me", cookies=login_cookie)
    assert res.status_code == 200
    assert res.json() == {
        "user_id": "test_1",
        "created_at": "2024-01-14T16:46:25.498268Z",
        "updated_at": "2025-01-14T16:46:25.498268Z",
        "avater_image_url": ""
    }


def test_get_user_profile_session_failed():
    res = client.get("/api/users/me")
    assert res.status_code == 401

# Todo: ユーザープロファイルの変更


# 目標
def test_get_purpose_list():
    res = client.get("/api/purposes", cookies=login_cookie)
    assert res.status_code == 200
    print(res.json())
    assert len(res.json()) == 2


def test_get_purpose_list_completed_filter():
    res = client.get("/api/purposes?status=completed", cookies=login_cookie)
    assert res.status_code == 200
    assert len(res.json()) == 1


def test_get_purpose_list_uncompleted_filter():
    res = client.get("/api/purposes?status=uncompleted", cookies=login_cookie)
    assert res.status_code == 200
    assert len(res.json()) == 1


def test_create_purpose():
    res = client.post("/api/purposes", json={
        "title": "test3",
        "description": "test3の説明",
        "due_at": "2024-01-14T16:46:25.498268+00:00",
        "status": "completed",
        "completed_at": "2024-01-14T16:46:25.498268+00:00",
    }, cookies=login_cookie)
    assert res.status_code == 201


def test_get_purpose():
    res = client.get("/api/purposes/1", cookies=login_cookie)
    assert res.status_code == 200


def test_change_purpose():
    base = client.get("/api/purposes/1", cookies=login_cookie).json()
    base["title"] = "modifyed title"

    print(base)

    res = client.put("/api/purposes/1", cookies=login_cookie, json=base)
    assert res.status_code == 200
    assert res.json()["title"] == "modifyed title"


def test_detele_purpose():
    res = client.post("/api/purposes", json={
        "title": "test_delete",
        "description": "test_deleteの説明",
        "due_at": "2024-01-14T16:46:25.498268+00:00",
        "status": "completed",
        "completed_at": "2024-01-14T16:46:25.498268+00:00",
    }, cookies=login_cookie)

    client.delete(f"/api/purposes/{res.json()["purpose_id"]}", cookies=login_cookie)

    not_found = client.get(f"/api/purposes/{res.json()["purpose_id"]}", cookies=login_cookie)

    assert not_found.status_code == 404


def test_get_action_list():
    res = client.get("/api/actions", cookies=login_cookie)
    assert res.status_code == 200
    assert len(res.json()) == 3

def test_create_action():
    res = client.post("/api/actions", json={
        "user_id": "test_1",
        "purpose_id": 1,
        "action_detail": "てすとじ作成",
        "started_at": "2024-01-14T16:46:25.498268+00:00",
        "finished_at": "2024-01-14T17:46:25.498268+00:00",
    }, cookies=login_cookie)

    assert res.status_code == 201
