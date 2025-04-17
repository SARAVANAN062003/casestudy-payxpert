# PayXpert/exception/tax_calculation_exception.py
class TaxCalculationException(Exception):
    def __init__(self, message):
        super().__init__(message)