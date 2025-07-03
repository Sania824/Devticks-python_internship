# Number of days per month. The first index does not count due to indexing purposes
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# Making a function if a year is a leap year
def is_leap(year):
    """Returns true for leap years anSd false for non-leap years"""
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0) # must be divisible by 4 and (either divisible by 100 or 400)

def days_in_month(year,month):
    """Returns days of month in that year"""

    # checks if the month is between 1-12
    if month < 1 or month > 12:
        return "Invalid Month"
    elif month == 2 and (is_leap(year) == True): # if month is 2 i.e. February, and it is also a leap year, then it returns the number of days in that month, that should be 2
        return 29
    else:
        return month_days[month]

    # if not February then simply returns the number of days of that month
    #return month_days[month]

print(days_in_month(2021,2))