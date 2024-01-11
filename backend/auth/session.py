from sqlite3 import Connection
from secrets import token_bytes
from hashlib import sha512
from datetime import datetime, timedelta

from .model import SessionState

class SessionRepository:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn
        
    def find_session(session_id) -> SessionState | None:
        pass
    
    def save(SessionState) -> None:
        pass
    
    def delete(session_id) -> None:
        pass

class SessionStore:
    # expire_delta_sec = 1209600 （二週間）
    def __init__(self, session_repository: SessionRepository, expire_delta: timedelta = timedelta(days=14)) -> None:
        self.repo = session_repository
        self.expire_delta = expire_delta
    def create_session(self, user_id):
        while True:
            ssid = generate_session_id()
            if self.repo.find_session(ssid):
                continue
            
            issued_at = datetime.now()
            expired_at = issued_at + self.expire_delta
            session_state = SessionState(ssid, user_id, issued_at, expired_at)
            
    def revoke(self, user_id, session_id):
        pass


def generate_session_id(self) -> str:
    m = sha512()
    m.update(token_bytes(128))
    return m.hexdigest()