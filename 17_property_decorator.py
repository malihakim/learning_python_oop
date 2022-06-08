#property decorator
#gives class attributes getter, setter and deleter functionality (from other lang)

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    #fixes need to change all instances
    #define like method but access like attribute
    @property  
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    #we need to parse string 
    
    @fullname.setter    #name of method
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
        
emp1 = Employee('John', 'Smith')
emp1.first = 'Jim'
#does not change in self.email
#if new method is made, code breaks for others
#all instances will need to be changed (emp2.email --> emp2.email())

emp1.fullname = 'Corey Schafer'
print(emp1.first)      
print(emp1.email)
print(emp1.fullname)  

del emp1.fullname

#no need to change code to access attribute

