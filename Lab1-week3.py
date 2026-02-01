import pandas as pd

train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})

test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})


age_median = train["age"].median()
city_mode = train["city"].mode()[0]


train["age_missing"] = train["age"].isna().astype(int)
train["city_missing"] = train["city"].isna().astype(int)


train["age"] = train["age"].fillna(age_median)
train["city"] = train["city"].fillna(city_mode)


test["age_missing"] = test["age"].isna().astype(int)
test["city_missing"] = test["city"].isna().astype(int)


test["age"] = test["age"].fillna(age_median)
test["city"] = test["city"].fillna(city_mode)


print(train)
print(test)
