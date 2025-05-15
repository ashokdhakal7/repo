#to find fibonacci series using the recursion method

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
fib_series = [fibonacci(i) for i in range(6)]
print(fib_series)