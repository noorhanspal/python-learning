import math

class Shape:
    def area(self):
        print("Area is not defined")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle is", self.length * self.breadth)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle is", 3.14 * self.radius * self.radius)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square is", self.side * self.side)

# Polymorphism in action
for shape in [Rectangle(4, 4), Circle(4), Square(2)]:
    shape.area()

