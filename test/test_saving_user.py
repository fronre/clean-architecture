from unittest.mock import Mock
import pytest

from src.Use_Cases.Saving_User.SavingUseCase import SavingUseCase
from src.entities.user import User
from src.Use_Cases.Saving_User.user_repository_interface import UserRepositoryInterface

@pytest.mark.parametrize(
    "user",
    [
        User("Islam", "hala"),
        User("Julian234", "Julian"),
        User("Julian44444", "Julian"),
        User("Julian444", "Julian6"),
        User("Julian333", "Julian7"),
        User("Julian33", "Julian9999"),
        User("Julian2", "Julian"),
        User("Julian3", "Julian"),
        User("Julian4", "Julian"),
        User("Julian5", "Julian"),



    ]
)
def test_saving_user_is_calling_delegated_repository(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)


def test_saving_user_save_the_user_in_the_repository():
    # Arrange
    user = User('Islam', 'hala')
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)
