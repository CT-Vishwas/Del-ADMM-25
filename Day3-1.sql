CREATE DATABASE demodb;
USE demodb;
CREATE TABLE 
	employees(id INT, name VARCHAR(30), manager_id INT);
    
INSERT INTO employees VALUES
(1, 'Vishwas',3),
(2, 'John',3),(3, 'Jane',NULL),(4, 'Janice',1);

SELECT * FROM employees;


SELECT t1.id,t1.name AS employee_name, t2.name AS manager_name 
FROM employees t1
JOIN employees t2
ON t1.manager_id = t2.id;

SELECT * FROM user_emails;
DROP TABLE user_emails;

SELECT SUBSTRING(Email, 1, LOCATE('@', Email)-1) AS UserName FROM user_emails;