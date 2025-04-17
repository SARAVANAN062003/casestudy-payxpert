from dao.i_employee_service import IEmployeeService
from entity.employee import Employee
from util.db_conn_util import GetDBConnection
from exception.employee_not_found_exception import EmployeeNotFoundException

class EmployeeService(IEmployeeService):

    def get_employee_by_id(self, employee_id):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?", (employee_id,))
            row = cursor.fetchone()
            if row:
                return Employee(*row)
            else:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")

    def get_all_employees(self):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employee")
            rows = cursor.fetchall()
            return [Employee(*row) for row in rows]

    def add_employee(self, employee):
        # Get the next available EmployeeID
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(EmployeeID) FROM Employee")
            max_employee_id = cursor.fetchone()[0]
            new_employee_id = 1 if max_employee_id is None else max_employee_id + 1  # Increment or start from 1 if no records exist

            # Insert the new employee with the generated EmployeeID
            cursor.execute("""
                INSERT INTO Employee (EmployeeID, FirstName, LastName, DateOfBirth, Gender, 
                                      Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                new_employee_id,
                employee.first_name,
                employee.last_name,
                employee.date_of_birth,
                employee.gender,
                employee.email,
                employee.phone_number,
                employee.address,
                employee.position,
                employee.joining_date,
                employee.termination_date  # Can safely be None
            ))
            conn.commit()

    def update_employee(self, employee):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Employee
                SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, 
                    PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
                WHERE EmployeeID = ?
            """, (
                employee.first_name,
                employee.last_name,
                employee.date_of_birth,
                employee.gender,
                employee.email,
                employee.phone_number,
                employee.address,
                employee.position,
                employee.joining_date,
                employee.termination_date,
                employee.employee_id
            ))
            conn.commit()

    def remove_employee(self, employee_id):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,))
            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
            conn.commit()
            print(f"Employee {employee_id} deleted successfully.")
