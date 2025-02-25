"""
SystemPrompt.py

Representation of a prompt from an external file for the LLM, so
we can keep our prompts nice and maintainable.
"""
from typing import Optional


class SystemPrompt:

    fname: str
    content: Optional[str] = None

    def __init__(self, fname: str):
        self.fname = fname

    def get_content(self) -> str:
        """ Get the content of the system prompt """
        # Read the prompt if necessary
        if not self.content:
            with open(self.fname, 'r') as f:
                prompt = f.read()

        return prompt