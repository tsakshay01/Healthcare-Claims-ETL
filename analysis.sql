-- Query 1: Top 5 Providers by Total Claim Amount
-- This helps identify which doctors are billing the most money.
SELECT 
    Provider_NPI, 
    COUNT(*) as Total_Claims, 
    SUM(Claim_Amount) as Total_Amount 
FROM claims 
GROUP BY Provider_NPI 
ORDER BY Total_Amount DESC 
LIMIT 5;

-- Query 2: Rejected vs. Paid Counts
-- This helps us see how many claims are getting denied.
SELECT 
    Status, 
    COUNT(*) as Count 
FROM claims 
GROUP BY Status;

-- Query 3: Average Cost per Diagnosis
-- This tells us which diseases are the most expensive to treat.
SELECT 
    Diagnosis_Code, 
    AVG(Claim_Amount) as Avg_Cost 
FROM claims 
GROUP BY Diagnosis_Code 
ORDER BY Avg_Cost DESC;