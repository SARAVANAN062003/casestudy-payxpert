# PayXpert/exception/database_connection_exception.py
class DatabaseConnectionException(Exception):
    def __init__(self, message):
        super().__init__(message)