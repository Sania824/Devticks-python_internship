# Lists
courses = ['a','b','c','d']

courses.append('e') # adds the item to the end of the list

courses.insert(3,'f')

courses2 = ['e','f','g']
courses.extend(courses2)

popped = courses.pop()


#Sorting the Lists

courses = ['Maths','Geography','History','Comp Sci']
nums = [5,2,3,4,1]

courses.sort()
nums.sort()
print(courses)
print(nums)

#Finding Lists
print(courses.index('c'))
print('e' in courses)

for course in courses:
    print(course)

#enumerate function to get the index along with each element
for index, course in enumerate(courses, start=1):
    print(index,course)


# Sets
cs_courses = {1,4,2,3,4,3}
print(cs_courses)


mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi','mango'] # ek tarha se replacement
print(mylist)

mylist = ["apple","banana","cherry"]
mylist.clear()
print(mylist)