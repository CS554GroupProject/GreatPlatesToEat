import requests
import json

# Define the API endpoint
url = "https://api.openai.com/v1/engines/davinci/completions"

# Set up the headers, including your API key
headers = {
    "Authorization": f"Bearer YOUR_OPENAI_API_KEY",  # replace YOUR_OPENAI_API_KEY with your actual key
    "Content-Type": "application/json",
}

# Define the payload for the request
data = {
    "prompt": "Translate the following English text to French: 'Hello, how are you?'",
    "max_tokens": 150
}

# Make the request to the API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    response_data = response.json()
    generated_text = response_data["choices"][0]["text"].strip()
    print(f"Generated Text: {generated_text}")
else:
    print(f"Error {response.status_code}: {response.text}")

