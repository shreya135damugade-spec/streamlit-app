from fastapi import FastAPI
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str, timeout=10)

@app.get("/databases")
def get_databases():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.databases")
    rows = cursor.fetchall()
    conn.close()
    return {"databases": [r[0] for r in rows]}



