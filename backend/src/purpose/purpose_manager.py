
from .model import Purpose
from .purpose_repository import PurposeRepository, PurposeFilter


class PurposeManager:
    def __init__(self, repo: PurposeRepository) -> None:
        self.repo = repo

    # purpose_idを指定していないPurposeを入力して新しく登録されたデータを返却する。
    def new_purpose(self, purpose: Purpose) -> Purpose:
        pass

    # 登録されているデータを更新する
    def change_purpose(self, purpose: Purpose) -> Purpose:
        pass

    def get_purpose(self, purpose_id: str) -> Purpose:
        pass

    def get_purpose_list(self, user_id, status: PurposeFilter) -> list[Purpose]:
        pass

    