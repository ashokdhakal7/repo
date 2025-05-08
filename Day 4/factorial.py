def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    result = factorial(num)
    print(f"Factorial of {num} is {result}")

if __name__ == "__main__":
    main()
