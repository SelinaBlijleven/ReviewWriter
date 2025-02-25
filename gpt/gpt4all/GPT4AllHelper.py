"""
GPT4AllHelper.py

@author     Lina Blijleven
"""
from typing import Optional
from gpt.gpt4all.GPT4AllConfig import GPT4AllConfig

import requests
import json

class GPT4AllHelper:

    # LLM config
    model: str
    max_tokens: int
    temperature: float

    def __init__(self, model = "Llama 3.2 1B Instruct", max_tokens = 50, temperature = 0.28):
        """
        Construct a new model using GPT4All's local API

        :param  model           Preferred model to use (optional, default Phi-3 Mini Instruct)
        :param  max_tokens      Maximum number of tokens for the response
        :param  temperature     Desired temperature for the model
        """
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.settings = GPT4AllConfig()

    def get_models(self) -> Optional[dict]:
        """
        Get the available models from where the API is hosted

        :return:    requests.Response   Response object
        """
        response = requests.get(self.settings.models_url)

        return response.json() if response.status_code == 200 else None

    def post(self, endpoint: str, prompt: str) -> requests.Response:
        """
        Send a POST request to the API

        :param      endpoint:   Desired endpoint
        :param      prompt:     Prompt for the model (text-only)
        :return:    Response:   Response object containing status code, JSON and more
        """
        # Send the request to the server
        return requests.post(
            endpoint,
            data=json.dumps(self._get_data(prompt)),
            headers=GPT4AllConfig.headers
        )

    def prompt(self, prompt: str) -> requests.Response:
        """
        Send a prompt to the completion endpoint of GPT4All to
        complete text/answer questions/etc.

        :param      prompt:     Prompt for the model (text-only)
        :return:    Response:   Response object containing status code, JSON and more
        """
        return self.post(endpoint=self.settings.prompt_url, prompt=prompt)

    def chat(self, prompt) -> requests.Response:
        """
        Send a prompt to the chat completion endpoint of GPT4All to
        chat with the model.

        :param      prompt:     Prompt for the model (text-only)
        :return:    Response:   Response object containing status code, JSON and more
        """
        return self.post(endpoint=self.settings.chat_url, prompt=prompt)

    def _get_data(self, prompt: str):
        """ Helper function to prepare JSON data for API """
        return {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }