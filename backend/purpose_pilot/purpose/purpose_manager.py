
from enum import StrEnum
from .model import Purpose
from .purpose_repository import PurposeRepository
from datetime import datetime, timezone


class PurposeFilter(StrEnum):
    COMPLETED = "completed"
    UNCOMPLETED = "uncompleted"
    ALL = "all"


class PurposeManager:
    def __init__(self, repo: PurposeRepository) -> None:
        self.repo = repo

    # purpose_idを指定していないPurposeを入力して新しく登録されたデータを返却する。
    def new_purpose(self, current_user, title, description, due_at, status, completed_at) -> Purpose:
        new = Purpose(
            user_id=current_user,
            title=title,
            description=description,
            created_at=datetime.now(timezone.utc),
            due_at=due_at,
            status=status,
            completed_at=completed_at
        )

        return self.repo.save(new)

    # 登録されているデータを更新する
    def change_purpose(self, purpose: Purpose, current_user) -> Purpose:
        update = self.get_purpose(purpose_id=purpose.purpose_id, current_user=current_user)
        if update is None:
            raise ValueError('変更対象のpurposeは存在していません')
        update.update(purpose)
        result = self.repo.save(update)
        return result

    def delete_purpose(self, purpose_id, current_user):
        self.repo.delete(purpose_id, current_user)

    # 目標を取得
    def get_purpose(self, purpose_id, current_user) -> Purpose | None:
        res = self.repo.find(purpose_id, current_user)
        return res

    # 目標の一覧を取得
    def get_purpose_list(self, current_user, status: PurposeFilter) -> list[Purpose]:
        show_completed, show_uncompleted = True, True
        if status == PurposeFilter.ALL:
            show_completed, show_uncompleted = True, True
        elif status == PurposeFilter.COMPLETED:
            show_completed, show_uncompleted = True, False
        elif status == PurposeFilter.UNCOMPLETED:
            show_completed, show_uncompleted = False, True
        else:
            pass

        res = self.repo.findAll(current_user, show_completed, show_uncompleted)
        return res
