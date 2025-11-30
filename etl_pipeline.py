import pandas as pd
import sqlite3
import os


db_file = 'healthcare.db'


print("1. EXTRACT: Reading CSV...")
df = pd.read_csv('claims_raw.csv')


print("2. TRANSFORM: Cleaning data...")

df = df.drop_duplicates()

df['Status'] = df['Status'].fillna('Rejected')

df['Patient_Name'] = df['Patient_Name'].str.title()

df = df[df['Provider_NPI'].astype(str).str.len() == 10]

df['Is_High_Risk'] = df['Claim_Amount'] > 10000

df['Claim_Amount'] = df['Claim_Amount'].round(2)

print(f"   Data cleaned. {len(df)} valid rows remaining.")


print("3. LOAD: Saving to SQL...")


conn = sqlite3.connect(db_file)
cursor = conn.cursor()


df.to_sql('claims', conn, if_exists='replace', index=False)


conn.close()

print(f"Success! Data loaded into '{db_file}' inside table 'claims'.")