import pandas as pd

df = pd.read_csv('../mobiles_dataset_2025.csv')

top_3_brands = df['Company Name'].value_counts().head(3)

print("Top 3 Brands with Most Smartphone Models:\n", top_3_brands)