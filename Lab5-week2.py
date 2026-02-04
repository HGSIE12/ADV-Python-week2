import numpy as np
import pandas as pd

np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])
df = pd.DataFrame({"income": values})

Q1 = df["income"].quantile(0.25)
Q3 = df["income"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers_iqr = df[(df["income"] < lower) | (df["income"] > upper)]

mean = df["income"].mean()
std = df["income"].std()

z_scores = (df["income"] - mean) / std
outliers_z = df[np.abs(z_scores) > 3]

df_iqr_cap = df.copy()
df_iqr_cap["income"] = np.clip(df_iqr_cap["income"], lower, upper)

df_log = df.copy()
df_log["income"] = np.log1p(df_log["income"])

print(len(outliers_iqr))
print(len(outliers_z))

print(df.describe())
print(df_iqr_cap.describe())
print(df_log.describe())
