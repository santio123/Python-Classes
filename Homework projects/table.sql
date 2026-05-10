-- 1. Create the Employees table
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2),
    HireDate DATE
);

-- 2. Manipulate data (Insert employee details)
INSERT INTO Employees (EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES 
(101, 'Rahul', 'Sharma', 'IT', 65000.00, '2022-01-15'),
(102, 'Priya', 'Verma', 'HR', 55000.00, '2021-03-22'),
(103, 'Amit', 'Singh', 'Finance', 75000.00, '2020-11-10'),
(104, 'Sneha', 'Reddy', 'IT', 68000.00, '2023-05-01'),
(105, 'Vikram', 'Malhotra', 'Marketing', 48000.00, '2022-08-19');

-- 3. Filter data (Find employees in the IT department)
SELECT * FROM Employees 
WHERE Department = 'IT';

-- 4. Sort data (List all employees by salary from highest to lowest)
SELECT * FROM Employees 
ORDER BY Salary DESC;

-- 5. Manipulate data (Update an employee's salary)
UPDATE Employees 
SET Salary = 70000.00 
WHERE EmpID = 101;

-- 6. View the final table
SELECT * FROM Employees;