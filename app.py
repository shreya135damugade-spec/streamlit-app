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
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            "TrustServerCertificate=yes;"
        )

        conn = pyodbc.connect(conn_str, timeout=5)

        st.success("✅ Connected successfully to SQL Server")

        # ---- Test Query ----
        query = "SELECT name FROM sys.databases"
        df = pd.read_sql(query, conn)

        st.subheader("📂 Databases on Server")
        st.dataframe(df)

        conn.close()

    except Exception as e:
        st.error("❌ Connection failed")
        st.code(str(e))

