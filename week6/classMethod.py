class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def total_people(cls):
        return cls.count

p1 = Person("Noor")
p2 = Person("Alex")

print(Person.total_people()) 
