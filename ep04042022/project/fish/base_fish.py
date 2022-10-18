from abc import ABC, abstractmethod
from project.validator import Validator


class BaseFish(ABC):
    SIZE_INCREASE = 5

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Fish name cannot be an empty string."
        Validator.check_if_string_is_empty(value, message)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        message = "Fish species cannot be an empty string."
        Validator.check_if_string_is_empty(value, message)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        message = "Price cannot be equal to or below zero."
        Validator.check_if_number_is_equal_or_below_zero(value, message)
        self.__price = value

    def eat(self):
        self.size += self.SIZE_INCREASE
