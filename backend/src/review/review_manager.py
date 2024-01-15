from .review_repository import ReviewRepository
from .model import Review


class reviewManager:
    def __init__(self, repo: ReviewRepository) -> None:
        self.repo = repo

    def register(self) -> Review:
        pass

    def get(self, review_id: str) -> None:
        pass

    def put(self, review_id: str) -> None:
        pass
