from src.infrastructure.user_repository.in_memory_user_repository import InMemoryUserRepository
from src.entities.user import User

def test_inmemory_repo_persists_user():
    repo = InMemoryUserRepository()
    u = User("Persist","Me")
    repo.save(u)
    assert repo.storage == [u]
