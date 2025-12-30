# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
from youtube_scraper.scraper import scrape_trending

def main():
    print("Starting YouTube Trending Scraper...")
    
    videos = scrape_trending()
    
    if videos:
        print("\n--- Trending Videos ---")
        for v in videos:
            print(f"#{v['rank']} - {v['title']} by {v['channel']} ({v['views']})")
        
        with open("trending.json", "w") as f:
            json.dump(videos, f, indent=4)
        print("\nData saved to trending.json")
    else:
        print("No videos found.")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
