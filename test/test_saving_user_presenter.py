from src.interface_adapters.presentation import UserPresenter
from src.entities.user import User

def test_user_presenter_outputs_dict():
    presenter = UserPresenter()
    u = User("A", "B")
    out = presenter.present(u)
    assert out == {"first_name":"A","last_name":"B"}
