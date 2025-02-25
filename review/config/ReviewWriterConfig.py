"""
ReviewWriterConfig.py

Contains the settings for the review writer's GPT
"""

class ReviewWriterConfig:

    # LLM config
    model: str = "Llama 3.2 1B Instruct"
    max_tokens: int = 200
    temperature: float = 0.3
    prompt_file: str = "./prompts/write_review_prompt.txt"