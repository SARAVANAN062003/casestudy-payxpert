# PayXpert/exception/invalid_input_exception.py
class InvalidInputException(Exception):
    def __init__(self, message):
        super().__init__(message)