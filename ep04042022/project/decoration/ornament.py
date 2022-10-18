from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    COMFORT = 1
    PRICE = 5

    def __init__(self):
        super().__init__(comfort=self.COMFORT, price=self.PRICE)














