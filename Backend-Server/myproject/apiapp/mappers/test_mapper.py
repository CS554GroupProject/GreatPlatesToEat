from mapper import DataMapper

def test_rephrase_request():
    chat_gpt_request_object = {
        "role": "user",
        "content": "test",
    }
    assert (
        DataMapper.rephrase_request(self=DataMapper, user_text="test")
        == chat_gpt_request_object
    )


# https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
# https://www.youtube.com/watch?v=_uQrJ0TkZlc
# https://www.geeksforgeeks.org/python-functions/
# https://docs.python.org/3/library/stdtypes.html#dict
# https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-final-newline.html
# https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-module-docstring.html