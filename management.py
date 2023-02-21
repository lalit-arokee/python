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

emp1, emp2, emp3=Department(1,"name1",4,000,"DEpartment1"), Department(2,"name2",3,600,"DEpartment2"), Department(3,"name3",1,800,"DEpartment3")

management.add_employee(emp1, emp2, emp3)


management.remove_employee(emp1)

management.display_all_employees()
print(management._employees)