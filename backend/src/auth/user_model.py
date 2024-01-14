import dataclasses
from datetime import datetime

from .utils import make_hash


@dataclasses.dataclass
class User:
    user_id: str
    hash: str
    created_at: datetime
    updated_at: datetime
    avater_image_url: str = ""

    def asdict(self):
        return {
            "user_id": self.user_id,
            "hash": self.hash,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "avater_image_url": self.avater_image_url
        }

    def check_password(self, password):
        salt = self.get_salt()
        validate_hash = make_hash(salt, password)
        return validate_hash == self.hash

    def get_salt(self) -> str:
        salt, _ = self.hash.split(';', 1)
        return salt


def convert_user(user_id, hash, created_at, updated_at, avater_image_url):
    created_at = datetime.fromisoformat(created_at)
    updated_at = datetime.fromisoformat(updated_at)

    return User(user_id, hash, created_at, updated_at, avater_image_url)
