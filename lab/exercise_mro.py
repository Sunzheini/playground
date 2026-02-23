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


"""
Python uses the C3 linearization algorithm:
1. Children come before parents
2. Subclasses come before superclasses
3. The order of base classes is preserved
"""
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass


print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


# --------------------------------------------------------------------------------------
# Multiple Inheritance and MRO
# --------------------------------------------------------------------------------------
class Vehicle:
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels


class Boat(Vehicle):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type


# Composition instead of multiple inheritance
class AmphibiousVehicle:
    def __init__(self, name, wheels, type):
        self.car = Car(name, wheels)
        self.boat = Boat(name, type)

    @property
    def name(self):
        return self.car.name  # or self.boat.name

    @property
    def wheels(self):
        return self.car.wheels

    @property
    def type(self):
        return self.boat.type


# --------------------------------------------------------------------------------------
# super() with Different Signatures
# --------------------------------------------------------------------------------------
class A:
    def show(self):
        print("A", end=" ")


class B(A):
    def show(self):
        print("B", end=" ")
        super().show()


class C(A):
    def show(self):
        print("C", end=" ")
        super().show()


class D(B, C):
    def show(self):
        print("D", end=" ")
        super().show()


d = D()
d.show()  # D B C A
print()  # Newline
print(D.__mro__)  # (D, B, C, A, object)


# --------------------------------------------------------------------------------------
# MRO and Multiple Inheritance Conflicts
# --------------------------------------------------------------------------------------
class X:
    def method(self):
        print("X")

class Y:
    def method(self):
        print("Y")

class Z(X, Y):
    pass

class W(Y, X):
    pass

z = Z()
z.method()  # "X" - order matters!

w = W()
w.method()  # "Y" - order matters!

print(Z.__mro__)  # (Z, X, Y, object)
print(W.__mro__)  # (W, Y, X, object)


# ----------------------------------------------------------------------------------------
# The "Diamond" Problem with Different Methods
# ----------------------------------------------------------------------------------------
class Grandparent:
    def method(self):
        print("Grandparent")


class Parent1(Grandparent):
    def method(self):
        print("Parent1")
        super().method()


class Parent2(Grandparent):
    def method(self):
        print("Parent2")
        super().method()


class Child(Parent1, Parent2):
    def method(self):
        print("Child")
        super().method()


c = Child()
c.method()
# Output:
# Child
# Parent1
# Parent2
# Grandparent
