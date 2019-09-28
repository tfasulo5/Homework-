CREATE TABLE departments(
  Dept_No VARCHAR PRIMARY KEY,
  Dept_Name VARCHAR(250) NOT NULL
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

CREATE TABLE Employees(
  Emp_No SERIAL PRIMARY KEY,
  Birth_Date DATE,
  First_Name VARCHAR(250),
  Last_Name VARCHAR(250),
  Gender VARCHAR(250),
  Hire_Date DATE
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