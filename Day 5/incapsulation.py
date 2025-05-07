# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance # private attribute

#     def deposite(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount(100)
# account.deposite(50)
# print(account.get_balance())

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
stud = Student("Jessa", 14)
print('Name:', stud.name, stud.get_age())
stud.set_age(16)
print('Name:', stud.name, stud.get_age())