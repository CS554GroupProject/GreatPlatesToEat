from api import is_proper_key

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
