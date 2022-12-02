from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_string(value)
        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
