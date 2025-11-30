import sqlite3
import pandas as pd


conn = sqlite3.connect('healthcare.db')

print("--- HEALTHCARE CLAIMS ANALYSIS ---\n")


print("1. Top 5 Providers by Amount Claimed:")
query1 = """
SELECT 
    Provider_NPI, 
    COUNT(*) as Total_Claims, 
    SUM(Claim_Amount) as Total_Amount 
FROM claims 
GROUP BY Provider_NPI 
ORDER BY Total_Amount DESC 
LIMIT 5;
"""

df1 = pd.read_sql_query(query1, conn)
print(df1)
print("-" * 30)


print("\n2. Claims Status Breakdown:")
query2 = """
SELECT 
    Status, 
    COUNT(*) as Count 
FROM claims 
GROUP BY Status;
"""
df2 = pd.read_sql_query(query2, conn)
print(df2)
print("-" * 30)


print("\n3. Average Cost per Diagnosis Code:")
query3 = """
SELECT 
    Diagnosis_Code, 
    ROUND(AVG(Claim_Amount), 2) as Avg_Cost 
FROM claims 
GROUP BY Diagnosis_Code 
ORDER BY Avg_Cost DESC;
"""
df3 = pd.read_sql_query(query3, conn)
print(df3)

conn.close()