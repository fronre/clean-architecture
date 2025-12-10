from src.entities.user import User

def create_user_controller(dto, use_case, presenter):
    user = User(dto["first_name"], dto["last_name"])
    use_case.execute(user)
    return presenter.present(user)
