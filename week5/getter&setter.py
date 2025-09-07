class Student:
    def __init__(self, name, age):
        self.__age = age   # private

    def get_age(self):   # getter
        return self.__age

    def set_age(self, age):  # setter
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

s1 = Student("Noor", 20)
print(s1.get_age())   # 20
s1.set_age(21)
print(s1.get_age())   # 21
