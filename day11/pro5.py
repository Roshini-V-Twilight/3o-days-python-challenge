from datetime import date

birth_date = date(2005, 5, 10)
today = date.today()

difference = today - birth_date

print("Difference in days:", difference.days)