from employee import Employee

class Department(Employee) :
    def __init__(self, emp_id,name,contact,email,age,salary,status,department ):
        super().__init__(emp_id, name,contact,email,age, salary,status)
        self.department = department

    def display(self):
        print(f"id:{self.emp_id},Name:{self.name},Contact:{self.contact},Email:{self.email},age:{self.age},Status:{self.status} department:{self.department}")
