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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.pay)  # {} for pay, '{}' for names
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    #add 2 employees, and result = combined salary
    def __add__(self, other): #self + other
        return self.pay + other.pay

    #len on Employee = number of characters in name (maybe for doc)
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

#depending on data type, addition or concatonation is done
print(1+2)          #calls dunder add
print(int.__add__(1, 2))

print('a' + 'b')
print(str.__add__('a', 'b'))

print(len('test'))  #calls dunder len
print('test'.__len__())

print(emp1 + emp2)  #wo = TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'

print(len(emp1))    #wo = TypeError: 'str' object cannot be interpreted as an integer

#return NotImplemented allows another object to handle it before throwing an error
#like pass? but doesnt skip code but allows another object to handle
