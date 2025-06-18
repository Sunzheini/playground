import unittest


class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("First name must be a string")
        self.__first_name = value

    def get_full_name(self):
        return f'{self.__first_name} {self.last_name}'

    def get_info(self):
        return f'{self.__first_name} {self.last_name} is {self.age} years old'



class TestPerson(unittest.TestCase):
    def setUp(self):
        """
        Set up a Person instance for testing. Executed before each test method.
        :return: None
        """
        # Arrange
        self.person = Person('John', 'Doe', 30)

    def test_get_full_name(self):
        # Arrange
        expected_result = 'John Doe'

        # Act
        result = self.person.get_full_name()

        # Assert
        self.assertEqual(result, expected_result)

    def test_set_first_name(self):
        # Act
        self.person.first_name = 'Jane'

        # Assert
        self.assertEqual(self.person.first_name, 'Jane')

    def test_set_first_name_invalid_type(self):
        # Act & Assert
        with self.assertRaises(TypeError):
            self.person.first_name = 123

    def tearDown(self):
        """
        Clean up after each test method. Executed after each test method.
        :return: None
        """
        self.person = None


if __name__ == '__main__':
    unittest.main()
