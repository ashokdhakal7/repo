# local_scope.py

def myfunction():
    a = 10
    b = 10
    print("variable a:", a)
    print("variable b:", b)
    return a + b

if __name__ == "__main__":
    print(myfunction())
