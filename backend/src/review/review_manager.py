from .review_repository import ReviewRepository
from .model import Review


class reviewManager:
    def __init__(self, repo: ReviewRepository) -> None:
        self.repo = repo

    def new_review(self, review: Review) -> Review:
        return self.repo.save(review)

    def get(self, review_id: str, review: Review) -> None:
        pass

    def put(self, review_id: str, review: Review) -> None:
        pass
