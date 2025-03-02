import pandas as pd

df = pd.read_csv('../mobiles_dataset_2025.csv')

df['Battery Capacity'] = pd.to_numeric(df['Battery Capacity'], errors='coerce')
df['Mobile Weight'] = pd.to_numeric(df['Mobile Weight'], errors='coerce')

df_clean = df.dropna(subset=['Battery Capacity', 'Mobile Weight'])

correlation = df_clean['Battery Capacity'].corr(df_clean['Mobile Weight'])

print(f"Correlation between Battery Capacity and Mobile Weight: {correlation}")
