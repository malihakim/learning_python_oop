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

    #add developers programming language
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  #let Employee handle first, last, pay
        # OR Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    #pass a list of employees managed by manager
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  
        if employees is None:
            self.employees = [] #never pass mutable data types as default arguments 
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    #print all employees in list
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'Employee', 50000, 'Java') #inherited from Employee class

print(dev1.prog_lang)


mgr1 = Manager('Sue', 'Smith', 90000, [dev1]) #dev1 in list - [Corey Schafer]

print(mgr1.email)       #common code from Employee

mgr1.add_emp(dev2)      #[Corey Schafer, Test Employee]
mgr1.remove_emp(dev1)   #[Test Employee]
Manager.print_emps(mgr1)


