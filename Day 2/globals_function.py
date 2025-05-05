# globals_function.py

marks = 50
marks2 = 60

def myfunction():
    "change values of global variables"
    globals()["marks"] = globals()["marks"] + 10
    global marks2
    marks2 = marks2 + 20

if __name__ == "__main__":
    myfunction()
    print("marks:", marks, "marks2:", marks2)
