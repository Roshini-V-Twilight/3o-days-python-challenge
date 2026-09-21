import re

sentence = input("Enter a sentence: ")

digits = re.findall(r"\d", sentence)

print("Digits found:", digits)