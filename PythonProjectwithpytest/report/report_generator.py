import os
from datetime import datetime


class ReportGenerator:
    def __init__(self, report_type):
        self.report_type = report_type

    def generate_payroll_report(self, employees):
        """ Generate a payroll report for the given list of employees. """
        report_content = self._create_header()
        report_content += self._generate_payroll_report_content(employees)
        report_content += self._create_footer()

        return report_content

    def _create_header(self):
        """ Create the header for the report. """
        header = f"Payroll Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        header += "-" * 60 + "\n"
        header += f"{'Employee ID':<12}{'Name':<25}{'Gross Salary':<15}{'Net Salary':<15}\n"
        header += "-" * 60 + "\n"
        return header

    def _generate_payroll_report_content(self, employees):
        """ Generate the content of the payroll report. """
        content = ""
        for emp in employees:
            content += f"{emp['employee_id']:<12}{emp['name']:<25}{emp['gross_salary']:<15}{emp['net_salary']:<15}\n"
        return content

    def _create_footer(self):
        """ Create the footer for the report. """
        footer = "-" * 60 + "\n"
        footer += f"Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        return footer

    def generate_report(self, employees):
        """ Generate the complete report based on the type of report. """
        if self.report_type == "payroll":
            return self.generate_payroll_report(employees)
        else:
            raise ValueError("Invalid report type.")

    def save_report_to_file(self, report_content, filename="payroll_report.txt"):
        """ Save the report content to a file. """
        with open(filename, 'w') as file:
            file.write(report_content)
        print(f"Report saved as {filename}")


# Example Usage
if __name__ == "__main__":
    # Sample Employee Data (In a real scenario, this data could be fetched from the database)
    employees = [
        {"employee_id": 1, "name": "John Doe", "gross_salary": 6500, "net_salary": 5000},
        {"employee_id": 2, "name": "Jane Smith", "gross_salary": 7200, "net_salary": 5800},
        {"employee_id": 3, "name": "Alice Johnson", "gross_salary": 8000, "net_salary": 6400},
    ]

    # Generate Payroll Report
    report_generator = ReportGenerator(report_type="payroll")
    report_content = report_generator.generate_report(employees)

    # Save Report to File
    report_generator.save_report_to_file(report_content, "payroll_report.txt")

    # Print the report
    print(report_content)
