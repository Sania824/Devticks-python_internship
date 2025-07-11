import datetime
from time import strftime
import pytz

# Working with dates
today = datetime.date.today()
print("Today's date:", today)
print("Weekday (0-6, Monday=0):", today.weekday())
print("ISO weekday (1-7, Monday=1):", today.isoweekday())

# Date calculations
reference_date = datetime.date(2025, 7, 11)
days_ago = datetime.timedelta(days=84)
print("84 days before reference date:", reference_date - days_ago)

# Counting down to my birthday
birthday = datetime.date(2025, 9, 21)
time_until_birthday = birthday - reference_date
print("Seconds until my birthday:", time_until_birthday.total_seconds())

# Timezone handling
current_utc = datetime.datetime.now(tz=pytz.UTC)
print("Current UTC time:", current_utc)

# Display all available timezones
print("\nAvailable timezones:")
for timezone in pytz.all_timezones:
    print(timezone)

# Local time conversion
local_time = datetime.datetime.now()
brisbane_time = local_time.astimezone(pytz.timezone('Australia/Brisbane'))
print("\nCurrent time in Brisbane:", brisbane_time)

# Date formatting and parsing
print("\nFormatted date:", local_time.strftime('%B %d, %Y'))
date_string = 'July 08, 2025'
parsed_date = datetime.datetime.strptime(date_string, '%B %d, %Y')
print("Parsed date:", parsed_date)