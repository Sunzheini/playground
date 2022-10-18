class Validator:
    @staticmethod
    def check_if_string_is_empty(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def check_if_number_is_equal_or_below_zero(number: int, message: str):
        if number <= 0:
            raise ValueError(message)

