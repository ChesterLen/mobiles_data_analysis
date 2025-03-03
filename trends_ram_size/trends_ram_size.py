import pandas as pd
import re
import matplotlib.pyplot as plt

df = pd.read_csv('mobiles_dataset_2025.csv')

def extract_max_ram(ram_string):
    if pd.isna(ram_string):
        return None

    numbers = re.findall(r"\d+", ram_string)
    return max(map(int, numbers)) if numbers else None

df['RAM'] = df['RAM'].astype(str).apply(extract_max_ram)

df['RAM'] = pd.to_numeric(df['RAM'], errors='coerce')

df_clean = df.dropna(subset=['RAM'])

plt.figure(figsize=(8,5))
df_clean['RAM'].hist(bins=10)
plt.xlabel('RAM Size (GB)')
plt.ylabel('Number of Smartphones')
plt.title('Distribution of RAM Sizes')
plt.show()