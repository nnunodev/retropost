import os
import logging
import argparse
from dotenv import load_dotenv
from atproto import Client 
from google import genai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_env_variable(var_name):
    value = os.getenv(var_name)
    if not value:
        logger.error(f"Missing {var_name} environment variable. Please check your .env file.")
        raise ValueError(f"Missing {var_name} environment variable")
    return value

def load_env_variables():
    """Load environment variables from .env file."""
    load_dotenv()  # Load variables from .env into os.environ
    api_key = check_env_variable('API_KEY')
    bsky_handle = check_env_variable('BSKY_HANDLE')
    bsky_password = check_env_variable('BSKY_PASSWORD')
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

def generate_content(api_key, prompt):
    """Generate content using the provided API key."""
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
    except Exception as e:
        logger.error(f"Failed to generate content: {e}")
        raise
    return response.text

def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser(description="Run the retropost script.")
    parser.add_argument('--prompt', type=str, default="Explain how AI works", help="Prompt for content generation")
    args = parser.parse_args()

    api_key, bsky_handle, bsky_password = load_env_variables()
    logger.info("Environment variables loaded successfully")
    logger.critical("This is a critical message")

    client = login_to_client(bsky_handle, bsky_password)
    logger.info("Logged in to client successfully")

    profile = get_profile(client, bsky_handle)
    logger.info(f"Profile: {profile}")

    content = generate_content(api_key, args.prompt)
    logger.info(f"Generated content: {content}")

if __name__ == "__main__":
    main()