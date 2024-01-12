from datetime import datetime

from .account_repository import AccountRepository
from .register_user_model import RegisterUser
from .login_user_model import LoginUser
from .user_model import User
from .utils import make_hash


class AccountManager:
    def __init__(self, repo: AccountRepository) -> None:
        self.repo = repo
        
    def exists(self, reg_user: RegisterUser):
        if self.repo.find(reg_user):
            return True
        
        return False
    
    def register(self, reg_user: RegisterUser):
        now = datetime.now()
        user = User(
            reg_user.user_id,
            make_hash(reg_user.password),
            now,
            now
        )
        
        self.repo.save(user)
    
    def can_login(self, login_user: LoginUser):
        pass
    