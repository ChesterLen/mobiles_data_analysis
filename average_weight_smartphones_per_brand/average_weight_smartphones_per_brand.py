import pandas as pd

df = pd.read_csv('../mobiles_dataset_2025.csv')

df['Mobile Weight'] = df['Mobile Weight'].astype(str).str.replace(r"[^\d.]", "", regex=True)

df['Mobile Weight'] = pd.to_numeric(df['Mobile Weight'], errors='coerce')

df_clean = df.dropna(subset=['Mobile Weight'])

average_weight_per_brand = df_clean.groupby('Company Name')['Mobile Weight'].mean()

print(average_weight_per_brand.round(2))