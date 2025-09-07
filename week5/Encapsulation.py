class Student:
    def __init__(self, name, age):
        self.name = name      # public
        self.age = age        # public

s1 = Student("Noor", 20)
print(s1.name)   # Accessible
print(s1.age)    # Accessible
