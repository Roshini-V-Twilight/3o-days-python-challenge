import re

phone = input("Enter a phone number: ")

pattern = r"^[6-9]\d{9}$"

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")