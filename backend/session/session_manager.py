
from secrets import token_bytes
from hashlib import sha512
from datetime import datetime, timedelta

from .session_model import SessionState
from .session_repository import SessionRepository

class SessionManager:
    # expire_delta_sec = 1209600 （二週間）
    def __init__(self, session_repository: SessionRepository, expire_delta: timedelta = timedelta(days=14)) -> None:
        self.repo = session_repository
        self.expire_delta = expire_delta
        
    def new_session_id(self) -> bool:
        while True:
            ssid = generate_session_id()
            if self.repo.find(ssid):
                continue
            
            return ssid

    def create(self, user_id) -> SessionState:
        ssid = self.new_session_id()
        issued_at = datetime.now()
        expired_at = issued_at + self.expire_delta
        session_state = SessionState(ssid, user_id, issued_at, expired_at)
        
        self.repo.create(session_state)
        return session_state
    
    def find(self, session_id) -> SessionState:
        return self.repo.find(session_id)
    
    def revoke(self, session_id):
        self.repo.delete(session_id)


def generate_session_id(self) -> str:
    m = sha512()
    m.update(token_bytes(128))
    return m.hexdigest()