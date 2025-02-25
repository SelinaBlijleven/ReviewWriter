"""
GPT4AllSettings.py

Contains the settings for the GPT4All API specifically

https://docs.gpt4all.io/gpt4all_api_server/home.html
"""

class GPT4AllConfig:
    host: str = "http://localhost:4891/v1"
    headers: dict[str, str] = {"Content-Type": "application/json"}
    prompt_url: str = f"{host}/completions"
    chat_url: str = f"{host}/chat/completions"
    models_url: str = f"{host}/models"

