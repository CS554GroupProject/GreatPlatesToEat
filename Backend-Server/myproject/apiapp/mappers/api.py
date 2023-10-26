from flask import Flask, request, jsonify
from .mapperToChatGPT import DataMapperToChatGPT
from .mapperFromChatGPT import DataMapperFromChatGPT
from .utilities import is_proper_key, is_data_string_empty

app = Flask(__name__)

@app.route("/postToChatGpt", methods=["POST"])
def query_data():
    data = request.get_json()

    if len(data) != 1:
        return jsonify("JSON object must only have 1 key-value pair"), 503

    key = list(data.keys())[0]

    if is_proper_key(key=key) is False:
        return jsonify("Improper key name for key-value pair"), 503

    user_text = data[key]

    response = DataMapperToChatGPT.send_message_to_gpt(DataMapperFromChatGPT, request=user_text)

    if is_data_string_empty(response):
        return jsonify("No response or invalid data", 503)

    return jsonify(response), 200

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