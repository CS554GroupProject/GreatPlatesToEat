class DataMapperFromChatGPT:
    def __init__(self) -> None:
        pass

    def is_correct_response_structure(self, response) -> bool:
        if isinstance(response, dict) is False:
            return False
        if response.get('choices') is None:
            return False
        if isinstance(response['choices'], list) is False:
            return False
        if len(response['choices']) == 0:
            return False
        if isinstance(response['choices'][0], dict) is False:
            return False
        if response['choices'][0].get('message') is None:
            return False
        if isinstance(response['choices'][0]['message'], dict) is False:
            return False
        if response['choices'][0]['message'].get("content") is None:
            return False
        if isinstance(response['choices'][0]['message']['content'], str) is False:
            return False
        
        return True

    def get_message_from_response(self, response) -> str:
        correct_structure_for_response = DataMapperFromChatGPT.is_correct_response_structure(self=DataMapperFromChatGPT, response=response)

        if correct_structure_for_response is False:
            return ""
        return response['choices'][0]['message']['content']
