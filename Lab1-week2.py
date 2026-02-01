import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
raw = {
    "age": [25, "N/A", 40, 33, "?"],
    "income": [50000, 60000, None, "unknown", 80000],
    "churned": [0, 1, 0, 1, 0],
}

df_raw = pd.DataFrame(raw)

df = df_raw.replace(["N/A", "?", "unknown"], np.nan)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["income"] = pd.to_numeric(df["income"], errors="coerce")

print(df.isna().mean() * 100)

df_A = df.dropna()

df_B = df.copy()

df_B["age_missing"] = df_B["age"].isna().astype(int)
df_B["income_missing"] = df_B["income"].isna().astype(int)

df_B["age"] = df_B["age"].fillna(df_B["age"].mean())
df_B["income"] = df_B["income"].fillna(df_B["income"].mean())

print("\nVersion A:")
print(df_A)

print("\nVersion B:")
print(df_B)

plt.figure()
plt.hist(df_A["age"], label="Version A")
plt.hist(df_B["age"],  label="Version B")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Histogram")
plt.legend()
plt.show()
