import pyodbc
from exception.database_connection_exception import DatabaseConnectionException

class GetDBConnection:
    _connection = None

    @staticmethod
    def get_connection():
        if GetDBConnection._connection is None:
            try:
                GetDBConnection._connection = pyodbc.connect(
                    'DRIVER={SQL Server};'
                    'SERVER=DESKTOP-HCRUI4E;'
                    'DATABASE=payxpert;'
                    'Trusted_Connection=yes;'
                )
            except Exception as e:
                raise DatabaseConnectionException(f"Database connection failed: {e}")
        return GetDBConnection._connection
