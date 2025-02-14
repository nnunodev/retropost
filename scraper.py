import datetime
import json
import os
import requests
from bs4 import BeautifulSoup
from config import SCRAPING_CONFIG
from utils.exceptions import ScrapingError
from utils.logger import logger
from typing import List, Dict
from pathlib import Path

def scrape_retrodo_news() -> List[Dict[str, str]]:
    """Scrape news from RetroRodo website.
    
    Returns:
        List of news items with title, summary, link, and date
    Raises:
        ScrapingError: If scraping fails
        RequestException: If network request fails
    """
    try:
        response = requests.get(SCRAPING_CONFIG['base_url'])
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article previews on the page
        article_previews = soup.find_all('div', class_='elementor-post__text')

        news_data = []
        for preview in article_previews:
            title_element = preview.find(
                'h3', class_='elementor-post__title').find('a')
            title = title_element.text.strip()
            link = title_element['href']
            date_str = preview.find(
                'span', class_='elementor-post-date').text.strip()
            post_date = datetime.datetime.strptime(date_str, '%B %d, %Y')

            # Extract summary (from <p> tag)
            summary_element = preview.find('p')

            # Check if summary_element exists before extracting text
            if summary_element:
                summary = summary_element.text.strip()
            else:
                summary = "No summary available"

            # Calculate the date threshold using config
            days_ago = datetime.datetime.now() - datetime.timedelta(days=SCRAPING_CONFIG['days_threshold'])

            # Check if the post date is within the configured days
            if post_date >= days_ago:
                news_data.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "post_date": date_str  # Store the original date string
                })
                print(f"Title: {title}")
                print(f"Summary: {summary}")
                print(f"Link: {link}")
                print(f"Post Date: {post_date}")

        # Create data directory if it doesn't exist
        if not os.path.exists(SCRAPING_CONFIG['data_directory']):
            os.makedirs(SCRAPING_CONFIG['data_directory'])
        with open(f"{SCRAPING_CONFIG['data_directory']}/retrodo_news.json", 'w') as f:
            json.dump(news_data, f, indent=4)
    except requests.exceptions.RequestException as e:
        logger.error(f"Network request failed: {e}")
        raise ScrapingError(f"Network error: {str(e)}")
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        raise ScrapingError(str(e))
