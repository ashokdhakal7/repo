# def greet_user(name):
#     message = "Hello " + name + "!"
#     return message

# user_name = "Ram Krishna"
# greeting = greet_user(user_name)

# print(greeting)

#Basic Data Types
age=21                      #int
height=5.9                  #float
name="Ram Krishna"          #string
is_student=True             #boolean

#control ctructures
#conditionals
if age>18:
    print("You are an adult")
elif age==18:
    print("You are an adult")
else:
    print("You are not an adult")

#loops
for i in range(5):
    print(f"Number: {i}")

#while loop
count =0
while count<3:
    print("Counting:", count)
    count+=1

#functions
def greet(name):
    return f"Hello {name}!"

#function call
print(greet("Ram Krishna"))