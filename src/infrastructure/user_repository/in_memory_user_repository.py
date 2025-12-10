from src.use_cases.saving_user.user_repository_interface import UserRepositoryInterface
from src.entities.user import User
from typing import List

class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.storage: List[User] = []

    def save(self, user: User) -> None:
        # store the same User object
        self.storage.append(user)
