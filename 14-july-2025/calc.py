# File to be tested

class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def subtract(x,y):
        return x - y

    @staticmethod
    def multiply(x,y):
        return x * y

    @staticmethod
    def divide(x,y):
        if y == 0:
            raise ValueError('Can not be divisible by zero!')
        return x / y