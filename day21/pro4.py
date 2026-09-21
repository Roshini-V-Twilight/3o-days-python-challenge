import requests

url = input("Enter webpage URL: ")

response = requests.get(url)

with open("webpage.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Webpage HTML saved successfully.")