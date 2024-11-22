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
    api_json_path = os.path.join(current_file_path, '..', 'data', 'input.json')
    with open(api_json_path, 'r') as file:
        data = json.load(file)
    key, values = next(iter(data.items()))
    print("key and values: ", key, values)
    return key, values


def fetch_news(url, api_key, news_keywords, lookback_days=10):
    if not news_keywords:
        raise ValueError("news_keywords cannot be empty.")

    articles_list = []
    today = datetime.today()
    lookback_days_ago = today - timedelta(days=lookback_days)
    from_date = lookback_days_ago.strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    params = {
        "q": news_keywords,
        "language": "en",
        "from": from_date,
        "to": to_date,
        "apiKey": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for article in data["articles"]:
            articles_list.append(article)
    else:
        error = response.json()
        status = error["status"]
        code = error["code"]
        message = error["message"]
        print(f"Failed to retrieve data. Status code: {status} {code}")
        print(f"Details: {message}")

    return articles_list
