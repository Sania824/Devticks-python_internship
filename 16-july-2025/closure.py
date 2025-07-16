"""Underlying concepts => First class functions & Closures"""

#First class functions
"""First class functions can be assigned to variables, returned in functions, passed as arguements and stored in data structures (list, dictionaries, etc)"""

"""A basic function to get the gist of closures"""
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()
my_func() # prints Hi

