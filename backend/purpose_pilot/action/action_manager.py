from .model import Action
from .action_repository import ActionRepository
from datetime import datetime


class ActionManager:
    def __init__(self, repo: ActionRepository) -> None:
        self.repo = repo

    # action_idを指定していないActionを入力して新しく登録されたデータを返却する。
    def new_action(self, action: Action, current_user) -> Action:
        if action.action_id is not None:
            raise ValueError("action_idが設定されています。")

        if action.user_id != current_user:
            raise ValueError("user_idがとこなります")

        return self.repo.save(action)

    # 登録されているデータを更新する
    def change_action(self, action_id: int, current_user: str, action: Action):
        update = self.repo.find(action_id, current_user)
        if update is None:
            raise ValueError("データが存在しません")
        update.update(action)
        return self.repo.save(update)

    def get_action(self, action_id: int, current_user: str) -> Action | None:
        res = self.repo.find(action_id, current_user)
        return res

    def get_actions_list(self, user_id: str, purpose_ids: list[int] | None,
                         to: datetime | None, _from: datetime | None) -> list[Action]:
        if not purpose_ids:
            purpose_ids = self.repo.user_purpose_ids(user_id)

        if not to:
            to = datetime.min

        if not _from:
            _from = datetime.max

        return self.repo.findAll(user_id, purpose_ids, to, _from)

    def delete(self, action_id, current_user):
        self.repo.delete(action_id, current_user)
