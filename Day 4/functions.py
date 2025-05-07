# print(0.1+0.2 ==0.3)

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(-5))

# square = lambda x: x+x
# print(square(2))

# def greet(name):
#     return f"hello, {name}!"
# print(greet("John"))

# n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
# print (n(5))
# print (n(-3))
# print (n(0))

# calc = lambda x, y: (x+y, x*y)
# res = calc(3,4)
# print(res)

# n = [1,2,3,4,5,6]
# even = filter(lambda x: x% 2 == 0, n)
# print(list(even))

# a = [1,2,3,4]
# b = map(lambda x: x*2, a)
# print(list(b))

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
describe_person(name="John", age=30)

