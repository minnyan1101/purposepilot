from .user_repository import UserRepository
from .model import User


class UserManager:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def get_profile(self, user_id: str) -> User:
        return self.repo.find(user_id)

    def change_profile(self, user, current_user) -> User:
        pass

    def delete(self, user_id: str) -> None:
        pass
