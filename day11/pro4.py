from datetime import date, timedelta

today = date.today()

future_date = today + timedelta(days=100)

print("Date after 100 days:", future_date.strftime("%d-%m-%Y"))