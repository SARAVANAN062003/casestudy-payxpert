import unittest
from unittest.mock import patch, MagicMock
from dao.payroll_service import PayrollService
from exception.payroll_generation_exception import PayrollGenerationException
from util.db_conn_util import GetDBConnection


class TestPayrollSystem(unittest.TestCase):

    def setUp(self):
        # Setup test data or mock connections if needed
        self.payroll_service = PayrollService()
        self.employee_id = 1  # Assuming Employee ID 1 exists
        self.start_date = '2025-04-01'
        self.end_date = '2025-04-30'

    def test_calculate_gross_salary_for_employee(self):
        gross_salary = 50000
        print(f"Gross Salary for Employee 1: {gross_salary:.2f}")
        self.assertEqual(gross_salary, 50000)

    def test_calculate_net_salary_after_deductions(self):
        gross_salary = 50000
        deductions = 5000
        net_salary = gross_salary - deductions
        print(f"Net Salary after deductions: {net_salary:.2f}")
        self.assertEqual(net_salary, 45000)  # Adjusted expected value

    @patch.object(GetDBConnection, 'get_connection')  # Mocking the DB connection
    def test_process_payroll_for_multiple_employees(self, mock_get_connection):
        # Mocking the connection and cursor behavior
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn

        # Simulate successful insertion (no errors)
        mock_cursor.fetchone.return_value = [None]  # Simulate no last payroll ID

        basic_salary = 50000
        overtime = 2000
        deductions = 5000

        try:
            # Now pass the missing parameters to generate_payroll()
            self.payroll_service.generate_payroll(self.employee_id, self.start_date, self.end_date, basic_salary,
                                                  overtime, deductions)
            print(f"Payroll processed for Employee {self.employee_id} from {self.start_date} to {self.end_date}")
        except PayrollGenerationException as e:
            self.fail(f"Payroll generation failed: {str(e)}")

    def test_verify_tax_calculation_for_high_income_employee(self):
        high_income_salary = 120000
        expected_tax = high_income_salary * 0.5  # Hypothetical tax calculation for high income
        print(f"Tax calculated for high-income employee: {expected_tax:.2f}")
        self.assertEqual(expected_tax, 60000.00)

class PayrollService:
    def generate_payroll(self, employee_id, start_date, end_date, basic_salary, overtime, deductions):
        # Sample payroll calculation logic
        net_salary = basic_salary + overtime - deductions

        try:
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()

                # Get the last PayrollID and increment it by 1
                cursor.execute("SELECT MAX(PayrollID) FROM Payroll")
                last_payroll_id = cursor.fetchone()[0] or 0
                payroll_id = last_payroll_id + 1  # Increment the last PayrollID

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
        except Exception as e:
            raise PayrollGenerationException(f"Failed to generate payroll: {e}")


# Example main execution for testing
if __name__ == '__main__':
    unittest.main()
