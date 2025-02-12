import os
from dotenv import load_dotenv
from utils.logger import logger


def check_env_variable(var_name):
    value = os.getenv(var_name)
    if not value:
        logger.error(
            f"Missing {var_name} environment variable. Please check your .env file.")
        raise ValueError(f"Missing {var_name} environment variable")
    return value


def load_env_variables():
    """Load environment variables from .env file."""
    load_dotenv()  # Load variables from .env into os.environ
    api_key = check_env_variable('MISTRAL_KEY')
    bsky_handle = check_env_variable('BSKY_HANDLE')
    bsky_password = check_env_variable('BSKY_PASSWORD')
    return api_key, bsky_handle, bsky_password
