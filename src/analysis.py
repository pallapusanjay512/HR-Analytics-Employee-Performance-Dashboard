import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sriii@260108",
    database="hr_dashboard"
)

query = """
SELECT Department,
AVG(MonthlyIncome) AS AvgSalary
FROM employees
GROUP BY Department;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()