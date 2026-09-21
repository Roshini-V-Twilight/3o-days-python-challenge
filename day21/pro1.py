import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    for link in links:
        href = link.get("href")

        if href:
            print(href)

except requests.exceptions.RequestException as e:
    print("Error:", e)