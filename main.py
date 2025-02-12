import argparse
from utils.env_loader import load_env_variables
from utils.logger import logger
from utils.bluesky_client import login_to_bluesky_client, get_profile
from utils.mistral import generate_content
from scraper import scrape_retrodo_news


def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser(description="Run the retropost script.")
    parser.add_argument('--prompt', type=str, default="Explain how AI works",
                        help="Prompt for content generation")
    args = parser.parse_args()

    api_key, bsky_handle, bsky_password = load_env_variables()
    logger.info("Environment variables loaded successfully!\n")

    # Uncomment the following lines if you need to login and get the profile
    # client = login_to_bluesky_client(bsky_handle, bsky_password)
    # logger.info("Logged in to BlueSky client successfully")

    # profile = get_profile(client, bsky_handle)
    # logger.info(f"Profile: {profile}")

    content = generate_content(api_key, args.prompt)
    logger.info(f"Generated content: {content}")

    scrape_retrodo_news()
    logger.info("Scraped retrodo news successfully!\n")

if __name__ == "__main__":
    main()
