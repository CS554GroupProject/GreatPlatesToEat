"""This file includes all interactions with the chat gpt api"""
import os
import openai
from .secret_key import API_KEY

openai.api_key = API_KEY


class ChatInteractions:
    """
    Class for interacting with the openai API - scalzone
    """

    def get_completion(self, prompt: str):
        """Function to send a prompt to Chat-GPT - scalzone"""
        model = "gpt-3.5-turbo"
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]
        # return prompt
