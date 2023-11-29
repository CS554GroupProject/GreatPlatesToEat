"""
This is the test file for chat_gpt_api.
"""
from unittest.mock import patch, MagicMock
from .chat_gpt_api import ChatInteractions


@patch("apiapp.third_party_interfaces.chat_gpt_api.openai")
def test_api_functionality_get_completion(mock: MagicMock):
    """Test function for gpt responses"""
    # Arrange
    chat_gpt_response = "Success"
    response_mock = MagicMock()
    message_mock = MagicMock()
    message_mock.message = {"content": chat_gpt_response}
    response_mock.choices = [message_mock]
    mock.ChatCompletion.create.return_value = response_mock
    ask = "return the word 'Success'"

    # Act
    test_interaction = ChatInteractions()
    test_response = test_interaction.get_completion(ask)

    # Assert
    mock.ChatCompletion.create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": ask}],
        temperature=0,
    )
    assert test_response == chat_gpt_response
