import requests
from bs4 import BeautifulSoup

url = input("Enter news website URL: ")

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(["h1", "h2", "h3"])

print("Article Titles:\n")

for title in titles:
    text = title.get_text(strip=True)

    if text:
        print(text)