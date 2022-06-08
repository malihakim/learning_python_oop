class Employee:

    # class variable
    numEmps = 0          # +1 using init method
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numEmps += 1 # adds one everytime init method is called
        
        # raises is a class value that can be overwritten for diff employees
        # no. of emp is same for all 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.numEmps) # no employees

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(Employee.numEmps) # 2 employees created
