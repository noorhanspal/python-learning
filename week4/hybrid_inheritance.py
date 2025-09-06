class A:
    def feature1(self):
        print("Feature 1 from A")

class B(A):
    def feature2(self):
        print("Feature 2 from B")

class C(A):
    def feature3(self):
        print("Feature 3 from C")

class D(B, C):   # Hybrid: B & C both inherit A, and D inherits B & C
    def feature4(self):
        print("Feature 4 from D")

obj = D()
obj.feature1()
obj.feature2()
obj.feature3()
obj.feature4()
