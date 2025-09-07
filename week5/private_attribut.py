class Student:
    def __init__(self, name, age):
        self.__age = age   # private

s1 = Student("Noor", 20)
# print(s1.__age)  # ❌ Error: not accessible
print(s1._Student__age)   # ✅ Access via name mangling (not recommended)
