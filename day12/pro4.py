import re

sentence = input("Enter a sentence: ")

result = re.sub(r"\s", "_", sentence)

print("Updated sentence:", result)