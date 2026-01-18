# %%
'''
Generating the Data
write a script to create a "Synthetic Dataset" that looks like real loan data.
'''

# %%
import pandas as pd
import numpy as np
import os

# Create a 'data' folder to keep things organized
if not os.path.exists('data'):
    os.makedirs('data')

def generate_bank_data(records=5000):
    np.random.seed(42) # Ensures the "random" data is the same every time you run it
    
    data = {
        'loan_id': range(1000, 1000 + records),
        'customer_income': np.random.randint(30000, 150000, records),
        'credit_score': np.random.randint(300, 850, records),
        'loan_amount': np.random.randint(5000, 50000, records),
        'interest_rate': np.random.uniform(0.03, 0.25, records),
        'employment_status': np.random.choice(['Employed', 'Self-Employed', 'Unemployed'], records, p=[0.8, 0.15, 0.05]),
        'current_balance': np.random.randint(1000, 50000, records)
    }
    
    df = pd.DataFrame(data)
    print(df)
    # Save as a CSV file (The "Raw" data)
    df.to_csv('data/raw_loans.csv', index=False)
    print("✅ Successfully generated 5,000 loan records in data/raw_loans.csv")

if __name__ == "__main__":
    generate_bank_data()


