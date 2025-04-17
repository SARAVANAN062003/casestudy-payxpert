from abc import ABC, abstractmethod
from typing import List
from entity.financial_record import FinancialRecord
from datetime import date

class IFinancialRecordService(ABC):

    @abstractmethod
    def add_financial_record(self, record: FinancialRecord) -> None:
        pass

    @abstractmethod
    def get_financial_record_by_id(self, record_id: int) -> FinancialRecord:
        pass

    @abstractmethod
    def get_financial_records_for_employee(self, employee_id: int) -> List[FinancialRecord]:
        pass

    @abstractmethod
    def get_financial_records_for_date(self, record_date: date) -> List[FinancialRecord]:
        pass
