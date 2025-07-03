# def hello_func():
#     for i in range(4):
#         print("Hello Function!")
#
# hello_func()

# returning multiple values
def fun():
    name = 'Alice'
    age = 25
    return name, age

name, age = fun()
print(name)
print(age)

# Using parameters
def helloFunc(greeting):
    return f'{greeting} Function.'

print(helloFunc('Hey!'))

def is_true(a):

    # returning boolean of a
    return bool(a)

res = is_true(1>0)
print(res)

# Printing Sun Function
def sum(a,b):
    return a+b
# Arguments can be passed either through variables or directly
a=10
b=5
print(sum(10,5))

# Printing exponents
def exponent(n):
    return [n**2, n**3]

print(exponent(4))
