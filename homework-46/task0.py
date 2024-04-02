import numpy as np
import pandas as pd


# data = pd.DataFrame(np.random.standard_normal((1000, 4)))
# print(data)
# print(data.describe())
# col = data[2]
# print(col[col.abs() > 3])
# print(data[(data.abs() > 3).any(axis='columns')])
# data[data.abs() > 3] = np.sign(data) * 3
# print(data.describe())
# print(np.sign(data).head())

# df = pd.DataFrame(np.arange(5 * 7).reshape((5, 7)))
# print(df)
# sampler = np.random.permutation(5)
# print(sampler)
# print(df.take(sampler))
# print(df.iloc[sampler])

# column_sampler = np.random.permutation(7)
# print(column_sampler)
# print(df.take(column_sampler, axis='columns'))
# print(df.sample(n=3))
#
# choices = pd.Series([5, 7, -1, 6, 4])
# print(choices.sample(n=10, replace=True))

# df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
# print(df)
# print( pd.get_dummies(df['key']))
# dummies = pd.get_dummies(df['key'], prefix='key')
# df_with_dummy = df[['data1']].join(dummies)
# print(df_with_dummy)

# mnames = ['movie_id', 'title', 'genres']
# movies = pd.read_table('movies.dat', sep='::',
#                        header=None, names=mnames, engine='python')
# print(movies[:10])
# dummies = movies['genres'].str.get_dummies('|')
# print(dummies.iloc[:10, :6])
# movies_windic = movies.join(dummies.add_prefix('Genre_'))
# print(movies_windic.iloc[0])

# np.random.seed(12345)
# values = np.random.uniform(size=10)
# print(values)
# bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
# print(pd.get_dummies(pd.cut(values, bins)))

# s = pd.Series([1, 2, 3, None])
# print(s)
# s = pd.Series([1, 2, 3, None], dtype=pd.Int64Dtype())
# print(s)
# print(s.isna())
# print(s.dtype)
# print(s[3])
# print(s[3] is pd.NA)

# s = pd.Series([1, 2, 3, None], dtype='Int64')
# print(s)
# s = pd.Series(['one', 'two', None, 'three'], dtype=pd.StringDtype())
# print(s)
#
# df = pd.DataFrame({'A': [1, 2, None, 4],
#                    'B': ['one', 'two', 'three', None],
#                    'C': [False, None, False, True]})
# print(df)
#
# df['A'] = df['A'].astype('Int64')
# df['B'] = df['B'].astype('string')
# df['C'] = df['C'].astype('boolean')
# print(df)

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data': [i for i in range(6)]})
print(df)
print(pd.get_dummies(df['key']))
