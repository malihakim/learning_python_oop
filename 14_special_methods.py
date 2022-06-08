#CANNOT RUN AS NO CODE FOR REPR OR STR

#special (or magic) methods within classes
#emulate built-in behaviour in Python
#implement operator overloading

#change built-in behaviour to user-friendy 

#dunder init, dunder repr, dunder str
#called when repr or str is called

class Employee:
    raise_amt = 1.04 #100% + 4%

    def __init__(self, first, last, pay): #dunder init is init surrounded by underscores(__ = dunder)
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#usually print(emp) = <__main__.Employee object at 0x02F4B580>
    
    #repr - unambigous representation of the object
    #for developers
    def __repr__(self): #used for debugging and logging
        pass

    #str - readable representation of the object
    #for users
    def __str__(self): #used for display to the end-user
        pass

#dunder method is called when emp objects are created
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1)

#repr should be used atleast
#if str is called but no str is provided, repr is used instead

