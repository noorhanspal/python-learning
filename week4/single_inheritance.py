class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name, "is making a sound")

class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print(self.name, "is barking")

# Object
d = Dog("Tommy")
d.speak()
d.bark()
