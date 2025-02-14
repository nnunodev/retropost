import argparse
from utils.env_loader import load_env_variables
from utils.logger import logger
from utils.bluesky_client import login_to_bluesky_client, get_profile
from utils.mistral_client import MistralGenerator
from utils.post_storage import PostStorage
from scraper import scrape_retrodo_news
import json
import sys
from typing import List, Dict, Any
from pathlib import Path

def generate_posts_from_news() -> None:
    """Generate posts from scraped news and save them.
    
    Raises:
        FileNotFoundError: If news file doesn't exist
        JSONDecodeError: If news file is invalid
    """
    try:
        # Initialize generators
        mistral = MistralGenerator()
        storage = PostStorage('data/generated_posts.json')
        
        # Load the scraped news
        with open('data/retrodo_news.json', 'r', encoding='utf-8') as f:
            news_items = json.load(f)
        
        # Generate posts for each news item
        generated_posts = []
        for news in news_items:
            post_content = mistral.generate_post(news)
            generated_posts.append({
                "original_title": news["title"],
                "original_link": news["link"],
                "post_date": news["post_date"],
                "generated_content": post_content
            })
        
        # Save generated posts
        storage.save_generated_posts(generated_posts)
        logger.info("Generated posts from news and saved successfully!")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to read news file: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise

def main() -> None:
    try:
        api_key, bsky_handle, bsky_password = load_env_variables()
        logger.info("Environment variables loaded successfully!\n")

        # Uncomment the following lines if you need to login and get the profile
        # client = login_to_bluesky_client(bsky_handle, bsky_password)
        # logger.info("Logged in to BlueSky client successfully")

        # profile = get_profile(client, bsky_handle)
        # logger.info(f"Profile: {profile}")

        # scrape_retrodo_news()
        # logger.info("Scraped retrodo news successfully!\n")

        generate_posts_from_news()
        logger.info("Generated posts from scraped news successfully!\n")
    except Exception as e:
        logger.error(f"Application failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
