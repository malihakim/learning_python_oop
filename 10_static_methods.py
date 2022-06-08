# regular methods pass instance as first argument (called self)
# class methods pass class as first argument (called cls)

# static methods do not pass any arguments
# They have some logical connection with class

# Function that takes a date and returns if workday
# does not require class but is related
# Monday = 0, T=1, W=2, Sunday = 6 as per Python

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

    @classmethod   
    def set_raise_amt(cls, amount):  # cls == self
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod           # decorator
    def is_workday(day):    # we can directly pass argument
        if day.weekday() == 4 or day.weekday() == 5: # Friday and Saturday
            return False
        return True   

emp1 = Employee('ABC', 'XYZ', 50000)
emp2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2020, 8, 28)

print(Employee.is_workday(my_date))

# if you dont access instance or class, static method could be used          






