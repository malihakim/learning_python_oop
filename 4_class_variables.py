# class variables are shared among all instances of a class
# same for each instance

# for employees:
# annual raises may differ yearly but are same for each employee


class Employee:

    raise_amount = 1.04 # 4% raise (100% + 4%)

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount) OR
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1.fullname())
print(emp1.raise_amount)        # access class v from instance
print(Employee.raise_amount)    # access class v from class itself

print(emp1.__dict__)
print(Employee.__dict__)
