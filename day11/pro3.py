from datetime import date

birth_date = date(2005, 5, 10)
today = date.today()

age_in_days = (today - birth_date).days

print("Your age in days is:", age_in_days)