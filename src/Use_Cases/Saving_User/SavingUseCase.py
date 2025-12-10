from src.entities.user import User
from src.Use_Cases.Saving_User.user_repository_interface import UserRepositoryInterface
from typing import Optional, Protocol



class SavingUseCase:
    def __init__(self, user_repository, notification_service=None, authorization_service=None):
        self.user_repository = user_repository
        self.notification_service = notification_service
        self.authorization_service = authorization_service


def execute(self, user):
    if self.authorization_service and not self.authorization_service.is_authorized(user):
        return

    self.user_repository.save(user)

    if self.notification_service:
        self.notification_service.notify(user)

