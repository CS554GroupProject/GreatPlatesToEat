class DataMapperToChatGPT:
    def __init__(self) -> None:
        pass

    def rephrase_request(self, user_text: str) -> dict:
        message_array = []
        chat_gpt_request_object = {"role": "user", "content": user_text}
        message_array.append(chat_gpt_request_object)
        return message_array
