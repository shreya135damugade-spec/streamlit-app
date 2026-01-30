import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(page_title="SQL Server DSN-less Connection")

st.title("🌐 SQL Server Connection (DSN-less via ODBC)")

st.markdown("Enter SQL Server connection details below:")

# ---- User Inputs ----
server = st.text_input(
    "SQL Server (IP,PORT)",
    "192.168.1.5,54906"
)

database = st.text_input(
    "Database Name",
    "Sales"
)

username = st.text_input(
    "SQL Username",
    "sql_user"
)

password = st.text_input(
    "SQL Password",
    type="password"
)

connect_btn = st.button("Connect")

# ---- Connection Logic ----
if connect_btn:
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=192.168.1.5,54906;"
            "DATABASE=Sales;"
            "UID=sql_user;"
            "PWD=StrongPassword@123;",
            timeout=30
        )

        st.success("✅ Connected successfully to SQL Server")

        df = pd.read_sql("SELECT name FROM sys.databases", conn)

        st.subheader("📂 Databases on Server")
        st.dataframe(df)

        conn.close()

    except Exception as e:
        st.error("❌ Connection failed")
        st.code(str(e))


