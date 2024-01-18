import re
import secrets

from hashlib import sha512


def validate_user_id(user_id):
    if re.match(r"[a-zA-Z0-9_]{1,16}", user_id) is None:
        raise ValueError("user_idに許可されていない文字列が利用されています")


def validate_password(password):
    if len(password) < 8:
        raise ValueError("パスワードを8文字以上です")

    if 128 < len(password):
        raise ValueError("パスワードを128文字以内です")


def parse_salt(hash: str):
    salt, _hash = hash.split(";", 1)
    return salt, _hash


def gen_salt():
    return secrets.token_urlsafe(32)


def make_hash(salt, password):
    m = sha512()
    salted_password = salt + password
    m.update(salted_password.encode())

    salted_hash = m.hexdigest()
    return f"{salt};{salted_hash}"
