import numpy as np
import pandas as pd


# obj = pd.Series([4, 7, -5, 3])
# print(obj)
# print(obj.array)
# print(obj.index)

# obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print(obj2)
# print(obj2.index)
# print(obj2['a'])
# print(obj2['d'])
# print(obj2[['c', 'a', 'd']])
# print(obj2[obj2 > 0])
# print(obj2 * 2)
# print(np.exp(obj2))
# print('b' in obj2)
# print('e' in obj2)

# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# obj3 = pd.Series(sdata)
# print(obj3)
# print(obj3.to_dict())

# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj4 = pd.Series(sdata, index=states)
# print(obj4)
# print(pd.isna(obj4))
# print(obj4.isna())
# print(pd.notna(obj4))

# print(obj3)
# print(obj4)
# print(obj3 + obj4)

# print(obj)
# obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
# print(obj)

# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
#  'year': [2000, 2001, 2002, 2001, 2002, 2003],
#  'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

# frame = pd.DataFrame(data)
# print(frame)
# print(frame.head())
# print(frame.tail())
# print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

# frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
# print(frame2)
# print(frame2.columns)
# print(frame2['state'])
# print(frame2.year)
# print(frame2.loc[1])
# print(frame2.iloc[2])
# frame2['debt'] = np.arange(6.)
# print(frame2)

# val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# frame2['debt'] = val
# print(frame2)
# frame2['eastern'] = frame2['state'] == 'Ohio'
# print(frame2)
# del frame2['eastern']
# print(frame2.columns)

# populations = {'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}, 'Nevada': {2001: 2.4, 2002: 2.9}}
# frame3 = pd.DataFrame(populations)
# print(frame3)
# print(frame3.T)
# print(pd.DataFrame(populations, index=[2001, 2002, 2003]))

# pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
# print(pd.DataFrame(pdata))
# frame3.index.name = 'year'
# frame3.columns.name = 'state'
# print(frame3)

# print(frame3.to_numpy())
# print(frame2.to_numpy())

# obj = pd.Series(np.arange(3), index=['a', 'b', 'c'])
# print(obj)
# index = obj.index
# print(index)
# print(index[1:])
# # index[1] = 'd' # TypeError
#
# labels = pd.Index(np.arange(3))
# print(labels)
# obj2 = pd.Series([1.5, -2.5, 0], index=labels)
# print(obj2)
# print(obj2.index is labels)
#
# print(frame3)
# print(frame3.columns)
# print('Ohio' in frame3.columns)
# print(2003 in frame3.index)
# print(pd.Index(['foo', 'foo', 'bar', 'bar']))

# data = pd.Series(['r', 'y', 'u'], index=[4, 6, 8])
# print(data[8])
# print(data)
# print(data.index)
