import numpy as np
import pandas as pd


# obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# print(obj)

# obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# print(obj2)

# obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print(obj3)
# print(obj3.reindex(np.arange(6), method='ffill'))

# frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
# print(frame)
# frame2 = frame.reindex(index=['a', 'b', 'c', 'd'])
# print(frame2)
# states = ['Texas', 'Utah', 'California']
# print(frame.reindex(columns=states))
# print(frame.reindex(states, axis='columns'))
# print(frame.loc[['a', 'd', 'c'], ['California', 'Texas']])

# obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# print(obj)
# new_obj = obj.drop('c')
# print(new_obj)
# print(obj.drop(['d', 'c']))
# data = pd.DataFrame(np.arange(16).reshape((4, 4)),
#                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
#                     columns=['one', 'two', 'three', 'four'])
# print(data)
# print(data.drop(index=['Colorado', 'Ohio']))
# print(data.drop(columns=['two']))
# print(data.drop('two', axis=1))
# print(data.drop(['two', 'four'], axis='columns'))

# obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# print(obj)
# print(obj['b'])
# print(obj[2:4])
# print(obj[['b', 'a', 'd']])
# print(obj[obj < 2])
# print(obj.loc[['b', 'a', 'd']])

# obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])
obj2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# print(obj1)
# print(obj2)
# print(obj1[[0, 1, 2]])
# # print(obj2.loc[[0, 1]])
# print(obj1.iloc[[0, 1, 2]])
# print(obj2.iloc[[0, 1, 2]])
# print(obj2.loc['b':'c'])

# obj2.loc['b':'c'] = 5
# print(obj2)

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
# print(data)
# print(data['two'])
# print(data[['three', 'one']])
# print(data[:2])
# print(data[data['three'] > 5])
# print(data < 5)

data[data < 5] = 0
print(data)
print(data.loc['Colorado'])
print(data.loc[['Colorado', 'New York']])
print(data.loc['Colorado', ['two', 'three']])

print(data.iloc[2])
print(data.iloc[[2, 1]])
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[[1, 2], [3, 0, 1]])

print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])
print(data.loc[data.three >= 2])
