from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INITIAL_SIZE = 5
    SIZE_INCREASE = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)

# The SaltwaterFish could only live in SaltwaterAquarium!
