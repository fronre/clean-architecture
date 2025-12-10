from dataclasses import dataclass, asdict
from src.entities.user import User

@dataclass
class UserViewModel:
    first_name: str
    last_name: str

    @staticmethod
    def from_user(user: User) -> "UserViewModel":
        return UserViewModel(first_name=user.first_name, last_name=user.last_name)

    def to_dict(self) -> dict:
        return asdict(self)
