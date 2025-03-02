import pandas as pd
from data.data import df

df["Mobile Weight"] = df["Mobile Weight"].astype(str).str.replace(r"[^\d.]", "", regex=True)

df["Mobile Weight"] = pd.to_numeric(df["Mobile Weight"], errors="coerce")

top_5_heaviest_smartphones = df.nlargest(5, 'Mobile Weight')

print(top_5_heaviest_smartphones[["Model Name", "Company Name", "Mobile Weight"]])