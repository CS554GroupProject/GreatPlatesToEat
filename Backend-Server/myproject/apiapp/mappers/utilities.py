def is_proper_key(key):
    if key != "Query":
        return False
    return True

def get_response(mapped_data):
    # call to Nick's ChatGPT api
    return {"choices": [{"message": {"content": "Hello World"}}]}

def is_data_string_empty(data):
    if data == "":
        return True
    return False