CREATE DATABASE demodb;
USE demodb;
-- Creating a table called Employees
CREATE TABLE employees(
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50),
  emp_email VARCHAR(100) UNIQUE,
  emp_salary DECIMAL(8,3) CHECK (emp_salary >=0),
  hire_date DATE DEFAULT(CURRENT_DATE),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE employees
ADD COLUMN gender CHAR(6);

ALTER TABLE employees
ADD COLUMN dob TIMESTAMP;

ALTER TABLE employees
ADD COLUMN dob TIMESTAMP;

INSERT INTO employees(emp_id,emp_name,emp_salary,emp_email)
VALUES (1,'vishwas',20000,'vishwas@cloudthat.com');

INSERT INTO employees(emp_id,emp_name,emp_salary,emp_email)
VALUES 
(2,'vishwas1',20000,'vishwas2@cloudthat.com'),
(3,'vishwas3',20000,'vishwas3@cloudthat.com'),
(4,'vishwas4',20000,'vishwas4@cloudthat.com'),
(5,'vishwas5',20000,'vishwas5@cloudthat.com');

SELECT * FROM employees;

UPDATE employees SET gender = 'MALE' WHERE emp_id=1;
DELETE FROM employees WHERE emp_id=5;

TRUNCATE TABLE employees;
