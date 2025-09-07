class Student:
    def __init__(self, name, age):
        self._age = age   # protected

s1 = Student("Noor", 20)
print(s1._age)   # Accessible, but not recommended

