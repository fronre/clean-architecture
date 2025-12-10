from fastapi import FastAPI, Depends
from pydantic import BaseModel
from src.infrastructure.user_repository.in_memory_user_repository import InMemoryUserRepository
from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.presentation.user_presenter import UserPresenter

app = FastAPI(title="User API (TDD-demo)")

class CreateUserDTO(BaseModel):
    first_name: str
    last_name: str

def get_usecase():
    repo = InMemoryUserRepository()
    presenter = UserPresenter()  # not used here but could be injected
    return SavingUseCase(user_repository=repo)

@app.post("/users")
def create_user(dto: CreateUserDTO, use_case: SavingUseCase = Depends(get_usecase)):
    from src.entities.user import User
    user = User(dto.first_name, dto.last_name)
    use_case.execute(user)
    return {"status": "created"}
