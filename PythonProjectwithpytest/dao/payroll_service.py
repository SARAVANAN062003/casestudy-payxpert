from dao.i_payroll_service import IPayrollService
from entity.payroll import Payroll
from util.db_conn_util import GetDBConnection
from exception.payroll_generation_exception import PayrollGenerationException
from exception.employee_not_found_exception import EmployeeNotFoundException


class PayrollService(IPayrollService):

    def generate_payroll(self, payroll_id, employee_id, start_date, end_date, basic_salary, overtime, deductions):
        try:
            # Check if the employee exists
            if not self._employee_exists(employee_id):
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")

            # Calculate net salary
            net_salary = basic_salary + overtime - deductions

            # Insert payroll record into database
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Payroll (
                        PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, 
                        BasicSalary, OvertimePay, Deductions, NetSalary
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    payroll_id, employee_id, start_date, end_date,
                    basic_salary, overtime, deductions, net_salary
                ))
                conn.commit()
        except EmployeeNotFoundException as enf:
            raise PayrollGenerationException(f"Payroll generation failed: {enf}")
        except Exception as e:
            raise PayrollGenerationException(f"Failed to generate payroll: {e}")

    def _employee_exists(self, employee_id):
        # Simulate a check to verify if the employee exists in the database.
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Employees WHERE EmployeeID = ?", (employee_id,))
            return cursor.fetchone() is not None

    def get_payroll_by_id(self, payroll_id):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE PayrollID = ?", (payroll_id,))
            row = cursor.fetchone()
            return Payroll(*row) if row else None

    def get_payrolls_for_employee(self, employee_id):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
            rows = cursor.fetchall()
            return [Payroll(*row) for row in rows]

    def get_payrolls_for_period(self, start_date, end_date):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Payroll 
                WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?
            """, (start_date, end_date))
            rows = cursor.fetchall()
            return [Payroll(*row) for row in rows]
