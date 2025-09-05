# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):   # method override
        print(self.name, "barks.")

class Cat(Animal):
    def speak(self):
        print(self.name, "meows.")

# Objects
d = Dog("Tommy")
c = Cat("Kitty")

d.speak()
c.speak()
