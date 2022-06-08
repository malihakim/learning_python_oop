#why? - logically group data and functions to REUSE and BUILD UPON

#when associated with class:
#data - attribute
#function - method

# application where employees are represented by code
# each employee has specific attributes and methods
# eg: name, email address, pay, and actions
# use class as blueprint to use for each employee

# class is blueprint
# instance is each unique employee 


class Employee: # create class
    pass        # pass statement to leave class empty and avoid errors

emp1 = Employee()       # unique employee objects
emp2 = Employee()

# manual
emp1.first = 'Corey'
emp1.last = 'Schafer'
emp1.email = 'Corey.Schafer@company.com'
emp1.pay = 50000

emp2.first = 'Test'
emp2.last = 'User'
emp2.email = 'Test.User@company.com'
emp2.pay = 60000

print(emp1)
print(emp2)
print(emp1.email)
print(emp2.email)

# instance variables contain unique values 
