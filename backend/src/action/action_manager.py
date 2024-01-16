
from .model import Action
from .action_repository import ActionRepository
from datetime import datetime


class ActionManager:
    def __init__(self, repo: ActionRepository) -> None:
        self.repo = repo

    # action_idを指定していないActionを入力して新しく登録されたデータを返却する。
    def new_action(self, action: Action) -> Action:
        if action.action_id is not None:
            raise ValueError("action_idが設定されています。")
        return self.repo.save(action)

    # 登録されているデータを更新する
    def change_action(self, action_id: int, user_id: str, action: Action):
        update = self.repo.find(action_id, user_id)
        if update is None:
            return
        update.update(action)
        return self.repo.save(update)

    def get_action(self, action_id: str, user_id: str) -> Action | None:
        res = self.repo.find(action_id, user_id)
        return res

    def get_actions_list(self, user_id: str, purpose_ids: 'list[str]' or None,
                         to: datetime or None, _from: datetime or None) -> 'list[Action]':
        if not purpose_ids:
            purpose_ids = self.repo.user_purpose_ids(user_id)

        if not to:
            to = datetime.min

        if not _from:
            _from = datetime.max
        print(user_id, purpose_ids, to, _from)
        return self.repo.findAll(user_id, purpose_ids, to, _from)

    def delete(self, action_id, user_id):
        self.repo.delete(action_id, user_id)
