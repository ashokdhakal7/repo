# take user input and check if its length is greater than 3, if not discard it and print the rest.

def main():
    user_input = input("Enter a string: ")
    if len(user_input) > 3:
        print(user_input)
    else:
        print("Input discarded because length is 3 or less.")

if __name__ == "__main__":
    main()
