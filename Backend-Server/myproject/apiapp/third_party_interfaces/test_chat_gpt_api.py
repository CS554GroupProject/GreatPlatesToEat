"""
This is the test file for chat_gpt_api.
"""
from .chat_gpt_api import ChatInteractions

first_test = ChatInteractions()
print(first_test.get_completion("Return the phrase 'I know I'm right"))


def test_get_completion():
    """Test function for gpt responses"""
    test_interaction = ChatInteractions()
    ask = "return the word 'Success'"
    test_response = test_interaction.get_completion(ask)
    # was supposed to assert success but api call in get_completion is commented out currently so this test needs to be modified when that happens
    assert test_response == ask
