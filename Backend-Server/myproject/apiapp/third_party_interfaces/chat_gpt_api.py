"""This file includes all interactions with the chat gpt api"""
import os
from openai import OpenAI
from .secret_key import API_KEY

client = OpenAI(api_key=API_KEY)


class ChatInteractions:
    """
    Class for interacting with the openai API - scalzone
    """

    def get_completion(self, prompt: str):
        """Function to send a prompt to Chat-GPT - scalzone"""
        model = "gpt-3.5-turbo"
        message = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model, messages=message, temperature=0
        )
        return response.choices[0].message.content
        # return prompt


# test_object = ChatInteractions()
# test_response = test_object.get_completion("What is a good recipe for pizza with white sauce?")
# print(test_response)
