import os
import logging
from dotenv import load_dotenv
from atproto import Client
from google import genai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_env_variables():
    """Load environment variables from .env file."""
    load_dotenv()  # Load variables from .env into os.environ
    api_key = os.getenv('API_KEY')
    bsky_handle = os.getenv('BSKY_HANDLE')
    bsky_password = os.getenv('BSKY_PASSWORD')

    if not api_key:
        logger.error("Missing API_KEY environment variable. Please check your .env file.")
        raise ValueError("Missing API_KEY environment variable")
    if not bsky_handle:
        logger.error("Missing BSKY_HANDLE environment variable. Please check your .env file.")
        raise ValueError("Missing BSKY_HANDLE environment variable")
    if not bsky_password:
        logger.error("Missing BSKY_PASSWORD environment variable. Please check your .env file.")
        raise ValueError("Missing BSKY_PASSWORD environment variable")

    return api_key, bsky_handle, bsky_password

def login_to_client(bsky_handle, bsky_password):
    """Login to the client using the provided handle and password."""
    client = Client()
    try:
        client.login(bsky_handle, bsky_password)
    except Exception as e:
        logger.error(f"Failed to login: {e}")
        raise
    return client

def get_profile(client, bsky_handle):
    """Retrieve the profile for the given handle."""
    try:
        profile = client.get_profile(bsky_handle)
    except Exception as e:
        logger.error(f"Failed to get profile: {e}")
        raise
    return profile

def generate_content(api_key):
    """Generate content using the provided API key."""
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents="Explain how AI works"
        )
    except Exception as e:
        logger.error(f"Failed to generate content: {e}")
        raise
    return response.text

def main():
    """Main function to execute the script."""
    api_key, bsky_handle, bsky_password = load_env_variables()
    logger.info("Environment variables loaded successfully")

    client = login_to_client(bsky_handle, bsky_password)
    logger.info("Logged in to client successfully")

    profile = get_profile(client, bsky_handle)
    logger.info(f"Profile: {profile}")

    content = generate_content(api_key)
    logger.info(f"Generated content: {content}")

if __name__ == "__main__":
    main()