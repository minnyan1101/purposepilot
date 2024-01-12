import dataclasses

from datetime import datetime


@dataclasses.dataclass
class SessionState:
    session_id: str
    user_id: str
    issued_at: datetime
    expired_at: datetime

    def asdict(self) -> dict:
        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "issued_at": self.issued_at.isoformat(),
            "expired_at": self.issued_at.isoformat(),
        }
    
    def is_alive(self, now_datetime: datetime) -> bool:
        if self.expired_at < now_datetime:
            return True
        
        return False
