import numpy as np
import pandas as pd


# float_data = pd.Series([1.2, -3.5, np.nan, 0])
# print(float_data)
# print(float_data.isna())
#
# string_data = pd.Series(["aardvark", np.nan, None, "avocado"])
# print(string_data)
#
# float_data = pd.Series([1, 2, None], dtype='float64')
# print(float_data)
# print(float_data.isna())

# data = pd.Series([1, np.nan, 3.5, np.nan, 7])
# print(data.dropna())
# print(data[data.notna()])
#
# data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
# print(data)
# print(data.dropna(how="all"))
# data[4] = np.nan
# print(data)
# print(data.dropna(axis="columns", how="all"))

# df = pd.DataFrame(np.random.standard_normal((7, 3)))
# df.iloc[:4, 1] = np.nan
# df.iloc[:2, 2] = np.nan
# print(df)
# print(df.dropna())
# print(df.dropna(thresh=2))
# print( df.fillna(0))
# print(df.fillna({1: 0.5, 2: 0}))

# df = pd.DataFrame(np.random.standard_normal((6, 3)))
# df.iloc[2:, 1] = np.nan
# df.iloc[4:, 2] = np.nan
# print(df)
# print(df.fillna(method="ffill"))
# print(df.fillna(method="ffill", limit=2))
#
# data = pd.Series([1., np.nan, 3.5, np.nan, 7])
# print(data.fillna(data.mean()))

# data = pd.DataFrame({"k1": ["one", "two"] * 3 + ["two"], "k2": [1, 1, 2, 3, 3, 4, 4]})
# print(data)
# print(data.duplicated())
# print(data.drop_duplicates())
# data["v1"] = range(7)
# print(data)
# print(data.drop_duplicates(subset=["k1"]))
# print(data.drop_duplicates(["k1", "k2"], keep="last"))

# data = pd.DataFrame({"food": ["bacon", "pulled pork", "bacon",
#                               "pastrami", "corned beef", "bacon",
#                               "pastrami", "honey ham", "nova lox"],
#                      "ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
# print(data)
#
# meat_to_animal = {
#  "bacon": "pig",
#  "pulled pork": "pig",
#  "pastrami": "cow",
#  "corned beef": "cow",
#  "honey ham": "pig",
#  "nova lox": "salmon"
# }
#
# data["animal"] = data["food"].map(meat_to_animal)
# print(data)
#
# def get_animal(x):
#     return meat_to_animal[x]
#
# print( data["food"].map(get_animal))

# data = pd.Series([1., -999., 2., -999., -1000., 3.])
# print(data)
# print(data.replace(-999, np.nan))
# print(data.replace([-999, -1000], np.nan))
# print(data.replace([-999, -1000], [np.nan, 0]))
# print(data.replace({-999: np.nan, -1000: 0}))

# data = pd.DataFrame(np.arange(12).reshape((3, 4)),
#                     index=["Ohio", "Colorado", "New York"],
#                     columns=["one", "two", "three", "four"])
#
# def transform(x):
#     return x[:4].upper()
#
# print(data.index.map(transform))
# data.index = data.index.map(transform)
# print(data)
# print(data.rename(index=str.title, columns=str.upper))
# print(data.rename(index={"OHIO": "INDIANA"}, columns={"three": "peekaboo"}))

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
age_categories = pd.cut(ages, bins)
print(age_categories)
# print(age_categories.codes)
# print(age_categories.categories)
# print(age_categories.categories[0])
# print(pd.value_counts(age_categories))
print(pd.cut(ages, bins, right=False))

group_names = ["Youth", "YoungAdult", "MiddleAged", "Senior"]
print(pd.cut(ages, bins, labels=group_names))

# data = np.random.uniform(size=20)
# print(pd.cut(data, 4, precision=2))

data = np.random.standard_normal(1000)
quartiles = pd.qcut(data, 4, precision=2)
# print(quartiles)
# print(pd.value_counts(quartiles))
print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))
