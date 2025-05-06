import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_shl_catalog():
    base_url = "https://www.shl.com/solutions/products/product-catalog/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    assessments = []
    for card in soup.select(".product-card"):
        name_tag = card.select_one(".product-card__title")
        url_tag = card.select_one("a.product-card__link")
        if not name_tag or not url_tag:
            continue
        name = name_tag.text.strip()
        url = url_tag['href']
        if not url.startswith('http'):
            url = 'https://www.shl.com' + url
        # For demo purposes, add dummy values for other fields
        assessments.append({
            "name": name,
            "url": url,
            "description": name + " assessment from SHL.",
            "remote_testing_support": "Yes",
            "adaptive_irt_support": "No",
            "duration": "60 minutes",
            "test_type": "General"
        })
    os.makedirs("../data", exist_ok=True)
    with open("../data/assessments.json", "w") as f:
        json.dump(assessments, f, indent=2)
    print(f"Scraped {len(assessments)} assessments.")

if __name__ == "__main__":
    scrape_shl_catalog()
