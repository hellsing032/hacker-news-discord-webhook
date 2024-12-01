import time
import requests
import feedparser
import argparse

# Webhook URL
webhook_url = ""

# RSS Feed URL
rss_url = "https://feeds.feedburner.com/TheHackersNews"

def fetch_news():
    """
    Fetch news from The Hacker News RSS feed.
    """
    feed = feedparser.parse(rss_url)
    news_list = []

    for entry in feed.entries:
        # Check if the enclosure field exists for the image
        image_url = None
        if "enclosures" in entry and len(entry.enclosures) > 0:
            image_url = entry.enclosures[0].get("url")

        # Create a news item dictionary
        news = {
            "title": entry.title,
            "link": entry.link,
            "description": entry.summary,
            "published": entry.published,
            "image": image_url
        }
        news_list.append(news)

    return news_list

def send_news_via_webhook(news_list):
    """
    Send the news to Discord via webhook.
    """
    for news in news_list:
        embed = {
            "embeds": [
                {
                    "title": news["title"],
                    "url": news["link"],
                    "description": news["description"],
                    "color": 0x1E90FF,  # Dodger Blue
                    "footer": {"text": f"Published: {news['published']}"},
                }
            ]
        }

        if news["image"]:  # Add image to the embed if available
            embed["embeds"][0]["image"] = {"url": news["image"]}

        response = requests.post(webhook_url, json=embed)

        if response.status_code == 204:
            print(f"News '{news['title']}' sent successfully!")
        else:
            print(f"Failed to send news: {response.status_code}, {response.text}")

        time.sleep(2)  # Optional delay between sending messages

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-w', '--webhook-url', help='Discord Webhook URL', required=True)
    parser.add_argument("-s", "--interval", type=int, help="Scraping interval in seconds", required=True)
    parser.add_argument('-h', "--help", action="help", help="Show this message and exit")
    args = parser.parse_args()

    webhook_url = args.webhook_url
    scrape_interval = args.interval

    if not webhook_url:
        parser.print_help()
        exit(0)

    print("Starting to scrape and send news...")
    while True:
        news_list = fetch_news()
        if news_list:
            send_news_via_webhook(news_list)
        time.sleep(scrape_interval)
