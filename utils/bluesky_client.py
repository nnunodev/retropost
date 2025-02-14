from typing import Any, Dict
from utils.logger import logger
from atproto import Client
from utils.exceptions import BlueSkyError

def login_to_bluesky_client(bsky_handle: str, bsky_password: str) -> Client:
    """Login to the BlueSky client.
    
    Args:
        bsky_handle: BlueSky handle
        bsky_password: BlueSky password
    Returns:
        Client: Authenticated client instance
    Raises:
        BlueSkyError: If login fails
    """
    client = Client()
    try:
        client.login(bsky_handle, bsky_password)
    except Exception as e:
        logger.error(f"Failed to login to BlueSky: {e}")
        raise BlueSkyError(f"Login failed: {str(e)}")
    return client

def get_profile(client: Client, bsky_handle: str) -> Dict[str, Any]:
    """Retrieve the profile for the given handle from BlueSky.
    
    Args:
        client: Authenticated client instance
        bsky_handle: BlueSky handle
    Returns:
        Dict[str, Any]: Profile information
    Raises:
        BlueSkyError: If profile retrieval fails
    """
    try:
        profile = client.get_profile(bsky_handle)
    except Exception as e:
        logger.error(f"Failed to get BlueSky profile: {e}")
        raise BlueSkyError(f"Profile retrieval failed: {str(e)}")
    return profile
