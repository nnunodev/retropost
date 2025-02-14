import time
from config import MISTRAL_CONFIG
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from .logger import logger
from .exceptions import APIError
import os
from typing import Dict, Any, List

class MistralGenerator:
    def __init__(self):
        api_key = os.getenv("MISTRAL_KEY")  # Consistent with .env file
        if not api_key:
            raise APIError("MISTRAL_KEY environment variable not found")
        self.client = MistralClient(api_key=api_key)
        self.last_request_time = 0
        self.min_request_interval = 1  # Minimum 1 second between requests

    def _rate_limit(self):
        """Implement basic rate limiting."""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()

    def generate_post(self, news_item: Dict[str, str]) -> str:
        """Generate a social media post from news item.
        
        Args:
            news_item: Dictionary containing title and link
        Returns:
            str: Generated post content
        Raises:
            APIError: If API call fails
        """
        self._rate_limit()
        prompt = f"""Generate a short, engaging Bluesky post about this gaming news:
Title: {news_item['title']}
Link: {news_item['link']}

Include relevant hashtags. Keep it under 300 characters."""

        try:
            messages = [ChatMessage(role="user", content=prompt)]
            response = self.client.chat(
                model=MISTRAL_CONFIG['model'],
                messages=messages,
                max_tokens=MISTRAL_CONFIG['max_tokens'],
                temperature=MISTRAL_CONFIG['temperature']
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Failed to generate post: {e}")
            raise APIError(f"Mistral API error: {str(e)}")

    def generate_content(self, prompt: str) -> str:
        """Generate general content using the provided prompt."""
        try:
            chat_response = self.client.chat(
                model="mistral-tiny",
                messages=[{"role": "user", "content": prompt}]
            )
            return chat_response.choices[0].message.content
        except Exception as e:
            logger.error(f"Failed to generate content: {e}")
            raise APIError(f"Mistral API error: {str(e)}")
