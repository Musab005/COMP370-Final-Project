import argparse
import json
from src import load_api_key, fetch_news, load_keywords, load_output_file_path
import sys
import os

# Add the project's root directory to the PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


def parse_arguments():
    # usage: python newsapi.py [-b <# days to lookback>]
    parser = argparse.ArgumentParser(description="Fetch news articles")
    parser.add_argument('-b', '--lookback_days', help='number of days to look back', type=int, default=10)
    return parser.parse_args()


def main():
    args = parse_arguments()
    api_key = load_api_key()
    url = "https://newsapi.org/v2/everything"
    key, values = load_keywords()
    output_file_path = load_output_file_path()

    try:
        articles = fetch_news(url, api_key, values, args.lookback_days)
        print(f"Number of articles fetched: { len(articles)}")
        with open(output_file_path, 'w', encoding="utf-8", newline='') as output_file:
            json.dump(articles, output_file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    main()
