import requests
from bs4 import BeautifulSoup

url = input("Enter webpage URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

for paragraph in paragraphs:
    print(paragraph.get_text(strip=True))