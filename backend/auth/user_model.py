import dataclasses
from datetime import datetime

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