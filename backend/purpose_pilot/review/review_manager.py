from purpose_pilot.purpose.purpose_repository import PurposeRepository
from .review_repository import ReviewRepository
from .model import Review

from datetime import datetime, timedelta, timezone


class ReviewManager:
    def __init__(
        self, review_repo: ReviewRepository, purpose_repo: PurposeRepository
    ) -> None:
        self.review_repo = review_repo
        self.purpose_repo = purpose_repo

    def new_review(self, review: Review, current_user) -> Review:
        return self.review_repo.save(review)

    def get_need_weekly_reviews(self, current_user) -> list[int]:
        uncomleted_purposes = self.purpose_repo.findAll(
            user_id=current_user, show_completed=False, show_uncompleted=True
        )
        need_review_purposes = []

        now = datetime.now(timezone(timedelta(hours=9)))
        base = datetime(now.year, now.month, now.day, tzinfo=now.tzinfo)
        to = base - timedelta(days=now.weekday())
        _from = base + timedelta(days=7 - now.weekday())
        

        for purpose in uncomleted_purposes:
            result = self.review_repo.findAll(
                user_id=current_user,
                purpose_ids=[
                    purpose.purpose_id,
                ],
                to=to,
                _from=_from,
            )
            
            if not result:
                need_review_purposes.append(purpose.purpose_id)

        return need_review_purposes
