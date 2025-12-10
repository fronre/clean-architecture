import abc

from src.entities.user import User


class UserRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError
