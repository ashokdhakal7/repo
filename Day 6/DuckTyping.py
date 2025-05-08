#Duck Typing
class Duck:
    def sound(self):
        return "Quack quack"
class AnotherBird:
    def sound(self):
        return "I'm similar to a duck!"
def makeSound(duck):
    print(duck.sound())

# creating instance
duck = Duck()
AnotherBird = AnotherBird()

#calling method
makeSound(duck)
makeSound(AnotherBird)