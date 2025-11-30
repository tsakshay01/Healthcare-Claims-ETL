import pandas as pd
import random
from faker import Faker


fake = Faker()


NUM_ROWS = 10000

print(f"Generating {NUM_ROWS} rows of healthcare claim data...")


data = []


diagnosis_codes = ['J01.90', 'E11.9', 'I10', 'M54.5', 'Z00.00', 'R05']
statuses = ['Paid', 'Rejected', 'Pending']

for i in range(NUM_ROWS):
    
    claim_id = f"CLM-{i+1000}"
    patient_id = random.randint(1000, 9999)
   
    patient_name = fake.name()
    if random.choice([True, False]):
        patient_name = patient_name.lower()
    
    
    if random.random() < 0.95: 
        provider_npi = str(random.randint(1000000000, 9999999999))
    else:
        provider_npi = str(random.randint(100000000, 999999999)) 
        
    diagnosis_code = random.choice(diagnosis_codes)
    
   
    claim_amount = round(random.uniform(50.0, 12000.0), 2)
    
    status = random.choice(statuses)
    
   
    if random.random() < 0.02:
        status = None
        
    data.append([claim_id, patient_id, patient_name, provider_npi, diagnosis_code, claim_amount, status])


columns = ['Claim_ID', 'Patient_ID', 'Patient_Name', 'Provider_NPI', 'Diagnosis_Code', 'Claim_Amount', 'Status']
df = pd.DataFrame(data, columns=columns)


df = pd.concat([df, df.head(50)], ignore_index=True)


csv_filename = 'claims_raw.csv'
df.to_csv(csv_filename, index=False)

print(f"Success! Data saved to '{csv_filename}' with {len(df)} rows (including duplicates).")