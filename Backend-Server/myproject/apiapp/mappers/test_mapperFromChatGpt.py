from .mapperFromChatGPT import DataMapperFromChatGPT

def test_is_correct_response_structure_true():
    data = {"choices": [{"message": {"content": "Hello World"}}]}

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is True

def test_is_correct_response_structure_noObjectResponse():
    data = ""

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is False

def test_is_correct_response_structure_no_empty_response_object():
    data = {}

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is False

def test_is_correct_response_structure_no_choices():
    data = {"choices": []}

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is False

def test_is_correct_response_structure_no_message():
    data = {"choices": [{}]}

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is False

def test_is_correct_response_structure_no_object_message():
    data = {"choices": [{"message"}]}

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is False

def test_is_correct_response_structure_no_content():
    data = {"choices": [{"message": {}}]}

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is False

def test_is_correct_response_structure_content_not_string():
    data = {"choices": [{"message": {"content"}}]}

    result = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=data)

    assert result is False