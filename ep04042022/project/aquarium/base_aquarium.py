from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish
from project.validator import Validator


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Aquarium name cannot be an empty string."
        Validator.check_if_string_is_empty(value, message)
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def calculate_comfort(self):
        total_comfort = 0
        for decoration in self.decorations:
            total_comfort += decoration.comfort
        return total_comfort

    def add_fish(self, fish: BaseFish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        if self.fish_type != fish.__class__.__name__:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} " \
               f"to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"

        result += 'Fish: '
        if not self.fish:
            result += 'none\n'
        else:
            for fish in self.fish:
                result += f"{fish.name} "
                result.strip()
                result += '\n'

        result += f'Decorations: {len(self.decorations)}\n'

        result += f'Comfort: {self.calculate_comfort()}'

        return result






