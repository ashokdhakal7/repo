# to create a set and to take user input to check if it exists in the set and also give the position with it.
a = {1, 2, 3, 4, 5}

user_input = input("Enter a number to check if it exists in the set: ")

try:
    user_input_int = int(user_input)
    found = False
    for element in a:
        if element == user_input_int:
            found = True
            break
    if found:
        print(f"{user_input_int} exists in the set.")
        print("item #{} = {}".format(a, user_input))
    else:
        print("Don't exist")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
