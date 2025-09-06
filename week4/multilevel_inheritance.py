class Grandfather:
    def property(self):
        print("I have land")

class Father(Grandfather):  # Father inherits Grandfather
    def car(self):
        print("I have a car")

class Son(Father):  # Son inherits Father (and also Grandfather indirectly)
    def bike(self):
        print("I have a bike")

s = Son()
s.property()
s.car()
s.bike()
