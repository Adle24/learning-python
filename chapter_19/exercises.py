from datetime import datetime, timedelta

# exercise 1
current_date = datetime.now().date()
fmt = "day: %d, month: %M, year: %Y"
str_date = datetime.strftime(current_date, fmt)

with open("today.txt", encoding="utf-8", mode="w") as f:
    f.write(str_date)

with open("today.txt", encoding="utf-8", mode="r") as f:
    today_str = f.read()
    print(today_str)

# exercise 2
birthday = datetime(1996, 7, 21).date()
print(birthday.isoweekday())

days = timedelta(days=10000)
future = birthday + days
print(future)
