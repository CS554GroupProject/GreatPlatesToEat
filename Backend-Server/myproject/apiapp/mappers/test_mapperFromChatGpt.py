from mapperFromChatGPT import DataMapperFromChatGPT

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

def test_get_message_from_response_none():
    response_from_chat_gpt = ""

    message_expected = ""
    result = DataMapperFromChatGPT.get_message_from_response(self=DataMapperFromChatGPT, response=response_from_chat_gpt)

    assert result == message_expected

def test_get_message_from_response_valid():
    response_from_chat_gpt = {"choices": [{"message": {"content": "Hello World"}}]}

    message_expected = "Hello World"
    result = DataMapperFromChatGPT.get_message_from_response(self=DataMapperFromChatGPT, response=response_from_chat_gpt)

    assert result == message_expected