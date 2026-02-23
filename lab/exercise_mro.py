"""
MRO is the order in which Python searches for methods in a class hierarchy. When you call a method
on an object, Python follows this order to find which method to execute.
"""

class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")


class C(A):
    def method(self):
        print("C")


class D(B, C):
    pass


d = D()
d.method()  # B gets printed, because B is listed before C in the class definition of D.