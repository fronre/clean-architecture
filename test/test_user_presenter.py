from src.entities.user import User
from src.interface_adapters.presenters.user_presenter import UserPresenter

def test_user_presenter_returns_dict_using_viewmodel():
    u = User("John", "Doe")
    p = UserPresenter()
    out = p.present(u)
    assert out == {"first_name": "John", "last_name": "Doe"}
