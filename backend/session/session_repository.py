import textwrap
from datetime import datetime
from sqlite3 import Connection, IntegrityError

from .session_model import SessionState

def convert_session_state(session_id, user_id, issued_at, expired_at):
    return SessionState(
        session_id,
        user_id,
        datetime.fromisoformat(issued_at),
        datetime.fromisoformat(expired_at)
  )
  

class SessionRepository:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn
        
    def find(self, session_id: str) -> SessionState | None:
        with self.conn.cursor() as cur:
            result = cur.execute(
                textwrap.dedent("""
                SELECT session_id, user_id, issued_at, expired_at FROM Session
                    WHERE session_id = ?                                      
                """),
                session_id
            )
            res = result.fetchone()
            if res:
                return None
          
            return convert_session_state(res)
    
    def create(self, session_state: SessionState) -> bool:
        with self.conn.cursor() as cur:
            try:
                cur.execute(
                    textwrap.dedent("""
                        INSERT INTO Session (session_id, user_id, issued_at, expired_at) VALUES (:session_id, :user_id, :issued_at, :expired_at)               
                    """),
                    session_state.asdict()
                )
            except IntegrityError:
                self.conn.rollback()
                raise ValueError("セッションステートのsession_idが既に存在します")
            
            else:
                self.conn.commit()
          
    def update(self, session_state: SessionState) -> None:
        with self.conn.cursor() as cur:
            cur.execute(
                textwrap.dedent("""
                    UPDATE (Session) SET user_id=:user_id, issued_at=:issued_at, expired_at=:expired_at
                        WHERE session_id=:session_id
                """),
                session_state.asdict()
            )
    
    def delete(self, session_id: str) -> None:
        with self.conn.cursor() as cur:
            cur.execute(
                textwrap.dedent("""
                    DELETE FROM Session WHERE session_id = ?
                """),
                session_id
            )
