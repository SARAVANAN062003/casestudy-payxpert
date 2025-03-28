CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender VARCHAR(10) CHECK (Gender IN ('Male', 'Female', 'Other')) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20) UNIQUE NOT NULL,
    Address TEXT NOT NULL,
    Position VARCHAR(50) NOT NULL,
    JoiningDate DATE NOT NULL,
    TerminationDate DATE NULL
);

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT NOT NULL,
    PayPeriodStartDate DATE NOT NULL,
    PayPeriodEndDate DATE NOT NULL,
    BasicSalary DECIMAL(10,2) NOT NULL CHECK (BasicSalary >= 0),
    OvertimePay DECIMAL(10,2) DEFAULT 0 CHECK (OvertimePay >= 0),
    Deductions DECIMAL(10,2) DEFAULT 0 CHECK (Deductions >= 0),
    NetSalary AS (BasicSalary + OvertimePay - Deductions) PERSISTED, -- Computed column
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE
);

CREATE TABLE Tax (
    TaxID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT NOT NULL,
    TaxYear INT NOT NULL CHECK (TaxYear >= 1900 AND TaxYear <= YEAR(GETDATE())),
    TaxableIncome DECIMAL(10,2) NOT NULL CHECK (TaxableIncome >= 0),
    TaxAmount DECIMAL(10,2) NOT NULL CHECK (TaxAmount >= 0),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE
);

CREATE TABLE FinancialRecord (
    RecordID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT NOT NULL,
    RecordDate DATE NOT NULL,
    Description TEXT NOT NULL,
    Amount DECIMAL(10,2) NOT NULL CHECK (Amount >= 0),
    RecordType VARCHAR(20) CHECK (RecordType IN ('Income', 'Expense', 'Tax Payment')) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE
);
