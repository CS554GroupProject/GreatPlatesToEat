from .ingredients import request_response_as_list_of_ingredients

def test_append_sentence_to_return_list_empty_prompt():
    sentence_to_append_expected = "Present this as a list."

    prompt = ""

    result = request_response_as_list_of_ingredients(prompt=prompt)

    assert result == prompt + " " + sentence_to_append_expected

def test_append_sentence_to_return_list_prompt():
    sentence_to_append_expected = "Present this as a list."

    prompt = "Can I get the ingredients for apple pie?"

    result = request_response_as_list_of_ingredients(prompt=prompt)

    assert result == prompt + " " + sentence_to_append_expected

def test_append_sentence_to_return_list_prompt_with_1_character():
    sentence_to_append_expected = "Present this as a list."

    prompt = "C"

    result = request_response_as_list_of_ingredients(prompt=prompt)

    assert result == prompt + " " + sentence_to_append_expected