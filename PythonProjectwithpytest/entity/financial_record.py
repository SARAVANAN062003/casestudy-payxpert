class FinancialRecord:
    def __init__(self, record_id, employee_id, record_date, description, amount, record_type,
                 pay_period_start_date=None, pay_period_end_date=None):
        self._record_id = record_id
        self._employee_id = employee_id
        self._record_date = record_date
        self._description = description
        self._amount = amount
        self._record_type = record_type
        self._pay_period_start_date = pay_period_start_date
        self._pay_period_end_date = pay_period_end_date

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value

    @property
    def pay_period_start_date(self):
        return self._pay_period_start_date

    @pay_period_start_date.setter
    def pay_period_start_date(self, value):
        self._pay_period_start_date = value

    @property
    def pay_period_end_date(self):
        return self._pay_period_end_date

    @pay_period_end_date.setter
    def pay_period_end_date(self, value):
        self._pay_period_end_date = value
