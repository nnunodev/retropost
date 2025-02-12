from utils.logger import logger
from atproto import Client  # Replace with the actual library


def login_to_bluesky_client(bsky_handle, bsky_password):
    """Login to the BlueSky client using the provided handle and password."""
    client = Client()
    try:
        client.login(bsky_handle, bsky_password)
    except Exception as e:
        logger.error(f"Failed to login to BlueSky: {e}")
        raise
    return client


def get_profile(client, bsky_handle):
    """Retrieve the profile for the given handle from BlueSky."""
    try:
        profile = client.get_profile(bsky_handle)
    except Exception as e:
        logger.error(f"Failed to get BlueSky profile: {e}")
        raise
    return profile
