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


class Vehicle:
    def __init__(self, name):
        self.name = name
        print(f"Vehicle init: {name}")


class Car(Vehicle):
    def __init__(self, name, wheels):
        super().__init__(name)  # Uses MRO to find next __init__
        self.wheels = wheels
        print(f"Car init: {wheels} wheels")


class Boat(Vehicle):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
        print(f"Boat init: {type}")


class AmphibiousVehicle(Car, Boat):
    def __init__(self, name, wheels, type):
        super().__init__(name, wheels)  # Wait, what about type?
        # super() follows MRO!


av = AmphibiousVehicle("Duck", 4, "sailing")
# Output shows the MRO in action















