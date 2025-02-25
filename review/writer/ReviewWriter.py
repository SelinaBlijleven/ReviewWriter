"""
ReviewWriter.py

A little BS factory
"""
from typing import Optional

import requests

from gpt.gpt4all.GPT4AllHelper import GPT4AllHelper
from review.config.ReviewWriterConfig import ReviewWriterConfig
from gpt.SystemPrompt import SystemPrompt


class ReviewWriter:

    gpt: GPT4AllHelper
    review_prompt: SystemPrompt

    def __init__(self):
        # Load our own settings
        config = ReviewWriterConfig()

        # Pass the settings to our GPT writer
        self.gpt: GPT4AllHelper = GPT4AllHelper(
            model=config.model,
            max_tokens=config.max_tokens,
            temperature=config.temperature
        )

        # Set the file location for the system prompt with
        # a path from the prompts folder.
        self.review_prompt = SystemPrompt(config.prompt_file)

    def generate_review(self) -> Optional[str]:
        """ Generate a fake review using the configured GPT. """
        api_response: requests.Response = self.gpt.chat(self.review_prompt.get_content())

        # Without a proper response we can not extract a review
        if api_response.status_code != 200: return None

        # Extract the message content from the first choice
        choices: Optional[list] = api_response.json().get('choices', None)

        # Fail-safe for when there would be no available answers
        if not choices: return None

        # Extract the message if we can
        return choices[0].get('message', None).get('content', None)

