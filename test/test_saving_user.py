from unittest.mock import Mock
import pytest

from src.Use_Cases.Saving_User.SavingUseCase import SavingUseCase
from src.entities.user import User
from src.Use_Cases.Saving_User.user_repository_interface import UserRepositoryInterface

@pytest.mark.parametrize(
    "user",
    [
        User("John", "Doe"),
        User("Alice", "Smith"),
        User("Bob", "Marley"),
        User("Charlie", "Brown"),
    ]
)
def test_saving_user_is_calling_delegated_repository(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

def test_saving_user_is_not_saving_when_non_authorized(user):

    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_user_repository.save = Mock()

    dummy_notification_service = Mock()
    stub_authorization_service = Mock()
    stub_authorization_service.is_authorized = Mock(return_value=False)

    saving_use_case = SavingUseCase(
        spy_user_repository,
        dummy_notification_service,
        stub_authorization_service
    )

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()
