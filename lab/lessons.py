# ---------------------------------------------------------------------------
# Dataclass package
# ---------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class SampleClass:
    """
    A sample class to demonstrate the use of dataclasses.
    Automatically generates init, repr, and other methods.
    """
    name: str
    age: int
    is_student: bool

    def greet(self) -> str:
        """Returns a greeting message."""
        return f"Hello, my name is {self.name}."


# ---------------------------------------------------------------------------
# Type annotations
# ---------------------------------------------------------------------------
import mypy
# this is a static type checker


elements: list[int] = [1, 2, 3, 4, 5, 'a']
# run mypy lab\lessons.py to static-check


def get_data() -> list[dict[str, str]]:
    """
    Returns a list of dictionaries with string keys and values.
    """
    return [
        {'name': 'Alice', 'age': '30'},
        {'name': 'Bob', 'age': '25'},
    ]


# ---------------------------------------------------------------------------
# Bad design: Rigidity, Fragility, Immobility
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Design Principles (not Design Patterns)
# ---------------------------------------------------------------------------
# 1. Encapsulate what varies (example with factory pattern)
# When checking the type inside order_pancake, instead of having the logic inside the is
# statement we can use a factory pattern to create the pancake object and return it.

class Pancake:
    def __init__(self):
        self.type = 'plain'

    def cook(self):
        print(f"Cooking a {self.type} pancake")


class BananaPancake(Pancake):
    def __init__(self):
        super().__init__()
        self.type = 'banana'


class ChocolatePancake(Pancake):
    def __init__(self):
        super().__init__()
        self.type = 'chocolate'



def order_pancake(pancake_type: str) -> Pancake:
    if pancake_type == 'banana':
        return BananaPancake()
    elif pancake_type == 'chocolate':
        return ChocolatePancake()
    else:
        raise ValueError("Unknown pancake type")


# 2. Favor composition over inheritance (Has-A is better than Is-A)
# Instead of: coffee with butter is a coffee, we can say a coffee has a condiment

class Butter:
    def __init__(self):
        self.type = 'butter'

    def cost(self):
        return 0.5

    def prepare(self):
        print(f"Preparing {self.type}")


class Coffee:
    def __init__(self):
        self.type = 'coffee'
        self.condiments = []

    def add_condiment(self, condiment):
        self.condiments.append(condiment)
        condiment.prepare()

    def cost(self):
        total_cost = 1.0
        for condiment in self.condiments:
            total_cost += condiment.cost()
        return total_cost


# 3. Strive for loosely coupled designs between objects that interact
# The WeatherApp class knows only about the Screen interface, but not about the
# concrete implementation
from abc import ABC, abstractmethod


class Screen(ABC):
    @abstractmethod
    def display(self, content):
        pass


class LcdScreen(Screen):
    def display(self, content):
        self.display_on_lcd(content)

    @staticmethod
    def display_on_lcd(content):
        print(f"Displaying on LCD: {content}")


class WeatherApp:
    def __init__(self, screen: Screen):
        self.screen = screen

    def show_weather(self, weather_data):
        self.screen.display(weather_data)


# 4. Program to an interface, not an implementation
# WebSystem class is dependent on the AbstractDatabase interface, not on a concrete implementation
class AbstractDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str):
        pass


class MySQLDatabase(AbstractDatabase):
    def connect(self):
        print("Connecting to MySQL database")

    def disconnect(self):
        print("Disconnecting from MySQL database")

    def execute_query(self, query: str):
        print(f"Executing query on MySQL database: {query}")


class WebSystem:
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def run_query(self, query: str):
        self.db.connect()
        self.db.execute_query(query)
        self.db.disconnect()


# ---------------------------------------------------------------------------
# SOLID Principles
# ---------------------------------------------------------------------------
# S - Single Responsibility Principle (SRP)
# O - Open/Closed Principle (OCP)
# L - Liskov Substitution Principle (LSP)
# I - Interface Segregation Principle (ISP)
# D - Dependency Inversion Principle (DIP)


# Interface Segregation Principle (ISP)






































