# regular methods - in a class, takes instance as first argument (self)
# class methods - automatically takes class as first argument
# static methods

class Employee:

    numEmps = 0
    raise_amt = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.numEmps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # regular method to class method
    # same as Employee.raise_amount = 1.03
    @classmethod   
    def set_raise_amt(cls, amount):  # cls == self
        cls.raise_amt = amount
    
emp1 = Employee('ABC', 'XYZ', 50000)
emp2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.03)
# accepts cls, so only amount needs to be entered
# changes all emp raise amts to 1.03
# without it, emp raise amts = 1.05

emp1.set_raise_amt(1.04)
# class methods from instances
# not common
# changes all emp raises to 1.04

print(Employee.raise_amt)   # class raise amt
print(emp1.raise_amt)       # instance raise amt
