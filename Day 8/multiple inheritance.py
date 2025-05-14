class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}."

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
    def get_id(self):
        return f"My employee ID is {self.employee_id}."

class Manager(Employee, Person):
    def __init__(self, name, employee_id, department):
        Person.__init__(self, name)
        Employee.__init__(self,name)
        self.department = department
    def show_details(self):
        return f"{self.greet()} {self.get_id()} I manage the {self.department} department."
    
manager = Manager("Alice", "E12345", "Sales")

print(manager.greet())
print(manager.get_id())
print(manager.show_details())