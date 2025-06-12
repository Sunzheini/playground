# UML: Unified Modeling Language
# UML is a way of visualizing a software program using a collection of diagrams

# Class Diagrams
"""
+ Public attribute or method
- Private attribute or method

Relationships:
    - Association: A class can be associated with another class
    - Inheritance (Generalization): A class inherits attributes and methods from
        another class. Arrow points to the superclass. If the superclass is abstract,
        the name is italicized
    - Realization: Relationship between an interface and classes that implement it
    - Dependency: When an object of one class uses an object of another class and
        the used object is passed as an argument to the using object. The arrow
        points to the class that is used

    - Aggregation: A class can be composed of other classes as attributes, but the
        composed classes can exist independently of the class
    - Composition: A class can be composed of other classes as attributes, but the
        composed classes cannot exist independently of the class
"""