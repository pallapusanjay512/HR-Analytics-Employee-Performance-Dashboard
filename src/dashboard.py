import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")

st.title("📊 HR Analytics & Employee Performance Dashboard")
st.write("Analyze employee performance, salaries, attrition, and work-life balance.")

# -------------------------------
# Database Connection
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sriii@260108",   # <-- Replace with your password
    database="hr_dashboard"
)

# -------------------------------
# KPI Section
# -------------------------------
total_emp = pd.read_sql("SELECT COUNT(*) AS Total FROM employees;", conn)
avg_salary = pd.read_sql("SELECT ROUND(AVG(MonthlyIncome),2) AS Salary FROM employees;", conn)
avg_perf = pd.read_sql("SELECT ROUND(AVG(PerformanceRating),2) AS Rating FROM employees;", conn)

col1, col2, col3 = st.columns(3)

col1.metric("👨‍💼 Total Employees", int(total_emp.iloc[0,0]))
col2.metric("💰 Avg Salary", f"₹ {avg_salary.iloc[0,0]}")
col3.metric("⭐ Avg Performance", avg_perf.iloc[0,0])

st.divider()

# -------------------------------
# Department-wise Salary
# -------------------------------
st.subheader("📈 Department-wise Average Salary")

query = """
SELECT Department, AVG(MonthlyIncome) AS AvgSalary
FROM employees
GROUP BY Department;
"""

df = pd.read_sql(query, conn)

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(df["Department"], df["AvgSalary"])
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
ax.set_title("Average Salary by Department")

st.pyplot(fig)

# -------------------------------
# Attrition Pie Chart
# -------------------------------
st.subheader("🥧 Employee Attrition")

query = """
SELECT Attrition, COUNT(*) AS Total
FROM employees
GROUP BY Attrition;
"""

df = pd.read_sql(query, conn)

fig2, ax2 = plt.subplots(figsize=(5,5))
ax2.pie(df["Total"], labels=df["Attrition"], autopct="%1.1f%%")
ax2.set_title("Employee Attrition")

st.pyplot(fig2)

# -------------------------------
# Performance Rating
# -------------------------------
st.subheader("⭐ Performance Rating Distribution")

query = """
SELECT PerformanceRating, COUNT(*) AS Total
FROM employees
GROUP BY PerformanceRating;
"""

df = pd.read_sql(query, conn)

fig3, ax3 = plt.subplots(figsize=(7,4))
ax3.bar(df["PerformanceRating"].astype(str), df["Total"])
ax3.set_xlabel("Performance Rating")
ax3.set_ylabel("Employees")

st.pyplot(fig3)

# -------------------------------
# Work-Life Balance
# -------------------------------
st.subheader("⚖ Work-Life Balance")

query = """
SELECT WorkLifeBalance, COUNT(*) AS Total
FROM employees
GROUP BY WorkLifeBalance;
"""

df = pd.read_sql(query, conn)

fig4, ax4 = plt.subplots(figsize=(7,4))
ax4.bar(df["WorkLifeBalance"].astype(str), df["Total"])
ax4.set_xlabel("Work-Life Balance")
ax4.set_ylabel("Employees")

st.pyplot(fig4)

conn.close()