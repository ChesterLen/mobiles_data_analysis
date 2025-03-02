import pandas as pd

df = pd.read_csv('../mobiles_dataset_2025.csv')

df_clean = df.dropna(subset=['Screen Size'])

most_common_screen_size = df_clean['Screen Size'].mode()[0]

print(f"The most common screen size is: {most_common_screen_size} inches")