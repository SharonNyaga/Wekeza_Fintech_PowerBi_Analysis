"""
SQLite import script for Power BI

Loads the seven tables from the Wekeza SQLite database into pandas DataFrames
for use with Power BI's "Get Data > Python script" connector.

In Power BI Desktop:
Home > Get data > Other > Python script
Paste the contents of this file into the script box, or open this file and copy
the code into the script box.

"""

import sqlite3
import pandas as pd

# 1. Database path
db_path = r"C:\Users\Administrator\Desktop\Wekeza_Fintech_Case_Study\kenya_fintech.db"

# 2. Connect to SQLite
conn = sqlite3.connect(db_path)

try:
    # 3. Extract the seven tables into pandas DataFrames
    agents = pd.read_sql_query("SELECT * FROM agents", conn)
    counties = pd.read_sql_query("SELECT * FROM counties", conn)
    customers = pd.read_sql_query("SELECT * FROM customers", conn)
    loan_products = pd.read_sql_query("SELECT * FROM loan_products", conn)
    loans = pd.read_sql_query("SELECT * FROM loans", conn)
    repayments = pd.read_sql_query("SELECT * FROM repayments", conn)
    transactions = pd.read_sql_query("SELECT * FROM transactions", conn)

finally:
    # 4. Close the database connection
    conn.close()