from abc import ABC, abstractmethod
from typing import List
from entity.employee import Employee

class IEmployeeService(ABC):

    @abstractmethod
    def get_employee_by_id(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Employee]:
        pass

    @abstractmethod
    def add_employee(self, employee: Employee) -> None:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> None:
        pass

    @abstractmethod
    def remove_employee(self, employee_id: int) -> None:
        pass
