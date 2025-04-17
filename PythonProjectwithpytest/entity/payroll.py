class Payroll:
    def __init__(self, payroll_id, employee_id, pay_period_start, pay_period_end,
                 basic_salary, overtime_pay, deductions, net_salary):
        self._payroll_id = payroll_id
        self._employee_id = employee_id
        self._pay_period_start = pay_period_start
        self._pay_period_end = pay_period_end
        self._basic_salary = basic_salary
        self._overtime_pay = overtime_pay
        self._deductions = deductions
        self._net_salary = net_salary

    @property
    def payroll_id(self):
        return self._payroll_id

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def pay_period_start(self):
        return self._pay_period_start

    @property
    def pay_period_end(self):
        return self._pay_period_end

    @property
    def basic_salary(self):
        return self._basic_salary

    @property
    def overtime_pay(self):
        return self._overtime_pay

    @property
    def deductions(self):
        return self._deductions

    @property
    def net_salary(self):
        return self._net_salary

    def __str__(self):
        return (f"Payroll ID: {self._payroll_id}, Employee ID: {self._employee_id}, "
                f"Pay Period: {self._pay_period_start} to {self._pay_period_end}, "
                f"Basic Salary: {self._basic_salary}, Overtime Pay: {self._overtime_pay}, "
                f"Deductions: {self._deductions}, Net Salary: {self._net_salary}")
