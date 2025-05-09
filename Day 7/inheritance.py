# class Parent:
#     def yourMethod(self):
#         print('Calling parent method')
# class Child(Parent):
#     def myMethod(self):
#         print('Calling child method')

# c=Child()
# c.yourMethod()

class Employee:
    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
class SalesOfficer(Employee):
    def __init__(self, nm, sal, inc):
        super().__init__(nm, sal)
        self.incentive = inc
    def getSalary(self):
        return self.salary+self.incentive

e1=Employee("Rajesh", 9000)
print("Total Salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 1000, 1000)
print("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))