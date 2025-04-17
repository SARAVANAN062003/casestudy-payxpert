from abc import ABC, abstractmethod
from typing import List
from entity.payroll import Payroll
from datetime import date

class IPayrollService(ABC):

    @abstractmethod
    def generate_payroll(self, employee_id: int, start_date: date, end_date: date) -> Payroll:
        pass

    @abstractmethod
    def get_payroll_by_id(self, payroll_id: int) -> Payroll:
        pass

    @abstractmethod
    def get_payrolls_for_employee(self, employee_id: int) -> List[Payroll]:
        pass

    @abstractmethod
    def get_payrolls_for_period(self, start_date: date, end_date: date) -> List[Payroll]:
        pass
