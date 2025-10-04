import calendar
from datetime import date, timedelta, time, datetime


print(f"is 1900 a leap year: {calendar.isleap(1900)}")
print(f"is 1996 a leap year: {calendar.isleap(1996)}")

haloween = date(2025, 10, 31)
print(f"haloween date: {haloween}")
print(
    f"haloween year: {haloween.year}, haloween month: {haloween.month}, haloween day: {haloween.day}"
)

now = date.today()
print(f"now date: {now}")

one_day = timedelta(days=1)
tomorrow = now + one_day
print(f"tomorrow date: {tomorrow}")

noon = time(12, 0, 0)
print(f"noon time: {noon}")
print(f"noon hour: {noon.hour}, noon minute: {noon.minute}, noon second: {noon.second}")

some_day = datetime(2025, 1, 2, 12, 30, 0, 0)
print(f"some_day date: {some_day}")

current_datetime = datetime.now()
print(f"current_datetime: {current_datetime}")
print(current_datetime.date())
print(current_datetime.time())

# formatting dates
my_day = date(2012, 12, 31)
fmt = "It's a %A, %B, %d, %Y"
val = my_day.strftime(fmt)
print(val)

fmt_date = "%d-%M-%Y"
my_date = datetime.strptime("28-04-2012", fmt_date)
print(my_date)
