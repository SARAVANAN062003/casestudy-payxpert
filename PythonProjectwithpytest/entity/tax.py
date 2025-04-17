class Tax:
    def __init__(self, tax_id=None, employee_id=None, tax_year=None, taxable_income=0.0, tax_amount=0.0):
        self._tax_id = tax_id
        self._employee_id = employee_id
        self._tax_year = tax_year
        self._taxable_income = taxable_income
        self._tax_amount = tax_amount

    @property
    def tax_id(self):
        return self._tax_id

    @tax_id.setter
    def tax_id(self, value):
        self._tax_id = value

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    @property
    def tax_year(self):
        return self._tax_year

    @tax_year.setter
    def tax_year(self, value):
        self._tax_year = value

    @property
    def taxable_income(self):
        return self._taxable_income

    @taxable_income.setter
    def taxable_income(self, value):
        self._taxable_income = value

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
