student = {'name':'Sania', 'age':25, 'courses':['DSA','OS']}
print(student['courses'])

# adding a new key-value pair
student['phone'] = '0300-2929292'
print(student.get('phone', 'Not Found'))

# deleting a key-value pair
del student['age']
popped = student.pop('age')
print(popped)


print(student.items()) # shows entire dictionary

for keys, values in student.items(): # shows all keys and values
    print(keys, values)

