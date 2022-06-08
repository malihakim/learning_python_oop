class Employee:

    raise_amount = 1.04 # 100% + 4% raise

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount) 
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

# creates raise_amount attribute for emp1
# increases only emp1 raise account
emp1.raise_amount = 1.05 
print(emp1.__dict__)

print(emp1.fullname())
print(emp1.raise_amount)        # access class v from instance
print(Employee.raise_amount)    # access class v from class itself
