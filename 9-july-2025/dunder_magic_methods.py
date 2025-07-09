class Employee:
    # Constructor
    def __init__(self, fname, lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = '{}.{}@gmail.com'.format(self.fname, self.lname)

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    # unambiguous representation of objects, used in debugging and logging
    def __repr__(self):
        return '{}, {}'.format(self.fname, self.lname)

    # more useful for the end users
    def __str__(self):
        return '{} - {} - {}'.format(self.fullname(), self.email,self.pay)

    # to add our own functionality of how we want the addition to work for the objects
    def __add__(self, other):
        return self.pay + other.pay

    # modifying len() dunder method calculate the charracters of the full name of the employee
    def __len__(self):
        return len(self.fullname())

emp1 = Employee("Sania", "Aimen", 56000)
emp2 = Employee("Sahab", "Noor", 59000)

print(len(emp1))