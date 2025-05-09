import random

def print_presentations():
    presenters = ['Bikash', 'Sneha', 'Kiran', 'Nabina', 'Suresh', 'Pooja', 'Dipesh', 'Asmita', 'Manoj', 'Ritika']
    random.shuffle(presenters)
    for day, presenter in enumerate(presenters, start=1):
        print(f"{presenter} has presentation on day {day}")

print_presentations()
