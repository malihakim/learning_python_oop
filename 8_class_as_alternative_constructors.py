# regular methods - in a class, takes instance as first argument (self)
# class methods - automatically takes class as first argument
# static methods

# class methods can be used to create objects in multiple ways

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
    
emp1 = Employee('ABC', 'XYZ', 50000)
emp2 = Employee('Test', 'User', 60000)

# if emp info is in string form separated hyphens
# it needs to be parsed each time

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-30000'
emp_str3 = 'Jane-Evans-90000'

new_emp1 = Employee.from_string(emp_str1)

print(new_emp1.email)
print(new_emp1.pay)








