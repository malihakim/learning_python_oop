#emulate built-in behaviour and implement operator overloading
#dunder init, dunder repr, dunder str

class Employee:
    raise_amt = 1.04 

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #we should be able to copy paste into Python
    #and recreate the object
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.pay)  # {} for pay, '{}' for names
    
    #readable for end-user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1) #str over repr

print(repr(emp2))
#OR print(emp1.__repr__())

print(str(emp2))
#OR print(emp1.__str__())
