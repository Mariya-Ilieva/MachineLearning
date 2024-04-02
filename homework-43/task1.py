import pandas as pd


def read_csv(file_path, **kwargs):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(kwargs.get('delimiter', ',')) for line in lines]

    if 'skiprows' in kwargs:
        data = [line for idx, line in enumerate(data) if idx not in kwargs['skiprows']]

    header = data[0]
    data = data[1:]

    return pd.DataFrame(data, columns=header)

df = read_csv('ex1.csv')
print(df)
print(read_csv('ex2.csv', header=None))
print(read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message']))

names = ['a', 'b', 'c', 'd', 'message']
print(read_csv('ex2.csv', names=names, index_col='message'))

parsed = read_csv('csv_mindex.csv')
print(parsed)

result = read_csv('ex3.txt', sep='\s+')
print(result)

print(read_csv('ex4.csv', skiprows=[0, 2, 3]))

result = read_csv('ex5.csv')
print(result)

result = read_csv('ex5.csv', na_values=['NULL'])
print(result)

result2 = read_csv('ex5.csv', keep_default_na=False)
print(result2)

result3 = read_csv('ex5.csv', keep_default_na=False, na_values=['NA'])
print(result3)

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
print(read_csv('ex5.csv', na_values=sentinels, keep_default_na=False))

pd.options.display.max_rows = 10
result = read_csv('ex6.csv')
print(result)

print( read_csv('ex6.csv', nrows=5))
chunker = read_csv('ex6.csv', chunksize=1000)

print(type(chunker))
chunker = read_csv('ex6.csv', chunksize=1000)
