
from enum import StrEnum
from .model import Purpose
from .purpose_repository import PurposeRepository


class PurposeFilter(StrEnum):
    COMPLETED = "completed"
    UNCOMPLETED = "uncompleted"
    ALL = "all"


class PurposeManager:
    def __init__(self, repo: PurposeRepository) -> None:
        self.repo = repo

    # purpose_idを指定していないPurposeを入力して新しく登録されたデータを返却する。
    def new_purpose(self, purpose: Purpose) -> Purpose:
        return self.repo.save(purpose)

    # 登録されているデータを更新する
    def change_purpose(self, purpose: Purpose) -> Purpose:
        self.repo.save(purpose)

    # 目標を取得
    def get_purpose(self, purpose_id, user_id: str) -> Purpose:
        res = self.repo.find(purpose_id, user_id)
        return res

    # 目標の一覧を取得
    def get_purpose_list(self, user_id, status: PurposeFilter) -> list[Purpose]:
        show_completed, show_uncompleted = True, True
        if status == PurposeFilter.ALL:
            show_completed, show_uncompleted = True, True
        elif status == PurposeFilter.COMPLETED:
            show_completed, show_uncompleted = True, False
        elif status == PurposeFilter.UNCOMPLETED:
            show_completed, show_uncompleted = False, True
        else:
            pass

        res = self.repo.findAll(user_id, show_completed, show_uncompleted)
        return res
