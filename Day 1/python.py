age = 21
height = 5.9
name = "Alice"
is_student = True
if age > 18:
    print("Adult")
elif age == 18:
    print("You just became an adult")
else:
    print("Minor")
for i in range(5):
    print(f"Number: {i}")

    count = 0
    while count < 3:
        print(count)
        count += 1
def greet(name):
    return f"Hello, {name}!"

print(greet(name))