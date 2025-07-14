# Sorting lists, tuples and Objects

li = [9,6,3,4,0,2,5,6,10]

"""sorted() method sorts the lists and return a new variable"""
# s_li = sorted(li)
# print(s_li)
#
"""sort(), sorts in place, returns null"""
# li.sort()  # reverse=True to sort in descending order
# print(li)
#
"""sorts in descending order"""
# s_li = sorted(li, reverse=True)
# print(s_li)

"""Sorting a tuple"""
# tup = (9,6,3,4,0,2,5,6,10)
# s_tup = sorted(tup)
# print('Tuple\t', s_tup)

"""Sorting a dictionary"""
# dic = {'name':'Sania', 'hobbies':'procatination'}
# s_dic = sorted(dic)
# print('Sorted Dic\t', s_dic)

"""To sort on the basis of a specific value"""
# list = [-6,-5,-4,1,2,3]
# s_list = sorted(list, key=abs)
# print(s_list)

"""To sort Object with a specific attribute, 3 ways to do it"""
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '{},{},${}'.format(self.name, self.age, self.salary)

e1 = Employee('Ayesha', 23, 0)
e2 = Employee('Aleeza', 25, 110)
e3 = Employee('Batima', 22, 110)

l_emp = [e1,e2,e3]

"""WAY 1"""
def sort_emp(self):
    return self.age

s_emp = sorted(l_emp, key=sort_emp, reverse=True) # key=emp.name, the name is being returned that tells the sorted function to sort on the basis of the employee's name
print(s_emp)

"""WAY 2 => Using lamba"""
s_emp = sorted(l_emp, key=lambda e:e.name)

"""WAY 3, IMPORTING THE ATTRIBUTE GETTER FUNC"""
from operator import attrgetter
s_emp = sorted(l_emp, key=attrgetter('age'))
print(s_emp)
