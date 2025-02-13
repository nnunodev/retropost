from .logger import logger
from utils.exceptions import APIError
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def generate_content(api_key: str, prompt: str) -> str:
    """Generate content using the provided API key."""
    client = MistralClient(api_key=api_key)
    try:
        # Using mistral-tiny for testing, can be changed to:
        # - mistral-tiny
        # - mistral-small
        # - mistral-medium
        # - mistral-large
        chat_response = client.chat(
            model="mistral-tiny",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        logger.error(f"Failed to generate content: {e}")
        raise APIError(f"Mistral API error: {str(e)}")
