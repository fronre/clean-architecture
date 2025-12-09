from unittest.mock import Mock

from src.SavingUseCase import SavingUseCase
from src.user import User
from src.user_repository_interface import UserRepositoryInterface


def test_saving_user_is_calling_delegated_repository():
    user: User = User(first_name='Islam', last_name='hala')
    spy_user_repository = Mock(spec=UserRepositoryInterface)

    saving_use_case: SavingUseCase = SavingUseCase(user_repository=spy_user_repository)
    saving_use_case.execute(user)

    spy_user_repository.save.assert_called_once()
