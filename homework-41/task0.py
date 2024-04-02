import numpy as np
import pandas as pd


ser = pd.Series(np.arange(3.))
print(ser)

ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser.iloc[-1])
print(ser[:2])

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

data.loc[:, 'one'] = 1
print(data)

data.iloc[2] = 5
print(data)

data.loc[data['four'] > 5] = 3
print(data)

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

print(s1)
print(s2)
print(s1 + s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1)
print(df2)
print(df1 + df2)

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})

print(df1)
print(df2)
print(df1 + df2)

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan

print(df1)
print(df2)
print(df1 + df2)

df1.add(df2, fill_value=0)
print(1 / df1)
print(df1.rdiv(1))

df1.reindex(columns=df2.columns, fill_value=0)

arr = np.arange(12.).reshape((3, 4))
print(arr)

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.iloc[0]
print(frame)
print(series)
print(frame - series)

series2 = pd.Series(np.arange(3), index=['b', 'e', 'f'])
print(series)
print(frame + series2)

series3 = frame['d']
print(frame)
print(series3)

frame.sub(series3, axis='index')
frame = pd.DataFrame(np.random.standard_normal((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(frame)
print(np.abs(frame))

def f1(x):
    return x.max() - x.min()

print(frame.apply(f1))
print(frame.apply(f1, axis='columns'))

def f2(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])

print(frame.apply(f2))

def my_format(x):
    return f'{x:.2f}'

print(frame.map(my_format))
print(frame['e'].map(my_format))
