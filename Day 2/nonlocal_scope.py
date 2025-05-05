# nonlocal_scope.py

def yourfunction():
    a = 5
    b = 6
    # nested function
    def myfunction():
        # nonlocal function
        nonlocal a
        nonlocal b
        a = 10
        b = 20
        print("variable a:", a)
        print("variable b:", b)
        return a + b
    print(myfunction())

if __name__ == "__main__":
    yourfunction()
