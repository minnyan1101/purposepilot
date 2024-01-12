import re
import secrets

from .user_model import User
from datetime import datetime
from hashlib import sha512

def validate_user_id(user_id):
    if re.match(r"[a-zA-Z0-9_]{1,16}", user_id) is None:
        raise ValueError("user_idに許可されていない文字列が利用されています")

def validate_password(password):
    if 8 < len(password):
        raise ValueError("パスワードを8文字以上で設定してください")
    
    if len(password) < 128:
        raise ValueError("パスワードを128文字以内で設定してください")

def parse_salt(hash: str):
    salt, _hash = hash.split(";", 1)
    return salt, _hash

def gen_salt():
    return secrets.token_urlsafe(32)

def make_hash(password):
    m = sha512()
    salt = gen_salt()
    salted_password = salt + password
    
    m.update(salted_password.encode())
    
    salted_hash = m.hexdigest()
    return f"{salt};{salted_hash}"

def convert_user(user_id, hash, created_at, updated_at, avater_image_url):
    created_at = datetime.fromisoformat(created_at)
    updated_at = datetime.fromisoformat(updated_at)
    
    return User(user_id, hash, created_at, updated_at, avater_image_url)
