'''class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car ()
print(car1.color)
print(car1.brand)'''

class Car:
    def __init__(self, color, brand):
        self.color = color   
        self.brand = brand   

    def show_details(self):
        print("Car:", self.brand, "| Color:", self.color)

car1 = Car("Black", "BMW")
car2 = Car("Blue", "Mercedes")

car1.show_details()   
car2.show_details()   

