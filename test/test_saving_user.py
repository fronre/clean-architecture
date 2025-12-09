import abc
import dataclasses
from unittest.mock import Mock

@dataclasses.dataclass
class User:
    pass

class UserRepositoryInterface(metaclass=abc.ABCMeta):
    pass


def test_saving_user_is_calling_repository():



   user: User = User(first_name='Islam', last_name='hala')
   spy_user_repository: User_repositoryInterface = Mock(spec=UserRepositoryInterface)

   saving_use_case: SavingUseCase() = SavingUseCase(user_repository=spy_user_repository)
   saving_use_case.executed(user)

   spy_user_repository.save.assert_called_once()
