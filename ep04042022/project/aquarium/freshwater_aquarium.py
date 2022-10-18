from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    @property
    def fish_type(self):
        return 'FreshwaterFish'

