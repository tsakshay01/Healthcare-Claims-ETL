import pandas as pd
import sqlite3
import os

# Define the database file name
db_file = 'healthcare.db'

# --- 1. EXTRACT ---
print("1. EXTRACT: Reading CSV...")
df = pd.read_csv('claims_raw.csv')

# --- 2. TRANSFORM ---
print("2. TRANSFORM: Cleaning data...")
# Remove duplicates
df = df.drop_duplicates()
# Fill missing status
df['Status'] = df['Status'].fillna('Rejected')
# Title case names
df['Patient_Name'] = df['Patient_Name'].str.title()
# Validate NPI (Keep only 10-digit NPIs)
df = df[df['Provider_NPI'].astype(str).str.len() == 10]
# High Risk Logic
df['Is_High_Risk'] = df['Claim_Amount'] > 10000
# Rounding
df['Claim_Amount'] = df['Claim_Amount'].round(2)

print(f"   Data cleaned. {len(df)} valid rows remaining.")

# --- 3. LOAD ---
print("3. LOAD: Saving to SQL...")

# Connect to SQLite (This creates the file 'healthcare.db' if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# This is the Magic Line:
# It takes the Pandas DataFrame and pushes it into a SQL Table named 'claims'
# if_exists='replace' means: If the table exists, drop it and create a new one.
df.to_sql('claims', conn, if_exists='replace', index=False)

# Close connection
conn.close()

print(f"Success! Data loaded into '{db_file}' inside table 'claims'.")