"""Encapsulation, making a variable private and writing a getter function for it"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get__age(self):
        return self.__age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age >0:
            self.__age = new_age
        else:
            raise ValueError('Age must be a positive integer')

class Employee(Person):
    def __init__(self, name, age, hobbies):
        super().__init__(name, age)
        self.hobbies = hobbies


emp1 = Employee("Sania", "23", "music")
# print(emp1.age) #'Employee' object has no attribute 'age' => bcz the attribute 'age' is private and can't be accessed by Employee class
print(emp1.get__age())
emp1.set_age(45)
print(emp1.get__age())