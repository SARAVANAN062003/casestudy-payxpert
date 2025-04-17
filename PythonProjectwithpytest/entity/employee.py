from datetime import date

class Employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, date_of_birth=None,
                 gender=None, email=None, phone_number=None, address=None,
                 position=None, joining_date=None, termination_date=None):
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._email = email
        self._phone_number = phone_number
        self._address = address
        self._position = position
        self._joining_date = joining_date
        self._termination_date = termination_date

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def joining_date(self):
        return self._joining_date

    @joining_date.setter
    def joining_date(self, value):
        self._joining_date = value

    @property
    def termination_date(self):
        return self._termination_date

    @termination_date.setter
    def termination_date(self, value):
        self._termination_date = value

    def calculate_age(self):
        today = date.today()
        return today.year - self._date_of_birth.year - (
            (today.month, today.day) < (self._date_of_birth.month, self._date_of_birth.day)
        )
