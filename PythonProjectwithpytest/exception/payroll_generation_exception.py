# PayXpert/exception/payroll_generation_exception.py
class PayrollGenerationException(Exception):
    def __init__(self, message):
        super().__init__(message)