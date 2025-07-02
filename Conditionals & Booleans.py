# if, else if statement
name = 'Samia'

if name == 'Sania':
    print("Name is Sania")
elif name == 'Sarah':
    print('Name is Sarah')
else:
    print('No match')

# and, or & not operators
user = 'Admin'
logged_in = True

if not logged_in:
    print('Welcome to the Admin Page')
else:
    print('Wrong credentails')

# Object Identity
a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))

print(a is b) # checks if both objects resides at the same memory location
