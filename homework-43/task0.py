import sys
import csv
import pandas as pd


df = pd.read_csv('ex1.csv')
print(df)
print(pd.read_csv('ex2.csv', header=None))
print(pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message']))

names = ['a', 'b', 'c', 'd', 'message']
print(pd.read_csv('ex2.csv', names=names, index_col='message'))

parsed = pd.read_csv('csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)

result = pd.read_csv('ex3.txt', sep='\s+')
print(result)

print(pd.read_csv('ex4.csv', skiprows=[0, 2, 3]))

result = pd.read_csv('ex5.csv')
print(result)
print(pd.isna(result))
result = pd.read_csv('ex5.csv', na_values=['NULL'])
print(result)
result2 = pd.read_csv('ex5.csv', keep_default_na=False)
print(result2)
print(result2.isna())
result3 = pd.read_csv('ex5.csv', keep_default_na=False, na_values=['NA'])
print(result3)
print(result3.isna())
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
print(pd.read_csv('ex5.csv', na_values=sentinels, keep_default_na=False))

pd.options.display.max_rows = 10
result = pd.read_csv('ex6.csv')
print(result)
print( pd.read_csv('ex6.csv', nrows=5))
chunker = pd.read_csv('ex6.csv', chunksize=1000)
print(type(chunker))

# tot = pd.Series([], dtype='int64')
# for piece in chunker:
#     tot = tot.add(piece['key'].value_counts(), fill_value=0)
# tot = tot.sort_values(ascending=False)
# print(tot[:10])

data = pd.read_csv('ex7.csv')
print(data)

data.to_csv('out.csv')
data.to_csv(sys.stdout, sep='|')
data.to_csv(sys.stdout, na_rep='NULL')
data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

f = open('ex7.csv')
reader = csv.reader(f)

for line in reader:
    print(line)

f.close()

with open('ex7.csv') as f:
    lines = list(csv.reader(f))

header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)
