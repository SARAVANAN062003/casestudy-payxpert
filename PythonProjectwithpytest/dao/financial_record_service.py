from dao.i_financial_record_service import IFinancialRecordService
from entity.financial_record import FinancialRecord
from util.db_conn_util import GetDBConnection
from exception.financial_record_exception import FinancialRecordException


class FinancialRecordService(IFinancialRecordService):
    def add_financial_record(self, record):
        try:
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO FinancialRecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    record.record_id,
                    record.employee_id,
                    record.record_date,
                    record.description,
                    record.amount,
                    record.record_type
                ))
                conn.commit()
        except Exception as e:
            raise FinancialRecordException(f"Failed to add financial record: {e}")

    def get_financial_record_by_id(self, record_id):
        try:
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID = ?", (record_id,))
                row = cursor.fetchone()
                return FinancialRecord(*row) if row else None
        except Exception as e:
            raise FinancialRecordException(f"Error retrieving financial record by ID: {e}")

    def get_financial_records_for_employee(self, employee_id):
        try:
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,))
                rows = cursor.fetchall()
                return [FinancialRecord(*row) for row in rows]
        except Exception as e:
            raise FinancialRecordException(f"Error retrieving records for employee: {e}")

    def get_financial_records_for_date(self, record_date):
        try:
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM FinancialRecord WHERE RecordDate = ?", (record_date,))
                rows = cursor.fetchall()
                return [FinancialRecord(*row) for row in rows]
        except Exception as e:
            raise FinancialRecordException(f"Error retrieving records for date: {e}")

    def get_financial_records_with_payroll_period_by_date(self, record_date):
        try:
            with GetDBConnection.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT fr.RecordID, fr.EmployeeID, fr.RecordDate, fr.Description, fr.Amount, fr.RecordType,
                           p.PayPeriodStartDate, p.PayPeriodEndDate
                    FROM FinancialRecord fr
                    JOIN Payroll p ON fr.EmployeeID = p.EmployeeID
                    WHERE fr.RecordDate = ?
                """, (record_date,))
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            raise FinancialRecordException(f"Error fetching records with payroll period: {e}")
