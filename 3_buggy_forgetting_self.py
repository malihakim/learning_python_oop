class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.lname = last  
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #forgetting self argument for instance
    def fullname():
        return '{} {}'.format(self.first, self.lname)

emp1 = Employee('Corey', 'Schafer', 50000)       
emp2 = Employee('Test', 'User', 60000)

print(emp1.fullname())
# TypeError: fullname() takes 0 positional arguments but 1 was given
# Although, we pass no arguments into fullname(), the instance (emp2) gets passed automatically

# We can run from class
print(Employee.fullname(emp1))
# however, we have to manually enter instance
# as it does not know what instance to run the method with

