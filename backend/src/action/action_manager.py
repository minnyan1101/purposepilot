
from .model import Action
from .action_repository import ActionRepository
from datetime import datetime


class PurposeManager:
    def __init__(self, repo: ActionRepository) -> None:
        self.repo = repo

    # action_idを指定していないActionを入力して新しく登録されたデータを返却する。
    def new_action(self, action: Action) -> Action:
        pass

    # 登録されているデータを更新する
    def change_action(self, actoin: Action) -> Action:
        pass

    def get_action(self, aciont_id: str) -> Action:
        pass

    def get_purpose_list(self, user_id: str, to: datetime, _from: datetime) -> list[Action]:
        pass
