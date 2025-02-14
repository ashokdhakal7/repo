# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))

# print star
# def print_star(n):
#     for i in range(1, n + 1):
#         print("*" * i)

# print_star(5)

# star reverse
# def print_star_reverse(n):
#     for i in range(n, 0, -1):
#         print("*" * i)

# print_star_reverse(5)

# print name Ashok starting from a
def print_name(name, starting):
    for i in range(starting, len(name) + 1):
        print(name[i - 1:])

print_name("Ashok", 1)
