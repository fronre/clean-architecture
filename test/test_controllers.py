
def test_controller_calls_usecase_and_returns_presented():
    dto = {"first_name":"A","last_name":"B"}
    mock_usecase = Mock()
    result = create_user_controller(dto, mock_usecase)
    mock_usecase.execute.assert_called_once()
    assert result == {"first_name":"A","last_name":"B"}
