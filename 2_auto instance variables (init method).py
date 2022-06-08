# first, last, pay are all attributes of class
# for action, methods can be added
class Employee:

    def __init__(self, first, last, pay): # methods created in a class receive instance as the first argument and this instance should be called self. After self other arguments to be accepted can be given. 
        self.first = first
        self.lname = last   # can be diff
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #method
    def fullname(self):
        return '{} {}'.format(self.first, self.lname)

    
# init method takes self as the instance and first, last, etc as arguments
# when separate instance is created (as below), self is passed as instance automatically
# hence, only names and other values need to be provided
emp1 = Employee('Corey', 'Schafer', 50000)       
emp2 = Employee('Test', 'User', 60000)


print(emp1.email)
print(emp2.email)

# To display full name, manually:
print('{} {}'.format(emp1.first, emp1.lname))

# With method:
print(emp1.fullname())
print(emp2.fullname())


