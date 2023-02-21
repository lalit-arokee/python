from employee import Employee
from department import Department

class EmployeeManagement:
    def __init__(self):
        self._employees = []

    def remove_employee(self, employee):
        if isinstance(employee, Employee):
            self._employees.remove(employee)

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self._employees.append(employee)

    def display_all_employees(self):
        for employee in self._employees:
            employee.display()
            print()

management = EmployeeManagement()

emp1, emp2, emp3=Department(1,"name1",9887677887, "testemail@gmail.com",4,000,"DEpartment1","Active"), Department(2,"name2",89787987887, "test2@gmail.com",3,600,"DEpartment2", "Non Active"), Department(3,"name3",79877657587,"test3@gmail.com",1,800,"DEpartment3","Active")

management.add_employee(emp1, emp2, emp3)


management.remove_employee(emp1)

management.display_all_employees()
print(management._employees)