
from secrets import token_bytes
from hashlib import sha512
from datetime import datetime, timedelta

from .model import SessionState
from .repositoy import SessionRepository

class SessionManager:
    # expire_delta_sec = 1209600 （二週間）
    def __init__(self, session_repository: SessionRepository, expire_delta: timedelta = timedelta(days=14)) -> None:
        self.repo = session_repository
        self.expire_delta = expire_delta

    def create_session(self, user_id):
        while True:
            ssid = generate_session_id()
            if self.repo.find(ssid):
                continue
            
            issued_at = datetime.now()
            expired_at = issued_at + self.expire_delta
            session_state = SessionState(ssid, user_id, issued_at, expired_at)
    
    def is_alive_session(self, user_id, session_id) -> bool:
        session_state = self.repo.find(session_id)
        if not session_state:
            return False
        
        if user_id != session_state.user_id:
            return False
        
        if session_state.expired_at < datetime.now() < session_state.issued_at:
            return False
        
        return True
    
    def revoke(self, session_id):
        self.repo.delete(session_id)


def generate_session_id(self) -> str:
    m = sha512()
    m.update(token_bytes(128))
    return m.hexdigest()