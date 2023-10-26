from flask import Flask, request, jsonify
from mapperToChatGPT import DataMapperToChatGPT
from mapperFromChatGPT import DataMapperFromChatGPT
from utilities import is_proper_key, get_response, is_data_string_empty;

app = Flask(__name__)

@app.route("/post", methods=["POST"])
def query_data():
    data = request.get_json()

    if len(data) != 1:
        return jsonify("JSON object must only have 1 key-value pair"), 503

    key = list(data.keys())[0]

    if is_proper_key(key=key) is False:
        return jsonify("Improper key name for key-value pair"), 503

    user_text = data[key]

    mapped_data = DataMapperToChatGPT.rephrase_request(self=DataMapperToChatGPT, user_text=user_text)
    response = get_response(mapped_data=mapped_data)

    mapped_response_data = DataMapperFromChatGPT.get_message_from_response(self=DataMapperFromChatGPT, response=response)

    if is_data_string_empty(mapped_response_data):
        return jsonify("No response or invalid data", 503)

    return jsonify(mapped_response_data), 200

if __name__ == "__main__":
    app.run(debug=True)

# https://www.youtube.com/watch?v=zsYIw6RXjfM
# https://www.w3schools.com/python/python_ref_dictionary.asp
# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
# https://tedboy.github.io/flask/generated/generated/flask.Request.get_json.html
# https://www.w3schools.com/python/ref_dictionary_keys.asp
# https://www.geeksforgeeks.org/python-data-types/
# https://platform.openai.com/docs/api-reference/introduction
# VS code