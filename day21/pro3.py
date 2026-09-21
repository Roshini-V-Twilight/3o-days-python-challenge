import requests
from bs4 import BeautifulSoup

url = input("Enter webpage URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

print("Number of images:", len(images))