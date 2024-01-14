from .review_repository import ReviewRepository
from .model import Review


class UserManager:
    def __init__(self, repo: ReviewRepository) -> None:
        pass

    def register(self) -> Review:
        pass

    def delete(self, user_id: str) -> None:
        pass

