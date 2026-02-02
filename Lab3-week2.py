import pandas as pd

raw = {
    "age": ["25", "30", "unknown"],
    "income": ["$50,000", "$60,000", None],
    "signup": ["2024-01-01", "01/05/2024", "not a date"],
}

df = pd.DataFrame(raw)

df["age"] = df["age"].replace("unknown", None)
df["income"] = df["income"].str.replace("$", "").str.replace(",", "")

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["income"] = pd.to_numeric(df["income"], errors="coerce")
df["signup"] = pd.to_datetime(df["signup"], errors="coerce")

print(df.dtypes)
print("\nNaN count:")
print(df.isna().sum())

print("\nFinal DataFrame:")
print(df)
