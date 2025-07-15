"""The following code in the file is written to be tested"""

def celsius_to_fahrenheit(c_temp):
    if c_temp < 273.15:
        raise ValueError("Temperature can not be below absolute zero")
    return (c_temp * 9/5) + 32

def fahrenheit_to_celsius(f_temp):
    if f_temp < -459.67:  # Absolute zero in Fahrenheit
        raise ValueError("Temperature cannot be below absolute zero")
    return (f_temp + 32) * 5/9

num = celsius_to_fahrenheit(0)
print(num)