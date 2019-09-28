CREATE TABLE departments(
  Dept_No VARCHAR PRIMARY KEY,
  Dept_Name VARCHAR(250) NOT NULL
);

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name. 
SELECT Dept_Name
FROM departments
WHERE Dept_Name = 'Sales' AND 'Development' IN
(
	SELECT Emp_No, Last_Name, First_Name
	FROM Employees
	WHERE Emp_No = 'Sales' AND 'Development'
);


--6. List all employees in the Sales Department, including their employee number, last name, first name, and department name.
SELECT Dept_Name
FROM departments
WHERE Dept_Name = 'Sales'; IN
( 
	SELECT Emp_No, Last_Name, First_Name
	FROM Employees
	WHERE Emp_No = 'Sales'
);


--4.List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT Emp_No, Last_Name, First_Name
FROM EMPLOYEES 
WHERE EMPLOYEES(Emp_No) IN
( 
	SELECT Dept_Name
	FROM departments
	WHERE departments (Dept_Name)
);



CREATE TABLE dept_emp(
  Emp_No SERIAL NOT NULL,
  Dept_No VARCHAR NOT NULL,
  From_Date DATE,
  To_Date DATE,
  FOREIGN KEY (Emp_No) REFERENCES Employees(Emp_No),
  FOREIGN KEY (Dept_No) REFERENCES departments(Dept_No)
);

CREATE TABLE Dept_Manager(
  Dept_No VARCHAR NOT NULL,
  Emp_No SERIAL NOT NULL,
  From_Date DATE,
  To_Date DATE,
  FOREIGN KEY (Dept_No) REFERENCES departments (Dept_No),
  FOREIGN KEY (Emp_No) REFERENCES Employees(Emp_No)
);
-- 3.List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name and start and end employment dates.
SELECT Dept_No
FROM Dept_Manager
WHERE Dept_Manager IN
(
	SELECT Dept_Name
	FROM departments
	WHERE departments IN
	(
		SELECT Last_Name, First_Name
		FROM Employees
		WHERE Emp_No IN
		(
			SELECT From_Date, To_Date
			FROM Dept_Manager
			WHERE Dept_Manager
		)
	)
);

CREATE TABLE Employees(
  Emp_No SERIAL PRIMARY KEY,
  Birth_Date DATE,
  First_Name VARCHAR(250),
  Last_Name VARCHAR(250),
  Gender VARCHAR(250),
  Hire_Date DATE
);
--8. In descending order, list the frequency count of employee last names, i.e, how many employees share each last name. 
SELECT Last_Name, COUNT(*) AS CNT
FROM Employees
GROUP BY Last_Name 
ORDER BY CNT DESC
--HAVING COUNT(*) > 1 



--5. List all the employees whose first name is "Hercules" and last names begin with "B".
SELECT First_Name, Last_Name
FROM Employees
WHERE First_Name = 'Hercules' AND Last_Name = 'B'; 

--2. List employees who were hired in 1986.
SELECT Hire_Date
FROM Employees
WHERE Hire_Date BETWEEN 1/1/1986 AND 12/31/1986


--1. List the following details of each Employee: employee number, last name, first name, gender, and salary.
SELECT Last_Name, First_Name
FROM Employees
WHERE Emp_No IN
(
	SELECT Gender
	FROM Employees
	WHERE Emp_No IN
	(
		SELECT SALARY
		FROM Salaries
		WHERE Emp_No
	)
);







CREATE TABLE Salaries(
  Emp_No INTEGER NOT NULL,
  Salary INTEGER,
  From_Date VARCHAR(250),
  To_Date VARCHAR(250),
  FOREIGN KEY (Emp_No) REFERENCES Employees
);

CREATE TABLE Titles(
  Emp_No INTEGER NOT NULL,
  Title VARCHAR(250) NOT NULL,
  From_Date DATE,
  To_Date DATE,
  FOREIGN KEY (Emp_No) REFERENCES Employees(Emp_No)
);

















