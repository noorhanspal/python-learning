class Mother:
    def cooking(self):
        print("I can cook food")

class Father:
    def driving(self):
        print("I can drive a car")

class Child(Mother, Father):   # Child inherits from both
    def study(self):
        print("I can study")

c = Child()
c.cooking()
c.driving()
c.study()
