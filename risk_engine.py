# %%
# Phase 4: Stress Testing & Provisioning (IFRS9 / CCAR)
# This is the "Director Level" logic.
# IFRS9: Calculating "Expected Credit Loss" (How much money should the bank set aside?).
    # ECL=PD * EAD * LGD
        # PD: Probability of Default (What is the chance the borrower will default?)
        # LGD: Loss Given Default (What is the loss if they do default?)
            # LGD=(EAD-Recovery Amount)/EAD
        # EAD: Exposure at Default (How much money is at risk?) 
# CCAR: Stress testing (What happens if the economy crashes?).

# %%
# pip install pyarrow

# %%
import pandas as pd

def calculate_ifrs9_ecl():
    # Load the processed data from the Spark step
    df = pd.read_parquet("data/processed_loans.parquet")
    
    # ECL Formula: Probability of Default (PD) * Loss Given Default (LGD) * Exposure (EAD)
    # Let's assume LGD is 45% (A common bank standard)
    LGD = 0.45
    
    # Calculate PD based on credit score (Higher score = Lower PD)
    df['PD'] = (850 - df['credit_score']) / 850 * 0.1
    
    # Expected Credit Loss (Provisioning)
    df['ECL'] = df['PD'] * LGD * df['current_balance']

    # ,.2f: commas and 2 decimal places
    print(f"Total Portfolio Provisioning (IFRS9): ${df['ECL'].sum():,.2f}")
    return df

def run_ccar_stress_test(df):
    # Scenario: Severe Recession (Unemployment triples, Credit Scores drop by 20%)
    print("\n--- Running CCAR Stress Test: 'Severe Adverse Scenario' ---")
    
    df_stressed = df.copy()
    df_stressed['stressed_PD'] = df_stressed['PD'] * 3.0 # PD triples in a crash
    df_stressed['stressed_ECL'] = df_stressed['stressed_PD'] * 0.45 * df_stressed['current_balance']
    
    print(f"📉 Stressed Portfolio Loss: ${df_stressed['stressed_ECL'].sum():,.2f}")
    print(f"⚠️ Capital Buffer Needed: ${(df_stressed['stressed_ECL'].sum() - df['ECL'].sum()):,.2f}")

if __name__ == "__main__":
    risk_data = calculate_ifrs9_ecl()
    run_ccar_stress_test(risk_data)


