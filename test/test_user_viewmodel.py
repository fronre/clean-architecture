from src.entities.user import User
import src.interface_adapters.presenters.view_models

def test_userviewmodel_from_user_and_to_dict():
    u = User("A", "B")
    vm = UserViewModel.from_user(u)
    d = vm.to_dict()
    assert d == {"first_name": "A", "last_name": "B"}
