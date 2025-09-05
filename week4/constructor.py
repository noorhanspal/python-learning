class Student:   
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def intro(self):   # method
        print("My name is", self.name, "and I am", self.age, "years old.")

# objects bana rahe hain
s1 = Student("Noor", 20)
s2 = Student("Bullet", 20)
s3 = Student("Simran", 21)

# method call kar rahe hain
s1.intro()
s2.intro()
s3.intro()
