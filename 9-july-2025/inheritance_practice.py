class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def print_name(self):
        print(self.first, self.last)

x = Person("Sania", "Aimen")
x.print_name()

class Student(Person):
    def __init__(self, fname, lname, year):
     super().__init__(fname, lname)
     self.graduationyear = year

    def print_name(self):
        print(self.first, self.last, self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.print_name()