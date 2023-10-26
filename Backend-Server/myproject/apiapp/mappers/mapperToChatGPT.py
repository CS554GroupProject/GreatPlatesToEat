from ..third_party_interfaces import chat_gpt_api

class DataMapperToChatGPT:
    def __init__(self) -> None:
        pass

    def rephrase_request(self, user_text):
        message_array = []
        chat_gpt_request_object = {"role": "user", "content": user_text}
        message_array.append(chat_gpt_request_object)
        return message_array

    def send_message_to_gpt(self, request):
        return chat_gpt_api.get_completion(prompt=request)