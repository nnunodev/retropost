from utils.logger import logger
from mistralai import Mistral


def generate_content(api_key, prompt):
    """Generate content using the provided API key."""
    client = Mistral(api_key=api_key)
    try:
        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        logger.error(f"Failed to generate content: {e}")
        raise
