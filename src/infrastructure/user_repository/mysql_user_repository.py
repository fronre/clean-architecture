from src.use_cases.saving_user.user_repository_interface import UserRepositoryInterface
from src.entities.user import User

class MySQLUserRepository(UserRepositoryInterface):
    def save(self, user: User) -> None:
        # placeholder: in real app this would persist
        print(f"[MySQLRepo] saved {user.first_name} {user.last_name}")
