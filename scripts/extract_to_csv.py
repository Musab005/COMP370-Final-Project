import csv
import os
import json
from datetime import datetime

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file_path = os.path.join(root_dir, "data", "articles.json")
csv_file_path = os.path.join(root_dir, "data", "articles.csv")


with open(json_file_path, "r", encoding="utf-8") as f:
    articles = json.load(f)

fields = ["date", "title", "description", "coding"]

csv_data = []
for article in articles:
    date_unformatted = article.get("publishedAt", "")
    dt = datetime.strptime(date_unformatted, "%Y-%m-%dT%H:%M:%SZ")
    date = dt.date()

    csv_data.append({
        "date": date,
        "title": article.get("title", ""),
        "description": article.get("description", ""),
        "coding": "",
    })

with open(csv_file_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(csv_data)

print(f"Data successfully written to {csv_file_path}")
