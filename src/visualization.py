
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import os

os.makedirs("images", exist_ok=True)
# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sriii@260108",
    database="hr_dashboard"
)

# 1. Department-wise Average Salary
query1 = """
SELECT Department, AVG(MonthlyIncome) AS AvgSalary
FROM employees
GROUP BY Department;
"""

df1 = pd.read_sql(query1, conn)

plt.figure(figsize=(8,5))
plt.bar(df1["Department"], df1["AvgSalary"])
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=10)
plt.tight_layout()
output_folder = os.path.join(os.getcwd(), "images")
os.makedirs(output_folder, exist_ok=True)

plt.savefig(os.path.join(output_folder, "department_salary.png"))
plt.show()
plt.close()

# 2. Attrition Analysis
query2 = """
SELECT Attrition, COUNT(*) AS Total
FROM employees
GROUP BY Attrition;
"""

df2 = pd.read_sql(query2, conn)

plt.figure(figsize=(6,6))
plt.pie(df2["Total"], labels=df2["Attrition"], autopct="%1.1f%%")
plt.title("Employee Attrition")
plt.savefig(os.path.join(output_folder, "attrition.png"))
plt.show()
plt.close()

conn.close()

print("Charts created successfully!")