import pandas as pd

df = pd.read_csv('../mobiles_dataset_2025.csv')

df_clean = df.dropna(subset=['Mobile Weight'])

df_clean['Mobile Weight'] = df_clean['Mobile Weight'].str.strip('g')

df_clean['Mobile Weight'] = pd.to_numeric(df_clean['Mobile Weight'], errors='coerce')

lightest_brand = df_clean.groupby('Company Name')['Mobile Weight'].mean().idxmin()

print(f"The brand with the lightest smartphones on average is: {lightest_brand}")