import unittest
from exception.payroll_generation_exception import PayrollGenerationException
from exception.database_connection_exception import DatabaseConnectionException
from util.db_conn_util import GetDBConnection  # Your provided MSSQL connection class

# PayrollService that interacts with MSSQL
class PayrollService:
    def generate_payroll(self, employee_id, start_date, end_date, basic_salary, overtime, deductions):
        net_salary = basic_salary + overtime - deductions

        try:
            conn = GetDBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT MAX(PayrollID) FROM Payroll")
            last_payroll_id = cursor.fetchone()[0] or 0
            payroll_id = last_payroll_id + 1

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

# Unit test using actual MSSQL DB
class TestPayrollSystem(unittest.TestCase):

    def setUp(self):
        self.payroll_service = PayrollService()
        self.employee_id = 1  # Ensure this exists in the Employee table
        self.start_date = '2025-04-01'
        self.end_date = '2025-04-30'

    def test_process_payroll_for_multiple_employees(self):
        basic_salary = 50000
        overtime = 2000
        deductions = 5000

        try:
            self.payroll_service.generate_payroll(
                self.employee_id, self.start_date, self.end_date,
                basic_salary, overtime, deductions
            )
            print(f"✅ Payroll processed for Employee {self.employee_id} from {self.start_date} to {self.end_date}")
        except PayrollGenerationException as e:
            self.fail(f"❌ Payroll generation failed: {str(e)}")
        except DatabaseConnectionException as e:
            self.fail(f"❌ Database connection failed: {str(e)}")

    def test_calculate_net_salary_after_deductions_db(self):
        basic_salary = 60000
        overtime = 3000
        deductions = 5000
        expected_net = basic_salary + overtime - deductions

        try:
            self.payroll_service.generate_payroll(
                self.employee_id, self.start_date, self.end_date,
                basic_salary, overtime, deductions
            )
            print(f"✅ Net Salary calculated and inserted: {expected_net}")
            self.assertEqual(expected_net, 58000)
        except Exception as e:
            self.fail(f"❌ Failed to generate payroll: {e}")


if __name__ == '__main__':
    unittest.main()
