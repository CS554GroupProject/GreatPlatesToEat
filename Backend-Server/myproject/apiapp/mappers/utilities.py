def is_proper_key(key):
    if key != "Query":
        return False
    return True

def is_data_string_empty(data):
    if data == "":
        return True
    return False