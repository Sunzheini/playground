# -----------------------------------------------------------------------------------
# singleton pattern
# -----------------------------------------------------------------------------------

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True


# -----------------------------------------------------------------------------------
# factory pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod


# Abstract Product
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

# Concrete Products
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def bake(self):
        print("Baking Cheese Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

    def bake(self):
        print("Baking Pepperoni Pizza")

# Abstract Creator
class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()

# Concrete Creators
class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()

# Client code
ny_store = NewYorkPizzaStore()
chicago_store = ChicagoPizzaStore()

ny_store.order_pizza("cheese")
chicago_store.order_pizza("pepperoni")
