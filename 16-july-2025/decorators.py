"""Decorators take a function as a parameter, enhance/modify it and then returns a function"""

"""Simple decorator"""
# def decorator(func):
#     def inner_decor():
#         print("Before enhancing the function")
#         func()
#         print("After enhancing the function")
#     return inner_decor
#
# def to_be_enhanced():
#     print("I will be enhanced in the decorator!")
#
# my_func = decorator(to_be_enhanced)
# my_func()

"""Simple decorator to add 5 in a num and return it"""
# def decor(func):
#     def inner():
#         a = func()
#         add = a+5
#         return add
#     return inner
#
# @decor
# def num():
#     return 10
#
# print(num())

"""Enhancing a function twice"""
def decor1(func):
    def inner():
        a = func()
        multi = a*5
        return multi
    return inner

def decor(func):
    def inner():
        b = func()
        add = b+5
        return add
    return inner


def num():
    return 10

num = decor(decor1(num))
print(num())