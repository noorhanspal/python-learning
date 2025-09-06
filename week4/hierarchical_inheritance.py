class Parent:
    def home(self):
        print("I have a home")

class Son(Parent):
    def laptop(self):
        print("I have a laptop")

class Daughter(Parent):
    def phone(self):
        print("I have a phone")

s = Son()
d = Daughter()

s.home()
s.laptop()

d.home()
d.phone()
