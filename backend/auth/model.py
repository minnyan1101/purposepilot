import dataclasses
import datetime

@dataclasses.dataclass
class SessionState:
    session_id: str
    user_id: str
    issued_at: datetime.datetime
    expired_at: datetime.datetime
