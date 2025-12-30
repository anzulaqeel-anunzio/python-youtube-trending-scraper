# YouTube Trending Video Metadata Scraper (Python)

A Python script to extract metadata (title, channel, view count) from the YouTube trending page.

> [!NOTE]
> This scraping tool parses the public HTML of the YouTube trending page. For robust, high-volume data access, use the official YouTube Data API.

## Features

-   **Trend Extraction**: Gets the top trending videos.
-   **Metadata Parsing**: Extracts video title, channel name, and view count.
-   **JSON Export**: Saves the data to a JSON file.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python run_scraper.py
```

## Configuration

Edit `youtube_scraper/config.py` to change the `TRENDING_URL` or `USER_AGENT`.

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
