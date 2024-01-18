from datetime import datetime, timedelta
from secrets import token_bytes
from hashlib import sha512


from .session_repository import SessionRepository
from .session_model import SessionState

from .auth_repository import AuthRepository
from .login_user_model import LoginUser

from .register_user_model import RegisterUser
from .user_model import User
from .utils import gen_salt, make_hash


class AuthManager:
    def __init__(self, session_repo: SessionRepository, auth_repo: AuthRepository) -> None:
        self.session_repo = session_repo
        self.auth_repo = auth_repo

    def find(self, session_id: str) -> SessionState:
        return self.session_repo.find(session_id)

    def is_authenticated(self, session_id: str) -> bool:
        session = self.find(session_id)
        if not session:
            return False
        return session.is_alive(datetime.now())

    def login(self, login_user: LoginUser) -> SessionState:
        user_verification_data = self.auth_repo.find(login_user.user_id)
        if not (user_verification_data and user_verification_data.check_password(login_user.password)):
            raise ValueError("ユーザーIDかパスワードが正しくありません")

        session = self.__session_create(login_user.user_id)
        return session

    def logout(self, session_id: str):
        session = self.session_repo.find(session_id)
        if not session:
            raise ValueError("セッションが存在していません")

        if not session.is_alive(datetime.now()):
            raise ValueError("セッションが有効ではありません")

        self.session_repo.delete(session)

    def register(self, register_user: RegisterUser) -> bool:
        salt = gen_salt()
        hash = make_hash(salt, register_user.password)
        user = User(
            register_user.user_id,
            hash,
            datetime.now(),
            datetime.now(),
            ""
        )
        if self.auth_repo.find(register_user.user_id):
            return False

        self.auth_repo.save(user)
        return True

    def __session_create(self, user_id) -> SessionState:
        ssid = self.__new_session_id()
        issued_at = datetime.now()
        expired_at = issued_at + timedelta(14)
        session_state = SessionState(ssid, user_id, issued_at, expired_at)

        self.session_repo.create(session_state)
        return session_state

    def __new_session_id(self) -> bool:
        while True:
            ssid = generate_session_id()
            if self.session_repo.find(ssid):
                continue

            return ssid


def generate_session_id() -> str:
    m = sha512()
    m.update(token_bytes(128))
    return m.hexdigest()
