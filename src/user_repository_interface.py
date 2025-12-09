import abc

from src.user import User


class UserRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, user: User) -> None:
        pass
