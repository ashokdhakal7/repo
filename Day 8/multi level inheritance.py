# class Animal:
#     def __init__(self, species):
#         self.species = species
#     def eat(self):
#         return f"{self.species} is eating"

# class Mammal(Animal):
#     def __init__(self, species, fur_color):
#         super().__init__(species)
#         self.fur_color = fur_color
#     def breathe (self):
#         return f"{self.species} breathes air"
    
# class Dog(Mammal):
#     def __init__(self, species, fur_color, name):
#         super().__init__(species, fur_color)
#         self.name = name
#     def bark(self):
#         return f"{self.name} says woof !"
    
# my_dog = Dog("Dog", "brown", "Buddy")

# print(my_dog.eat())
# print(my_dog.breathe())
# print(my_dog.bark())


#fffffffffffffffff

class Animal:
    def __init__(self, species):
        self.species = species
    def eat(self):
        return f"{self.species} is eating"

class Mammal(Animal):
    def __init__(self, species, fur_color):
        super().__init__(species)
        self.fur_color = fur_color
    def breathe (self):
        return f"{self.species} breathes air"
    
class Dog(Mammal):
    def __init__(self, species, fur_color, name):
        super().__init__(species, fur_color)
        self.name = name
    def bark(self):
        return f"{self.name} says woof !"

class Cat(Mammal):
    def __init__(self, species, fur_color, name):
        super().__init__(species, fur_color)
        self.name = name
    def meow(self):
        return f"{self.name} says meow !"
    
my_dog = Dog("Dog", "brown", "Buddy")
my_cat = Cat("Cat", "White", "Small")
    
print(my_dog.bark())
print(my_cat.meow())