class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + '.' + last + '@gmail.com'

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Kate', 'De Witte', 60000)

print(repr(emp1))
print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__())

print(int.__add__(1,2))
print(str.__add__('as', 'b'))

print(len(emp1))

emp1.fullname = 'Corey Schafer'
