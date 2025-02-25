# Example prompt
import requests

from gpt.gpt4all.GPT4AllHelper import GPT4AllHelper

example_prompt: str = "Who is Lionel Messi?"

# Create a default GPT
gpt: GPT4AllHelper = GPT4AllHelper()

# Ask which models are available
#models_response: Optional[dict] = gpt.get_models()
#print(f"Available models response:\n{models_response}")

# Send our example prompt to the language model and get a response :D
example_response: requests.Response = gpt.chat(example_prompt)

# Print some information about the response
print(f"API responded with {example_response.status_code}")
print(f"JSON response:\n{example_response.json() if example_response.status_code == 200 else None}")