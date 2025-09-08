class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department= department
    def data (self):
        print(self.name,self.salary,self.department)
obj1=Manager("noor",1000000,"cse")
obj1.data()


