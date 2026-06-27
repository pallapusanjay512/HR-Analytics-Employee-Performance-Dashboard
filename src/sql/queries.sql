-- Total Employees
SELECT COUNT(*) AS Total_Employees
FROM employees;

-- Employees by Department
SELECT Department, COUNT(*) AS Total
FROM employees
GROUP BY Department;

-- Average Salary by Department
SELECT Department, AVG(MonthlyIncome) AS Avg_Salary
FROM employees
GROUP BY Department;

-- Average Performance Rating
SELECT AVG(PerformanceRating) AS Avg_Performance
FROM employees;

-- Attrition Count
SELECT Attrition, COUNT(*) AS Total
FROM employees
GROUP BY Attrition;

-- Average Experience
SELECT AVG(TotalWorkingYears) AS Avg_Experience
FROM employees;