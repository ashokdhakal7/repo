# local scope
# def myfunction ():
#     a=10
#     b=10
#     print("variable a:",a)
#     print("variable b:",b)
#     return a+b

# print(myfunction())
    
# print(a+b)

# # global scope

# name = "Alice"
# marks = 50
# def myfunction ():
#     print("name:", name)
#     print("marks:", marks)
# myfunction()

# def yourfunction():
#     a = 5
#     b = 6
#     #nested function
#     def myfunction():
#         # non local function
#         nonlocal a
#         nonlocal b
#         a = 10
#         b = 20
#         print("variable a:", a)
#         print("variable b:", b)
#         return a+b
#     print(myfunction())
# yourfunction()

# name = "Alice"
# marks = 50
# result = True

# def myfunction ():
#     a=10
#     b=20
#     print (locals())
#     return a+b
# print (globals())

# marks = 50
# def myfunction ():
#     marks = 70
#     print (marks)
# myfunction()
# print (marks)

# marks = 50
# def myfunction():
#     marks=marks+20
#     print(marks)
# myfunction()
# print(marks)

# var1 = 50
# var2 = 60
# def myfunction():
#     "change values of global variables"
#     globals()["var1"] = globals()["var1"]+10
#     global var2
#     var2 = var2+20

# myfunction()
# print("var1:",var1, "var2:",var2)

marks = 50
marks2 = 60
def myfunction():
    "change values of global variables"
    globals()["marks"] = globals()["marks"]+10
    global marks2
    marks2 = marks2+20
myfunction()
print("marks:",marks, "marks2:",marks2)