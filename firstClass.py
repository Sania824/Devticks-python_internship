class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{self.first} {self.last}'

emp_1 = Employee('sania', 'aimen', 50000)

print(emp_1.email)