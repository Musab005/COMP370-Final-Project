import csv
import os
import json

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file_path = os.path.join(root_dir, "data", "articles.json")
csv_file_path = os.path.join(root_dir, "data", "articles.csv")


with open(json_file_path, "r", encoding="utf-8") as f:
    articles = json.load(f)

fields = ["title", "description", "url", "coding"]

csv_data = []
for article in articles:
    csv_data.append({
        "title": article.get("title", ""),
        "description": article.get("description", ""),
        "url": article.get("url", ""),
        "coding": "",
    })

with open(csv_file_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(csv_data)

print(f"Data successfully written to {csv_file_path}")
