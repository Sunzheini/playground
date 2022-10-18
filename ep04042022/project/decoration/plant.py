from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    COMFORT = 5
    PRICE = 10

    def __init__(self):
        super(Plant, self).__init__(comfort=self.COMFORT, price=self.PRICE)

