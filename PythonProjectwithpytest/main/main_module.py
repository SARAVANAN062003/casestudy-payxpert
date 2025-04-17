from dao.employee_service import EmployeeService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from dao.financial_record_service import FinancialRecordService
from exception.invalid_input_exception import InvalidInputException
from entity.employee import Employee
from entity.payroll import Payroll
from entity.tax import Tax
from entity.financial_record import FinancialRecord
from exception.tax_calculation_exception import TaxCalculationException
def show_menu():
    print("\n====== PayXpert Payroll Management System ======")
    print("1. Employee Management")
    print("2. Payroll Processing")
    print("3. Tax Calculation")
    print("4. Financial Records")
    print("5. Exit")
    print("===============================================\n")

# Employee Management functions
def manage_employees(employee_service):
    while True:
        print("\n===== Employee Management =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Remove Employee")
        print("5. Go Back")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                emp_id = int(input("Employee ID: "))
                fname = input("First Name: ")
                lname = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                gender = input("Gender: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                position = input("Position: ")
                joining = input("Joining Date (YYYY-MM-DD): ")
                termination = input("Termination Date (YYYY-MM-DD) or leave blank: ") or None

                employee = Employee(
                    employee_id=emp_id, first_name=fname, last_name=lname, date_of_birth=dob,
                    gender=gender, email=email, phone_number=phone, address=address, position=position,
                    joining_date=joining, termination_date=termination
                )
                employee_service.add_employee(employee)  # Pass Employee object
                print("Employee added successfully.")

            elif choice == "2":
                employees = employee_service.get_all_employees()
                for emp in employees:
                    print(f"ID: {emp.employee_id}, Name: {emp.first_name} {emp.last_name}, Position: {emp.position}")

            elif choice == "3":
                emp_id = int(input("Enter Employee ID to update: "))
                fname = input("New First Name: ")
                lname = input("New Last Name: ")
                email = input("New Email: ")
                position = input("New Position: ")

                employee = employee_service.get_employee_by_id(emp_id)  # Retrieve existing employee
                employee.first_name = fname
                employee.last_name = lname
                employee.email = email
                employee.position = position

                employee_service.update_employee(employee)  # Pass updated Employee object
                print(f"Employee {emp_id} updated successfully.")

            elif choice == "4":
                emp_id = int(input("Enter Employee ID to remove: "))
                employee_service.remove_employee(emp_id)
                print(f"Employee {emp_id} removed successfully.")

            elif choice == "5":
                break

            else:
                raise InvalidInputException("Invalid choice. Please enter a valid option.")

        except Exception as e:
            print(f"Error: {e}")

# Payroll Processing functions
from exception.invalid_input_exception import InvalidInputException
from exception.payroll_generation_exception import PayrollGenerationException
from datetime import datetime


def validate_date(date_str):
    """Helper function to validate date format and check if start date is before end date."""
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date
    except ValueError:
        raise InvalidInputException("Invalid date format. Use YYYY-MM-DD.")


def manage_payroll(payroll_service):
    while True:
        print("\n===== Payroll Processing =====")
        print("1. Generate Payroll")
        print("2. View Payroll by ID")
        print("3. View Payrolls for Employee")
        print("4. View Payrolls for Period")
        print("5. Go Back")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                payroll_id = int(input("Enter Payroll ID: "))
                emp_id = int(input("Enter Employee ID: "))
                start = input("Pay Period Start Date (YYYY-MM-DD): ")
                end = input("Pay Period End Date (YYYY-MM-DD): ")

                start_date = validate_date(start)
                end_date = validate_date(end)

                # Validate that the start date is before the end date
                if start_date > end_date:
                    raise InvalidInputException("Start date cannot be after the end date.")

                basic = float(input("Basic Salary: "))
                overtime = float(input("Overtime Pay: "))
                deductions = float(input("Deductions: "))

                # Validate negative salaries or deductions
                if basic < 0 or overtime < 0 or deductions < 0:
                    raise InvalidInputException("Salary, overtime pay, and deductions cannot be negative.")

                payroll_service.generate_payroll(
                    payroll_id, emp_id, start_date, end_date, basic, overtime, deductions
                )
                print("Payroll generated successfully.")

            elif choice == "2":
                payroll_id = int(input("Enter Payroll ID: "))
                payroll = payroll_service.get_payroll_by_id(payroll_id)
                if payroll:
                    print(f"Payroll ID: {payroll.payroll_id}, Employee ID: {payroll.employee_id}, "
                          f"Net Salary: {payroll.net_salary}")
                else:
                    print(f"No payroll found with ID {payroll_id}.")

            elif choice == "3":
                emp_id = int(input("Enter Employee ID: "))
                payrolls = payroll_service.get_payrolls_for_employee(emp_id)
                if payrolls:
                    for payroll in payrolls:
                        print(
                            f"Payroll ID: {payroll.payroll_id}, Period: {payroll.pay_period_start} to {payroll.pay_period_end}, "
                            f"Net Salary: {payroll.net_salary}")
                else:
                    print(f"No payroll records found for Employee ID {emp_id}.")

            elif choice == "4":
                start_date = input("Enter Pay Period Start Date (YYYY-MM-DD): ")
                end_date = input("Enter Pay Period End Date (YYYY-MM-DD): ")

                start_date = validate_date(start_date)
                end_date = validate_date(end_date)

                # Validate that the start date is before the end date
                if start_date > end_date:
                    raise InvalidInputException("Start date cannot be after the end date.")

                payrolls = payroll_service.get_payrolls_for_period(start_date, end_date)
                if payrolls:
                    for payroll in payrolls:
                        print(f"Payroll ID: {payroll.payroll_id}, Employee ID: {payroll.employee_id}, "
                              f"Net Salary: {payroll.net_salary}")
                else:
                    print(f"No payroll records found for the period {start_date} to {end_date}.")

            elif choice == "5":
                break

            else:
                raise InvalidInputException("Invalid choice. Please enter a valid option.")

        except InvalidInputException as e:
            print(f"Error: {e}")
        except PayrollGenerationException as e:
            print(f"Payroll generation failed: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Tax Calculation functions
def manage_taxes(tax_service: TaxService):
    while True:
        print("\n===== Tax Calculation =====")
        print("1. Calculate Tax for Employee")
        print("2. View Tax by ID")
        print("3. View Taxes for Employee")
        print("4. View Taxes for Year")
        print("5. Go Back")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                try:
                    emp_id = int(input("Enter Employee ID: "))
                    year = int(input("Enter Tax Year: "))

                    # Calculate tax for the given employee and year
                    tax_service.calculate_tax(emp_id, year)

                except ValueError:
                    print("Please enter valid numeric values for Employee ID and Tax Year.")

            elif choice == "2":
                try:
                    tax_id = int(input("Enter Tax ID: "))
                    tax = tax_service.get_tax_by_id(tax_id)
                    if tax:
                        print(
                            f"Tax ID: {tax.tax_id}, Employee ID: {tax.employee_id}, Tax Year: {tax.tax_year}, Tax Amount: {tax.tax_amount}")
                    else:
                        print(f"No tax record found with ID {tax_id}.")
                except ValueError:
                    print("Please enter a valid numeric value for Tax ID.")

            elif choice == "3":
                try:
                    emp_id = int(input("Enter Employee ID: "))
                    taxes = tax_service.get_taxes_for_employee(emp_id)
                    if taxes:
                        for tax in taxes:
                            print(f"Tax ID: {tax.tax_id}, Year: {tax.tax_year}, Tax Amount: {tax.tax_amount}")
                    else:
                        print(f"No tax records found for Employee ID {emp_id}.")
                except ValueError:
                    print("Please enter a valid numeric value for Employee ID.")

            elif choice == "4":
                try:
                    tax_year = int(input("Enter Tax Year: "))
                    taxes = tax_service.get_taxes_for_year(tax_year)
                    if taxes:
                        for tax in taxes:
                            print(f"Tax ID: {tax.tax_id}, Employee ID: {tax.employee_id}, Tax Amount: {tax.tax_amount}")
                    else:
                        print(f"No tax records found for the year {tax_year}.")
                except ValueError:
                    print("Please enter a valid numeric value for Tax Year.")

            elif choice == "5":
                break

            else:
                print("Invalid choice. Please enter a valid option.")

        except TaxCalculationException as e:
            print(f"Error: {e}")


# Financial Record functions
def manage_financial_records(financial_service):
    while True:
        print("\n===== Financial Records =====")
        print("1. Add Financial Record")
        print("2. View Financial Records by Employee")
        print("3. View Financial Record by Date")
        print("4. View Financial Records with Payroll Period by Date")
        print("5. Go Back")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                rec_id = int(input("Record ID: "))
                emp_id = int(input("Employee ID: "))
                date = input("Record Date (YYYY-MM-DD): ")
                desc = input("Description: ")
                amount = float(input("Amount: "))
                rec_type = input("Record Type (income/expense/tax): ")

                # Create FinancialRecord object
                record = FinancialRecord(
                    record_id=rec_id,
                    employee_id=emp_id,
                    record_date=date,
                    description=desc,
                    amount=amount,
                    record_type=rec_type
                )

                financial_service.add_financial_record(record)
                print("Financial record added successfully.")

            elif choice == "2":
                emp_id = int(input("Enter Employee ID: "))
                records = financial_service.get_financial_records_for_employee(emp_id)
                for record in records:
                    print(f"ID: {record.record_id}, Date: {record.record_date}, "
                          f"Description: {record.description}, Amount: {record.amount}, Type: {record.record_type}")

            elif choice == "3":
                date = input("Enter Date (YYYY-MM-DD): ")
                records = financial_service.get_financial_records_for_date(date)
                for record in records:
                    print(f"ID: {record.record_id}, Employee ID: {record.employee_id}, "
                          f"Description: {record.description}, Amount: {record.amount}, Type: {record.record_type}")

            elif choice == "4":
                date = input("Enter Date (YYYY-MM-DD): ")
                records_with_payroll = financial_service.get_financial_records_with_payroll_period_by_date(date)
                for record in records_with_payroll:
                    print(f"ID: {record[0]}, Employee ID: {record[1]}, Date: {record[2]}, "
                          f"Description: {record[3]}, Amount: {record[4]}, Type: {record[5]}, "
                          f"Pay Period: {record[6]} to {record[7]}")

            elif choice == "5":
                break

            else:
                raise InvalidInputException("Invalid choice. Please enter a valid option.")

        except Exception as e:
            print(f"Error: {e}")

# Main function that integrates all services
def main():
    employee_service = EmployeeService()
    payroll_service = PayrollService()
    tax_service = TaxService()
    financial_service = FinancialRecordService()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                manage_employees(employee_service)
            elif choice == "2":
                manage_payroll(payroll_service)
            elif choice == "3":
                manage_taxes(tax_service)
            elif choice == "4":
                manage_financial_records(financial_service)
            elif choice == "5":
                print("Exiting PayXpert... Goodbye!")
                break
            else:
                raise InvalidInputException("Invalid choice. Please enter a valid option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
