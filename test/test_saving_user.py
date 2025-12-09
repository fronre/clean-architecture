from unittest.mock import Mock

from src.SavingUseCase import SavingUseCase
from src.user import User
from src.user_repository_interface import UserRepositoryInterface


def test_saving_user_is_calling_delegated_repository():
     #Arrange
    user: User = User(first_name='Islam', last_name='hala')
    spy_user_repository = Mock(spec=UserRepositoryInterface)

    saving_use_case: SavingUseCase = SavingUseCase(user_repository=spy_user_repository)
    #Act
    saving_use_case.execute(user)
      #Assert
    spy_user_repository.save.assert_called_once()

def test_saving_user_save_the_user_in_the_repository():
    # Arrange

    user: User = User('Islam', 'hala')
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_user_repository.save = Mock()
    saving_use_case:SavingUseCase= SavingUseCase(user_repository=spy_user_repository)

    # Act

    saving_use_case.execute(user)


    # Assert
    spy_user_repository.save.assert_called_once_with(user)