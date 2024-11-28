import os
import json
from datetime import datetime, timedelta

import requests


def load_api_key():
    parent_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    api_json_path = os.path.join(parent_dir_path, 'data', 'apikey.json')
    with open(api_json_path, 'r') as file:
        data = json.load(file)
    return data.get("apiKey")


def load_output_file_path():
    # Define BASE_DIR as the project's root directory
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(parent_dir, 'data')
    output_file_path = os.path.join(data_dir, 'articles.json')
    return output_file_path


def load_keywords():
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    input_json_path = os.path.join(current_file_path, '..', 'data', 'input.json')
    with open(input_json_path, 'r') as file:
        data = json.load(file)
    key, values = next(iter(data.items()))
    print("keywords to find: ", values)
    return key, values

def is_valid_article(article):
    title = article.get('title', '')
    description = article.get('description', '')
    return title != '[Removed]' and description != '[Removed]' and title != '' and description != ''

def fetch_news(url, api_key, news_keywords, lookback_days=10, max_articles=550):
    if not news_keywords:
        raise ValueError("news_keywords cannot be empty.")

    today = datetime.today()
    lookback_days_ago = today - timedelta(days=lookback_days)
    from_date = lookback_days_ago.strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    params = {
        "q": news_keywords,
        "language": "en",
        "from": from_date,
        "to": to_date,
        "apiKey": api_key,
        "page": 1,
        "sortBy": "publishedAt"
    }

    all_articles = []

    while len(all_articles) < max_articles:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            params['to'] = articles[-1]['publishedAt']
            articles = list(filter(is_valid_article, articles))
            all_articles.extend(articles)
            print(f"Retrieved {len(articles)} articles.")
        else:
            print(f"Failed to fetch page {page}: {response.status_code} {response.text}")
            break
    
    all_articles = all_articles[:max_articles]
    print(f"Total articles fetched: {len(all_articles)}")
    return all_articles



