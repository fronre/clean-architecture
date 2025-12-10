from src.entities.user import User
from dataclasses import asdict

class UserPresenter:
    def present(self, user: User) -> dict:
        return {"first_name": user.first_name, "last_name": user.last_name}
