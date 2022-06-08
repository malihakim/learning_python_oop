#class inheritance
#inherit attributes and methods from a parent class
#subclass - inherit functionality of a class and overwrite wo loss

#create types of employees - developers and managers
class Employee:

    raise_amt = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee): #inherits from Employee
    raise_amt = 1.10 #10%

class Manager(Employee):
    pass

dev1 = Developer('ABC', 'XYZ', 50000)
dev2 = Employee('Test', 'Employee', 50000) #inherited from Employee class

print(dev1.email)
print(dev2.fullname())

print(dev1.pay)
dev1.apply_raise()  # Developer raise_amt of 10%
print(dev1.pay)

print(dev2.pay)
dev2.apply_raise()  # Employee raise_amt of 5%
print(dev2.pay)

print(help(Developer))
# Developer --> Employee --> object class (base object where every class in Python inherits from)
# Method Resolution Order
