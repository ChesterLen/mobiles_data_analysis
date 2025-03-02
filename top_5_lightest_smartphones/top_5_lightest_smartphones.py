import pandas as pd

df = pd.read_csv('../mobiles_dataset_2025.csv')

df['Mobile Weight'] = df['Mobile Weight'].astype(str).str.replace(r"[^\d.]", "", regex=True)

df['Mobile Weight'] = pd.to_numeric(df['Mobile Weight'], errors='coerce')

df_clean = df.dropna(subset=['Mobile Weight'])

top_5_lightest_smartphones = df_clean.nsmallest(5, 'Mobile Weight')

print(top_5_lightest_smartphones[['Model Name', 'Company Name', 'Mobile Weight']])