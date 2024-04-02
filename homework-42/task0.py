import numpy as np
import pandas as pd


# obj = pd.Series(np.arange(4), index=['d', 'a', 'b', 'c'])
# print(obj)
# print(obj.sort_index())

# frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
#                      index=['three', 'one'],
#                      columns=['d', 'a', 'b', 'c'])
# print(frame)
# print(frame.sort_index())
# print(frame.sort_index(axis='columns'))
# print(frame.sort_index(axis='columns', ascending=False))

# obj = pd.Series([4, 7, -3, 2])
# print(obj.sort_values())

# obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
# print(obj.sort_values())
# print(obj.sort_values(na_position='first'))

# frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
# print(frame)
# print(frame.sort_values('b'))
# print(frame.sort_values(['a', 'b']))

# obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
# print(obj.rank())
# print(obj.rank(method='first'))
# print(obj.rank(ascending=False))

# frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
# print(frame)
# print(frame.rank(axis='columns'))

# obj = pd.Series(np.arange(5), index=['a', 'a', 'b', 'b', 'c'])
# print(obj)
# print(obj.index.is_unique)
# print(obj['a'])
# print(obj['c'])

# df = pd.DataFrame(np.random.standard_normal((5, 3)), index=['a', 'a', 'b', 'b', 'c'])
# print(df)
# print(df.loc['b'])
# print(df.loc['c'])

# obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
# print(obj.describe())

# df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
#                   index=['a', 'b', 'c', 'd'],
#                   columns=['one', 'two'])
# print(df.sum())
# print(df.sum(axis='columns'))
# print(df.sum(axis='index', skipna=False))
# print(df.sum(axis='columns', skipna=False))
# print(df.mean(axis='columns'))
# print(df.idxmax)
# print(df.idxmin)
# print(df.cumsum)
# print(df.describe())

# print(df.min)
# print(df.max)
# print(df.idxmin)
# print(df.idxmax)
# print(df.cummin)
# print(df.cummax)
#
# print(df.count())
# print(df.quantile())
# print(df.median())
# print(df.prod())
# print(df.var())
# print(df.std())
# print(df.skew())
# print(df.kurt())
# print(df.cumprod())
# print(df.diff())

# obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# uniques = obj.unique()
# print(uniques)
# print(obj.value_counts())
# print(obj)

# mask = obj.isin(['b', 'c'])
# print(mask)
# print(obj[mask])

# to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
# unique_vals = pd.Series(['c', 'b', 'a'])
# indices = pd.Index(unique_vals).get_indexer(to_match)
# print(indices)

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
print(data)
print(data['Qu1'].value_counts().sort_index())

data = pd.DataFrame({'a': [1, 1, 1, 2, 2], 'b': [0, 0, 1, 0, 0]})
print(data)
