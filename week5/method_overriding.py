class Bird:
    def sound(self):
        print("Some generic bird sound")

class Sparrow(Bird):  # child
    def sound(self):
        print("Chirp Chirp")

class Crow(Bird):  # child
    def sound(self):
        print("Caw Caw")

# Polymorphism in action
for bird in [Sparrow(), Crow(), Bird()]:
    bird.sound()
