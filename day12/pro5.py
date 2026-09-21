import re

paragraph = input("Enter a paragraph: ")

numbers = re.findall(r"\d+", paragraph)

print("Numbers found:", numbers)
print("Total number of numbers:", len(numbers))