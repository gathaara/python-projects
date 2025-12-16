import pandas as pd

df = pd.read_csv("data.csv")

# Remove missing values
df_clean = df.dropna()

# Save cleaned data
df_clean.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully")
