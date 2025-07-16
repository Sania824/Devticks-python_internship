"""Create a decorator to print the function"""

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'{func.__name__} got executed in {end-start} time')
        return result
    return wrapper

def ex_func(n):
    time.sleep(n)

my_func = timer(ex_func)
my_func(2)