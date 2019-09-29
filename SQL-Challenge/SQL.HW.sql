--1. List the following details of each Employee: employee number, last name, first name, gender, and salary.
SELECT E.Emp_No,
	   E.Last_Name, 
	   E.First_Name,
	   E.Gender,
	   S.Salary
FROM SALARIES AS S
INNER JOIN Employees As E ON
E.Emp_No = S.Emp_No


--2. List employees who were hired in 1986.
SELECT Hire_Date, 
	   Last_Name, 
	   First_Name
FROM Employees
WHERE Hire_Date = DATE'1/1/1986';


-- 3.List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name and start and end employment dates.
SELECT dm.Dept_No, 
	   d.Dept_Name, 
	   E.Last_Name, 
	   E.First_Name, 
	   dm.From_Date, 
	   dm.To_Date,
	   E.Emp_No
 
FROM Dept_Manager AS dm 
INNER JOIN departments As d ON 
dm.Dept_No = d.Dept_No
INNER JOIN Employees As E ON
E.Emp_No = dm.Emp_No;

--4.List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT E.Emp_No,
	   E.Last_Name, 
	   E.First_Name,
	   D.Dept_Name,
	   DE.Dept_No
FROM Dept_Emp AS DE
INNER JOIN Employees As E ON
E.Emp_No = DE.Emp_No
INNER JOIN departments AS D ON
D.Dept_Name = D.Dept_Name

--5. List all the employees whose first name is "Hercules" and last names begin with "B".
SELECT First_Name, Last_Name
FROM Employees
WHERE First_Name LIKE 'Hercules%' AND Last_Name LIKE 'B%'

--6. List all employees in the Sales Department, including their employee number, last name, first name, and department name.
SELECT d.Dept_Name,
	   E.Emp_No,
	   E.Last_Name,
	   E.First_Name
FROM Employees AS E
INNER JOIN Dept_Emp AS DE ON
E.Emp_No = DE.Emp_No
INNER JOIN departments AS d ON
d.Dept_No = DE.Dept_No
WHERE d.Dept_Name in ('Sales')
ORDER BY E.Emp_No;


--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name. 
SELECT E.Emp_No,
	   d.Dept_Name, 
	   E.Last_Name, 
	   E.First_Name
FROM Employees AS E
INNER JOIN Dept_Emp AS DE ON
E.Emp_No = DE.Emp_No
INNER JOIN departments AS d ON
d.Dept_No = DE.Dept_No
WHERE d.Dept_Name in ('Sales', 'Development')
ORDER BY E.Emp_No;

--8. In descending order, list the frequency count of employee last names, i.e, how many employees share each last name. 
SELECT Last_Name, COUNT(*) AS CNT
FROM Employees
GROUP BY Last_Name 
ORDER BY CNT DESC
--HAVING COUNT(*) > 1















 

	 































