import pandas as pd

df = pd.read_excel("data.xlsx")
df = df.dropna()

if 'Price' in df.columns:
    df['Total'] = df['Price'] * 2

df.to_excel("cleaned_data.xlsx", index=False)

print("Done!")