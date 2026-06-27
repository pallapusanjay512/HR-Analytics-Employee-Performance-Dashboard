import pandas as pd
import mysql.connector

# Read CSV file
df = pd.read_csv("dataset/employee_data.csv")

# Keep only required columns
df = df[['EmployeeNumber','Age','Attrition','Department','Gender',
         'JobRole','MonthlyIncome','TotalWorkingYears',
         'YearsAtCompany','PerformanceRating','WorkLifeBalance']]

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sriii@260108",   # <-- Replace with your actual password
    database="hr_dashboard"
)

cursor = conn.cursor()

query = """
INSERT INTO employees
(EmployeeNumber, Age, Attrition, Department, Gender, JobRole,
MonthlyIncome, TotalWorkingYears, YearsAtCompany,
PerformanceRating, WorkLifeBalance)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for row in df.itertuples(index=False):
    cursor.execute(query, tuple(row))

conn.commit()

print("Data Imported Successfully!")

cursor.close()
conn.close()