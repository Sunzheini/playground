from project import aquarium_factory
from project.aquarium_factory import AquariumFactory
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.aquarium_factory = AquariumFactory()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        try:
            new_aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."
        except ValueError as error:
            return str(error)

    def add_decoration(self, decoration_type: str):
        if decoration_type == 'Ornament':
            new_decoration = Ornament()
        elif decoration_type == 'Plant':
            new_decoration = Plant()
        else:
            return "Invalid decoration type."
        self.decorations_repository.add_decoration(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        searched_decoration = self.decorations_repository.find_by_type(decoration_type)
        searched_aquarium = self.find_aquarium_object_by_name(aquarium_name)
        if searched_decoration is not None and searched_aquarium is not None:
            searched_aquarium.decorations.append(searched_decoration)
            self.decorations_repository.remove(searched_decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == 'FreshwaterFish':
            new_fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == 'SaltwaterFish':
            new_fish = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."
        searched_aquarium = self.find_aquarium_object_by_name(aquarium_name)
        return searched_aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        searched_aquarium = self.find_aquarium_object_by_name(aquarium_name)
        searched_aquarium.feed()
        return f"Fish fed: {len(searched_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        total_value = 0
        searched_aquarium = self.find_aquarium_object_by_name(aquarium_name)
        for fish in searched_aquarium.fish:
            total_value += fish.price
        for decoration in searched_aquarium.decorations:
            total_value += decoration.price
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'
        return result.strip()

    def find_aquarium_object_by_name(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium
        return None
