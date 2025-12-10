from unittest.mock import Mock


def test_controller_with_mock_presenter():
    dto = {"first_name": "A", "last_name": "B"}
    mock_usecase = Mock()
    mock_presenter = Mock()
    mock_presenter.present.return_value = {"first_name": "A", "last_name": "B"}

    result = create_user_controller(dto, mock_usecase, mock_presenter)

    mock_usecase.execute.assert_called_once()
    mock_presenter.present.assert_called_once()
    assert result == {"first_name": "A", "last_name": "B"}

def test_controller_calls_usecase_and_returns_presented():
    # Arrange
    dto = {"first_name": "A", "last_name": "B"}
    mock_usecase = Mock()
    mock_presenter = Mock()
    mock_presenter.present.return_value = {"first_name": "A", "last_name": "B"}

    # Act
    result = create_user_controller(dto, mock_usecase, mock_presenter)

    # Assert
    mock_usecase.execute.assert_called_once()
    mock_presenter.present.assert_called_once()
    assert result == {"first_name": "A", "last_name": "B"}