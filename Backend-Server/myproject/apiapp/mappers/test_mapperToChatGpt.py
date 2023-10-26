from .mapperToChatGPT import DataMapperToChatGPT

def test_rephrase_request():
    message_array = [{
        "role": "user",
        "content": "test",
    }]
    assert (
        DataMapperToChatGPT.rephrase_request(self=DataMapperToChatGPT, user_text="test")
        == message_array
    )


# https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
# https://www.youtube.com/watch?v=_uQrJ0TkZlc
# https://www.geeksforgeeks.org/python-functions/
# https://docs.python.org/3/library/stdtypes.html#dict
# https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-final-newline.html
# https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-module-docstring.html