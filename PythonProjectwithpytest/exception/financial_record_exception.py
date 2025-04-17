# PayXpert/exception/financial_record_exception.py
class FinancialRecordException(Exception):
    def __init__(self, message):
        super().__init__(message)