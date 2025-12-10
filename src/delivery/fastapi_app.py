# src/delivery/fastapi_app.py
from fastapi import FastAPI, Depends
import pydantic

from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.infrastructure.user_repository.in_memory_user_repository import InMemoryUserRepository

from src.interface_adapters.controllers.create_user_controller import create_user_controller
from src.interface_adapters.presenters.user_presenter import UserPresenter

app = FastAPI(title="User API (TDD-demo)")

class CreateUserDTO(BaseModel):
    first_name: str
    last_name: str

def get_usecase():
    repo = InMemoryUserRepository()
    return SavingUseCase(user_repository=repo)

@app.post("/users")
def create_user(dto: CreateUserDTO, use_case: SavingUseCase = Depends(get_usecase)):
    presenter = UserPresenter()
    return create_user_controller(dto.dict(), use_case, presenter)
