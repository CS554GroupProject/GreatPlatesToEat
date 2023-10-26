from utilities import is_proper_key, is_data_string_empty, get_response

def test_is_proper_key_valid():
    valid_key = "Query"
    assert (
        is_proper_key(key=valid_key)
        is True
    )

def test_is_proper_key_invalid():
    invalid_key = "query"
    assert (
        is_proper_key(key=invalid_key)
        is False
    )

def test_is_data_string_empty():
    data_string = ""
    assert (
        is_data_string_empty(data=data_string)
        is True
    )

def test_is_data_string_nonempty():
    data_string = "A"
    assert (
        is_data_string_empty(data=data_string)
        is False
    )

# get_response will get tested when actually getting data