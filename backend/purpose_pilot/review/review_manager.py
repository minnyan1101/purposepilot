from .review_repository import ReviewRepository
from .model import Review

from datetime import datetime


class reviewManager:
    def __init__(self, repo: ReviewRepository) -> None:
        self.repo = repo

    def new_review(self, review: Review, current_user) -> Review:
        return self.repo.save(review)

    def get_review_list(self, purpose_ids: list[int], to, _from, current_user) -> list[Review]:
        if purpose_ids is None:
            purpose_ids = []
            
        if not purpose_ids:
            purpose_ids = self.repo.get_active_purpose_ids(current_user)
            
        if to is None:
            to = datetime.min
            
        if _from is None:
            _from = datetime.max
        
        return self.repo.findAll(current_user, purpose_ids, to, _from)

