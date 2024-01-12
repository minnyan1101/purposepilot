import sqlite3
import textwrap

from .utils import convert_user
from .user_model import User

class AccountRepository:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.conn = db_conn
        
    def find(self, user_id: str):
        with self.conn.cursor() as cur:
            result = cur.execute(textwrap.dedent("""
                    SELECT user_id, hash, created_at, updated_at, avater_image_url FROM User
                        WHERE user_id = ?                           
                """),
                user_id    
            )
            
            res = result.fetchone()
            if res is None:
                return None
            user = convert_user(*res)
            
            return user
    
    def save(self, user: User):
        if self.find(user.user_id):
            with self.conn.cursor() as cur:
                cur.execute(textwrap.dedent("""
                        UPDATE User SET user_id=:user_id, hash=:hash, created_at=:created_at, updated_at=:updated_at, avater_image_url=:avater_image_url 
                            WHERE user_id = :user_id
                    """),
                    User.asdict()
                )
                self.conn.commit()
        
        else:
            with self.conn.cursor() as cur:
                cur.execute(textwrap.dedent("""
                        INSERT INTO  User (user_id, hash, created_at, updated_at, avater_image_url) 
                            VALUES (:user_id, :hash, :created_at, :updated_at, :avater_image_url)
                    """),
                    User.asdict()
                )
                self.conn.commit()
                
            
            