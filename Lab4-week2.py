import pandas as pd

# Data
rows = [
    {"user": "U1", "day": "2024-01-01", "product": "A", "clicked": 1},
    {"user": "U1", "day": "2024-01-01", "product": "A", "clicked": 1},
    {"user": "U1", "day": "2024-01-01", "product": "B", "clicked": 0},
    {"user": "U2", "day": "2024-01-02", "product": "A", "clicked": 1},
]

df = pd.DataFrame(rows)

df_no_exact = df.drop_duplicates()

df_unique = df_no_exact.drop_duplicates(subset=["user", "day", "product"])

user_features = df_unique.groupby("user")["clicked"].sum().reset_index()

print(df_no_exact)
print( df_unique)
print(user_features)
