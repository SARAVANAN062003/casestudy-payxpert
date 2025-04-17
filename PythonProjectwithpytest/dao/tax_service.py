from dao.i_tax_service import ITaxService
from entity.tax import Tax
import decimal
from util.db_conn_util import GetDBConnection
from exception.tax_calculation_exception import TaxCalculationException


class TaxService(ITaxService):
    def calculate_tax(self, employee_id, tax_year):
        try:
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()

                # Calculate total income for the given employee and tax year
                cursor.execute("""
                          SELECT SUM(NetSalary) FROM Payroll 
                          WHERE EmployeeID = ? AND YEAR(PayPeriodEndDate) = ?
                      """, (employee_id, tax_year))
                total_income = cursor.fetchone()[0] or decimal.Decimal(0)  # Ensure it's a Decimal

                # Check if total income exists for the employee in the given year
                if total_income == 0:
                    print("No salary records found for this Employee and Year.")
                    return  # Stops further processing if there's no income

                # Define the tax rate as a decimal
                tax_rate = decimal.Decimal('0.1')  # 10% tax rate
                tax_amount = total_income * tax_rate

                # Print the calculated tax details
                print(f"Tax Calculation for Employee ID: {employee_id} for Year: {tax_year}")
                print(f"Total Income: {total_income}")
                print(f"Tax Amount: {tax_amount:.2f}")  # Prints the tax amount with two decimal places

        except Exception as e:
            raise TaxCalculationException(f"Failed to calculate tax: {e}")


    def get_tax_by_id(self, tax_id):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", (tax_id,))
            row = cursor.fetchone()
            return Tax(*row) if row else None

    def get_taxes_for_employee(self, employee_id):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE EmployeeID = ?", (employee_id,))
            rows = cursor.fetchall()
            return [Tax(*row) for row in rows]

    def get_taxes_for_year(self, tax_year):
        with GetDBConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", (tax_year,))
            rows = cursor.fetchall()
            return [Tax(*row) for row in rows]
