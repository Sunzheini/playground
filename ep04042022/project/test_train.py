from unittest import TestCase, main
from project.train import Train


# class Train:
#     TRAIN_FULL = "Train is full"
#     PASSENGER_EXISTS = "Passenger {} Exists"
#     PASSENGER_NOT_FOUND = "Passenger Not Found"
#     PASSENGER_ADD = "Added passenger {}"
#     PASSENGER_REMOVED = "Removed {}"
#     ZERO_CAPACITY = 0

class TestTrain(TestCase):
    TRAIN_NAME = 'Train'
    TRAIN_CAPACITY = 2

    #     def __init__(self, name: str, capacity: int):
    #         self.name = name
    #         self.capacity = capacity
    #         self.passengers = []

    def setUp(self) -> None:
        self.train = Train(self.TRAIN_NAME, self.TRAIN_CAPACITY)

    def test_train_init(self):
        self.assertEqual(self.TRAIN_NAME, self.train.name)
        self.assertEqual(self.TRAIN_CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

#     def add(self, passenger_name: str) -> str:
#         if len(self.passengers) == self.capacity:
#             raise ValueError(self.TRAIN_FULL)

#         if passenger_name in self.passengers:
#             raise ValueError(self.PASSENGER_EXISTS.format(passenger_name))
#
#         self.passengers.append(passenger_name)
#         return self.PASSENGER_ADD.format(passenger_name)

    def test_train_add1(self):
        passengers = ['Daniel', 'Maxi']
        self.train.passengers = passengers

        with self.assertRaises(ValueError) as error:
            self.train.add('Adi')
        self.assertEqual("Train is full", str(error.exception))

#     def remove(self, passenger_name: str) -> str:
#         if passenger_name not in self.passengers:
#             raise ValueError(self.PASSENGER_NOT_FOUND.format(passenger_name))
#
#         self.passengers.remove(passenger_name)
#         return self.PASSENGER_REMOVED.format(passenger_name)

if __name__ == '__main__':
    main()