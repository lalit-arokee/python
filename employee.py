from abc import ABC, abstractmethod

class Employee :
    def __init__(self, emp_id,name, contact, email, age,salary, status):
        self.emp_id =emp_id
        self.name =name
        self.contact =contact
        self.email =email
        self.age = age
        self.salary =salary
        self.status =status
        
    def get_name(self):
        return self._name
    
    def get_contact(self):
        return self._contact
        
    def get_email(self):
        return self._email
    
    def get_age(self):
        return self._age

    def get_salary(self):
        return self.__salary
    
    def get_status(self):
        return self._status

    @abstractmethod
    def display(self):
        pass