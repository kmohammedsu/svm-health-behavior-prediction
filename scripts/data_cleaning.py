import pandas as pd
import numpy as np

# Paths
INPUT = './data/nhis_2022.csv'
OUTPUT = './data/nhis_2022_cleaned.csv'

# Read data
df = pd.read_csv(INPUT)

# --- Keep SAMPWEIGHT as weight ---
df['weight'] = df['SAMPWEIGHT']

# --- Clean Demographics ---
# AGE: set 997, 998, 999 to blank
df.loc[df['AGE'].isin([997, 998, 999]), 'AGE'] = np.nan

# SEX: set 7, 8, 9 to blank
df.loc[df['SEX'].isin([7, 8, 9]), 'SEX'] = np.nan

# MARSTCUR: set 0, 9 to blank
df.loc[df['MARSTCUR'].isin([0, 9]), 'MARSTCUR'] = np.nan

# EDUC: set 996, 997, 998, 999, 0 to blank
df.loc[df['EDUC'].isin([996, 997, 998, 999, 0]), 'EDUC'] = np.nan

# --- Clean Health Condition Variables ---
for col in ['CANCEREV', 'CHEARTDIEV', 'DIABETICEV', 'HEARTATTEV', 'STROKEV']:
    df.loc[df[col].isin([7, 8, 9, 0]), col] = np.nan

# --- Clean Key Health Metrics ---
# BMICALC: 996.0, 0.0 to blank
df.loc[df['BMICALC'].isin([996.0, 0.0]), 'BMICALC'] = np.nan

# HRSLEEP: 97, 98, 99, 0 to blank
df.loc[df['HRSLEEP'].isin([97, 98, 99, 0]), 'HRSLEEP'] = np.nan

# VIG10DMIN: 996, 997, 998, 999, 0 to blank
df.loc[df['VIG10DMIN'].isin([996, 997, 998, 999, 0]), 'VIG10DMIN'] = np.nan

# CIGDAYMO: 96, 97, 98, 99 to blank
df.loc[df['CIGDAYMO'].isin([96, 97, 98, 99]), 'CIGDAYMO'] = np.nan

# FRUTNO: 995, 996, 997, 998, 999 to blank
df.loc[df['FRUTNO'].isin([995, 996, 997, 998, 999]), 'FRUTNO'] = np.nan

# --- Output cleaned CSV ---
df.to_csv(OUTPUT, index=False)
print(f"Cleaned data written to {OUTPUT}")
