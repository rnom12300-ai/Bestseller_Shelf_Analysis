import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

with open(r"C:\Users\mylov\فاتن\Books.json", "r", encoding="utf-8") as f:
    books = json.load(f)

data_list = []

for book in books:
    url = book["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text.strip()
    price_tag = soup.select_one(".price_color")
    price = price_tag.text.strip() if price_tag else "N/A"
    category_tag = soup.select_one(".breadcrumb li:nth-child(3) a")
    category = category_tag.text.strip() if category_tag else "N/A"
    rating_tag = soup.select_one(".star-rating")
    rating = rating_tag["class"][1] if rating_tag else "N/A"

    data_list.append({
        "id": book["id"],
        "title": title,
        "price": price,
        "category": category,
        "rating": rating,
        "url": url
    })

df = pd.DataFrame(data_list)
df.to_csv("Books_Data.csv", index=False, encoding="utf-8-sig")

print("✅ تم استخراج البيانات وحفظها في الملف Books_Data.csv بنجاح!")


