from flask import Flask, request, jsonify
from mapper import DataMapper

def is_proper_key(key: str):
    if key != "Query":
        return False
    return True

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

    mapped_data = DataMapper.rephrase_request(self=DataMapper, user_text=user_text)

    return jsonify(mapped_data), 200

if __name__ == "__main__":
    app.run(debug=True)

# https://www.youtube.com/watch?v=zsYIw6RXjfM
# https://www.w3schools.com/python/python_ref_dictionary.asp
# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
# https://tedboy.github.io/flask/generated/generated/flask.Request.get_json.html
# https://www.w3schools.com/python/ref_dictionary_keys.asp