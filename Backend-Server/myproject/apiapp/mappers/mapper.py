class DataMapper:
    def __init__(self) -> None:
        pass

    def rephrase_request(self, user_text: str) -> dict:
        chat_gpt_request_object = {"role": "user", "content": user_text}
        return chat_gpt_request_object
