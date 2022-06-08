def add_employee(emp, empList = None):
    if empList is None:
        empList = []
    empList.append(emp)
    print(empList)

emps = ['Jane', 'John']

add_employee('Corey')
add_employee('Joe')
add_employee('Joel')
