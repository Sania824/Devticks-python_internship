import random
import math
import datetime
import calendar
import os

# working with random method
hobbies = ["golfing", "painting", "singing", "dancing"]

random_hobb = random.choice(hobbies)
print(random_hobb)

# working with math method to convert 90 to its radians value, then taking its sin
rads = math.radians(90)
print(math.sin(rads)) # sin is function in the math module

today = datetime.date.today()
print(today)

print(calendar.isleap(2024))
print(os.getcwd())
print(os.__file__)