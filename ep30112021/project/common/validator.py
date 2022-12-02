class Validator:

    @staticmethod
    def validate_string(value):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
