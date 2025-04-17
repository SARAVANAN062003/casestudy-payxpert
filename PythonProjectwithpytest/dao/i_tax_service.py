from abc import ABC, abstractmethod
from typing import List
from entity.tax import Tax

class ITaxService(ABC):

    @abstractmethod
    def calculate_tax(self, employee_id: int, tax_year: int) -> Tax:
        pass

    @abstractmethod
    def get_tax_by_id(self, tax_id: int) -> Tax:
        pass

    @abstractmethod
    def get_taxes_for_employee(self, employee_id: int) -> List[Tax]:
        pass

    @abstractmethod
    def get_taxes_for_year(self, tax_year: int) -> List[Tax]:
        pass
