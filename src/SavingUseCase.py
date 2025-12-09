from test.test_saving_user import UserRepositoryInterface, User


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository: UserRepositoryInterface = user_repository


    def execute(self, user: User) -> None:
        self.user_repository.save()
