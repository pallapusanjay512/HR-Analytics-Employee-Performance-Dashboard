import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector


# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="👥",
    layout="wide"
)


# --------------------------------
# Database Connection Function
# --------------------------------
def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sriii@260108",
        database="hr_dashboard"
    )


# --------------------------------
# Load Data
# --------------------------------
@st.cache_data
def load_data():

    conn = get_connection()

    query = """
    SELECT *
    FROM employees;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df



df = load_data()


# --------------------------------
# Header
# --------------------------------

st.title("👥 HR Analytics Employee Performance Dashboard")

st.write(
    "Interactive dashboard to analyze employee performance, salary, attrition and work-life balance."
)


st.divider()



# --------------------------------
# KPI Cards
# --------------------------------

total_emp = len(df)

avg_salary = round(
    df["MonthlyIncome"].mean(),
    2
)

attrition_rate = (
    len(df[df["Attrition"]=="Yes"])
    /
    len(df)
)*100


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "👨‍💼 Total Employees",
        total_emp
    )


with col2:

    st.metric(
        "💰 Average Salary",
        f"₹ {avg_salary}"
    )


with col3:

    st.metric(
        "🚪 Attrition Rate",
        f"{round(attrition_rate,2)}%"
    )



st.divider()



# --------------------------------
# Sidebar Navigation
# --------------------------------

st.sidebar.title("📌 HR Analytics Menu")


option = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard Overview",
        "💰 Salary Analysis",
        "⭐ Performance Analysis",
        "🚪 Attrition Analysis",
        "⚖ Work-Life Balance",
        "🔎 Employee Search"
    ]
)



# --------------------------------
# Dashboard Overview
# --------------------------------

if option == "🏠 Dashboard Overview":


    st.header("📊 Employee Overview")


    st.info(
        "Select an analysis from the left menu to generate insights."
    )


    dept_count = (
        df["Department"]
        .value_counts()
    )


    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        dept_count.index,
        dept_count.values
    )

    ax.set_title(
        "Employees by Department"
    )

    ax.set_xlabel(
        "Department"
    )

    ax.set_ylabel(
        "Employees"
    )


    st.pyplot(fig)




# --------------------------------
# Salary Analysis
# --------------------------------

elif option == "💰 Salary Analysis":


    st.header("💰 Salary Insights")


    if st.button("Generate Salary Report"):


        salary_df = (
            df.groupby("Department")
            ["MonthlyIncome"]
            .mean()
            .reset_index()
        )


        fig, ax = plt.subplots(figsize=(8,4))


        ax.bar(
            salary_df["Department"],
            salary_df["MonthlyIncome"]
        )


        ax.set_title(
            "Average Salary by Department"
        )


        ax.set_ylabel(
            "Salary"
        )


        st.pyplot(fig)




# --------------------------------
# Performance Analysis
# --------------------------------

elif option == "⭐ Performance Analysis":


    st.header("⭐ Employee Performance")


    if st.button("Generate Performance Report"):


        performance = (
            df["PerformanceRating"]
            .value_counts()
        )


        fig, ax = plt.subplots()


        ax.bar(
            performance.index.astype(str),
            performance.values
        )


        ax.set_xlabel(
            "Performance Rating"
        )


        ax.set_ylabel(
            "Employees"
        )


        st.pyplot(fig)




# --------------------------------
# Attrition Analysis
# --------------------------------

elif option == "🚪 Attrition Analysis":


    st.header("🚪 Employee Attrition")


    if st.button("Generate Attrition Report"):


        attrition = (
            df["Attrition"]
            .value_counts()
        )


        fig, ax = plt.subplots(figsize=(5,5))


        ax.pie(
            attrition.values,
            labels=attrition.index,
            autopct="%1.1f%%"
        )


        ax.set_title(
            "Attrition Percentage"
        )


        st.pyplot(fig)




# --------------------------------
# Work Life Balance
# --------------------------------

elif option == "⚖ Work-Life Balance":


    st.header("⚖ Work-Life Balance")


    if st.button("Generate Work-Life Report"):


        balance = (
            df["WorkLifeBalance"]
            .value_counts()
        )


        fig, ax = plt.subplots()


        ax.bar(
            balance.index.astype(str),
            balance.values
        )


        ax.set_xlabel(
            "Balance Rating"
        )


        ax.set_ylabel(
            "Employees"
        )


        st.pyplot(fig)



# --------------------------------
# Employee Search
# --------------------------------

elif option == "🔎 Employee Search":


    st.header("🔎 Search Employee")


    employee_id = st.number_input(
        "Enter Employee ID",
        min_value=1
    )


    if st.button("Search Employee"):


        result = df[
            df["EmployeeNumber"] == employee_id
        ]


        if len(result) > 0:

            st.success(
                "Employee Found"
            )

            st.dataframe(result)


        else:

            st.error(
                "Employee not found"
            )