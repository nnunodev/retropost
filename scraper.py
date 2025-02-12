import datetime
import json
import os
import requests
from bs4 import BeautifulSoup


def scrape_retrodo_news():
    response = requests.get("https://retrododo.com/category/news/")
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

        # Calculate the date 15 days ago
        fifteen_days_ago = datetime.datetime.now() - datetime.timedelta(days=15)

        # Check if the post date is within the last 15 days
        if post_date >= fifteen_days_ago:
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
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/retrodo_news.json', 'w') as f:
        json.dump(news_data, f, indent=4)


# This part is only for testing the scraper independently
# if __name__ == "__main__":
#     scrape_retrodo_news()
