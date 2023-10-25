"""This file includes all interactions with the chat gpt api"""
import os
import openai
import pandas as pd
import time
from secret_key import API_KEY

openai.api_key = API_KEY

class ChatInteractions:
    """
    Class for interacting with the openai API
    """
    def get_completion(self, prompt: str):
        """Function to send a prompt to Chat-GPT"""
        model = "gpt-3.5-turbo"
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]
