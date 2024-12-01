# The Hacker News to Discord Webhook

A Python script that fetches the latest news articles from **The Hacker News** RSS feed and sends them to a Discord channel using a webhook. 

## Features

- Fetches news articles, including title, description, link, and image.
- Sends formatted embeds to a Discord channel via webhook.
- Automatically scrapes and sends news at user-defined intervals.

## Requirements

- Python 3.6 or higher.
- Libraries specified in `requirements.txt`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hellsing032/hacker-news-discord-webhook.git
    cd hacker-news-discord-webhook
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python main.py -w "YOUR_DISCORD_WEBHOOK_URL" -s 300
    ```

    Replace:
    - `"YOUR_DISCORD_WEBHOOK_URL"`: Your Discord webhook URL.
    - `300`: Scraping interval in seconds (e.g., 300 = 5 minutes).

## Usage

### Script Arguments

| Argument         | Description                                | Required |
|------------------|--------------------------------------------|----------|
| `-w`, `--webhook-url` | The Discord Webhook URL.                  | Yes      |
| `-s`, `--interval`     | Scraping interval in seconds.             | Yes      |
| `-h`, `--help`         | Show help message and exit.              | No       |

### Example Command

```bash
python main.py -w "https://discord.com/api/webhooks/your_webhook_id" -s 300
```

## Contributing to this Project

Contributions are welcome and appreciated!  If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. 

## License
This project is licensed under the MIT License.