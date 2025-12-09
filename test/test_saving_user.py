import abc
import dataclasses
from unittest.mock import Mock


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str


class UserRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, user: User) -> None:
        pass


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        pass


def executed(self, user: User) -> None:
    pass


def test_saving_user_is_calling_repository():
    user: User = User(first_name='Islam', last_name='hala')
    spy_user_repository = Mock(spec=UserRepositoryInterface)

    saving_use_case: SavingUseCase() = SavingUseCase(user_repository=spy_user_repository)
    saving_use_case.execute(user)

    spy_user_repository.save.assert_called_once()
