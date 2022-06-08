class Employee:

    raise_amt = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee): 
    raise_amt = 1.10 

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'Employee', 50000, 'Java')

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])

#built-in finction isinstance tells if object is instance of a class
print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))

#built-in function issubclass tells if a class is a subclass of another
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

#subclass can also use another subclass
#class Interns(Employee):






