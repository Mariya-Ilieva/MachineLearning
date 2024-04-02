import json
import numpy as np
from task2 import Series
from task1 import Index, RangeIndex


class DataFrame:
    def __init__(self, data=None, index=None, columns=None):
        if data is None:
            data = {}

        self.data = data
        self.columns = list(data.keys())

        if isinstance(data, np.ndarray):
            if index is None:
                self._index = RangeIndex(0, 0, 1)
            else:
                self._index = Index(index)

            if columns is None:
                columns = RangeIndex(0, data.shape[1], 1)

            self.data = {col: Series(data[:, i], index=index) for i, col in enumerate(columns)}
            self.columns = list(columns)
        else:
            if isinstance(data, dict):
                if all(isinstance(value, list) for value in data.values()):
                    if index is None:
                        self._index = RangeIndex(0, 0, 1)
                    else:
                        self._index = Index(index)

                    if columns is None:
                        columns = list(data.keys())

                    self.data = {key: Series(value, index) for key, value in data.items()}
                    self.columns = list(columns)
                else:
                    raise ValueError('Data must be a dictionary with list-like values.')
            else:
                raise ValueError('Data must be a dictionary or a numpy array.')

    def __getitem__(self, item):
        if isinstance(item, str):
            if item in self.columns:
                return self.data[item]
            else:
                raise KeyError(f'Column "{item}" not found.')
        else:
            raise TypeError('Column must be accessed by string.')

    def __setitem__(self, key, value):
        if isinstance(value, Series):
            if len(value) == len(self._index):
                self.data[key] = value
            else:
                raise ValueError('Series length must match DataFrame index length.')
        else:
            raise TypeError('Value must be a Series.')

    def reindex(self, new_index):
        new_data = {}

        for key, series in self.data.items():
            new_data[key] = series.reindex(new_index)

        return DataFrame(data=new_data, index=new_index)

    def drop(self, labels=None, axis=0):
        if axis == 0 or axis == 'index':
            if labels is None:
                raise ValueError('Labels must be specified when dropping rows.')

            if isinstance(labels, str):
                if labels in self._index:
                    new_data = {key: series.drop(labels) for key, series in self.data.items()}
                    return DataFrame(data=new_data, index=self._index.drop(labels))
                else:
                    raise KeyError(f'Label "{labels}" not found in index.')

            if isinstance(labels, list):
                new_data = {key: series.drop(labels) for key, series in self.data.items()}
                return DataFrame(data=new_data, index=self._index.drop(labels))

            raise TypeError('Labels must be either str or array-like.')

        elif axis == 1 or axis == 'columns':
            if labels is None:
                raise ValueError('Labels must be specified when dropping columns.')

            if isinstance(labels, str):
                if labels in self.columns:
                    new_data = {key: series for key, series in self.data.items() if key != labels}
                    new_columns = [col for col in self.columns if col != labels]
                    return DataFrame(data=new_data, index=self._index)
                else:
                    raise KeyError(f'Column "{labels}" not found.')

            if isinstance(labels, list):
                new_data = {key: series for key, series in self.data.items() if key not in labels}
                new_columns = [col for col in self.columns if col not in labels]
                return DataFrame(data=new_data, index=self._index)

            raise TypeError('Labels must be either str or array-like.')

        else:
            raise ValueError('Axis must be 0 or "index" for rows, or 1 or "columns" for columns.')

    def add(self, other, fill_value=0):
        if isinstance(other, DataFrame):
            if self._index == other._index and self.columns == other.columns:
                new_data = {}

                for col in self.columns:
                    if col in other.columns:
                        new_data[col] = self.data[col] + other.data[col]
                    else:
                        new_data[col] = self.data[col] + fill_value

                for col in other.columns:
                    if col not in self.columns:
                        new_data[col] = other.data[col] + fill_value

                return DataFrame(data=new_data, index=self._index, columns=self.columns)
            else:
                raise ValueError('Index and columns must match for addition.')
        else:
            raise TypeError('Unsupported operand type(s) for +: "DataFrame" and "{}"'.format(type(other)))

    def radd(self, other, fill_value=0):
        return self.add(other, fill_value=fill_value)

    def div(self, other, fill_value=0):
        if isinstance(other, DataFrame):
            if self._index == other._index and self.columns == other.columns:
                new_data = {}

                for col in self.columns:
                    if col in other.columns:
                        new_data[col] = self.data[col] / other.data[col]
                    else:
                        new_data[col] = self.data[col] / fill_value

                for col in other.columns:
                    if col not in self.columns:
                        new_data[col] = fill_value / other.data[col]

                return DataFrame(data=new_data, index=self._index, columns=self.columns)
            else:
                raise ValueError('Index and columns must match for division.')
        else:
            raise TypeError('Unsupported operand type(s) for /: "DataFrame" and "{}"'.format(type(other)))

    def rdiv(self, other, fill_value=0):
        return self.div(other, fill_value=fill_value)

    def loc(self, label):
        return {key: self.data[key][label] for key in self.data}

    def iloc(self, pos):
        return {key: self.data[key][pos] for key in self.data}

    def at(self, label, column):
        if column not in self.columns:
            raise KeyError(f'Column "{column}" not found.')

        series = self.data[column]
        return series[label]

    def iat(self, i, j):
        if j >= len(self.columns):
            raise IndexError(f'Column index "{j}" out of range.')

        series = self.data[self.columns[j]]
        return series[i]

    @classmethod
    def read_json(cls, file_path):
        data = {}

        with open(file_path, 'r') as file:
            lines = file.readlines()
            columns = lines[0].strip().split(',')

            for column in columns:
                data[column] = []

            for line in lines[1:]:
                values = line.strip().split(',')

                for i, value in enumerate(values):
                    data[columns[i]].append(value)

        return cls(data)

    def to_json(self, file_path):
        data_dict = {}

        for column in self.columns:
            data_dict[column] = []

        for i in range(len(self._index)):
            for column in self.columns:
                data_dict[column].append(self.data[column][i])

        with open(file_path, 'w') as file:
            json.dump(data_dict, file)

    @classmethod
    def read_xml(cls, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        data = {}
        columns = []
        for line in lines:
            if line.startswith('<DataFrame>'):
                continue

            if line.startswith('</DataFrame>'):
                break

            if line.startswith('<'):
                column = line.strip('<').strip('>\n')
                columns.append(column)
                data[column] = []
            elif columns:
                values = line.strip().split(',')

                for i, value in enumerate(values):
                    if i < len(columns):
                        data[columns[i]].append(value)

        return cls(data)

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return {col: self.data[col] > other for col in self.data}
        elif isinstance(other, DataFrame):
            if self.columns != other.columns:
                raise ValueError('DataFrames must have the same columns for comparison.')

            result = {}
            for col in self.data:
                result[col] = self.data[col] > other.data[col]

            return result

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return {col: self.data[col] < other for col in self.data}
        elif isinstance(other, DataFrame):
            if self.columns != other.columns:
                raise ValueError('DataFrames must have the same columns for comparison.')

            result = {}
            for col in self.data:
                result[col] = self.data[col] < other.data[col]

            return result

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return {col: self.data[col] >= other for col in self.data}
        elif isinstance(other, DataFrame):
            if self.columns != other.columns:
                raise ValueError('DataFrames must have the same columns for comparison.')

            result = {}
            for col in self.data:
                result[col] = self.data[col] >= other.data[col]

            return result

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return {col: self.data[col] <= other for col in self.data}
        elif isinstance(other, DataFrame):
            if self.columns != other.columns:
                raise ValueError('DataFrames must have the same columns for comparison.')

            result = {}
            for col in self.data:
                result[col] = self.data[col] <= other.data[col]

            return result

    def dropna(self):
        new_data = {}

        for key, series in self.data.items():
            new_series = series.dropna()

            if len(new_series) > 0:
                new_data[key] = new_series

        return DataFrame(data=new_data, index=self._index)

    def fillna(self, value):
        new_data = {}

        for key, series in self.data.items():
            new_series = series.fillna(value)
            new_data[key] = new_series

        return DataFrame(data=new_data, index=self._index)

    def duplicated(self, subset=None):
        if subset is None:
            subset = self.columns

        if isinstance(subset, str):
            subset = [subset]

        duplicates = {}
        for col in subset:
            duplicates[col] = self.data[col].duplicated()

        return duplicates

    def drop_duplicates(self, subset=None, keep='first', inplace=False):
        if subset is None:
            subset = self.columns

        if isinstance(subset, str):
            subset = [subset]

        new_data = {}
        for col in self.columns:
            if col not in subset:
                new_data[col] = self.data[col]
            else:
                if keep == 'first':
                    mask = ~self.data[col].duplicated()
                elif keep == 'last':
                    mask = ~self.data[col].duplicated(keep='last')
                elif keep == 'False':
                    mask = ~self.data[col].duplicated(keep=False)
                else:
                    raise ValueError('Invalid value for "keep". Use "first", "last", or "False".')

                new_data[col] = self.data[col][mask]

        if inplace:
            self.data = new_data
            return None
        else:
            return DataFrame(data=new_data, index=self._index)

    def map(self, func):
        new_data = {}

        for col, series in self.data.items():
            new_data[col] = series.map(func)

        return DataFrame(data=new_data, index=self._index)

    def replace(self, to_replace, value=None):
        new_data = {}

        for col, series in self.data.items():
            new_data[col] = series.replace(to_replace, value)

        return DataFrame(data=new_data, index=self._index)

    def cut(self, bins, labels=None):
        new_data = {}

        for col, series in self.data.items():
            cut_values = []

            for value in series.values:
                if value <= bins[0]:
                    cut_values.append(labels[0] if labels else bins[0])
                elif value > bins[-1]:
                    cut_values.append(labels[-1] if labels else bins[-1])
                else:
                    for i in range(len(bins) - 1):
                        if bins[i] < value <= bins[i + 1]:
                            cut_values.append(labels[i] if labels else f'({bins[i]}, {bins[i + 1]})')
                            break

            new_data[col] = cut_values

        return DataFrame(data=new_data, index=self._index)

    def qcut(self, q, labels=None):
        new_data = {}

        for col, series in self.data.items():
            sorted_values = sorted(series.values)
            cut_values = []
            step = len(sorted_values) // q

            for i in range(0, len(sorted_values), step):
                if i + step < len(sorted_values):
                    cut_values.extend(
                        [labels[i // step] if labels else f'({sorted_values[i]}, {sorted_values[i + step]})'] * step)
                else:
                    cut_values.extend(
                        [labels[i // step] if labels else f'({sorted_values[i]}, {sorted_values[-1]})'] * (
                                len(sorted_values) - i))
                    break

            new_data[col] = cut_values

        return DataFrame(data=new_data, index=self._index)

    def describe(self):
        descriptions = {}

        for column_name, series in self.data.items():
            descriptions[column_name] = {
                'count': len(series),
                'mean': np.mean(series.values),
                'std': np.std(series.values),
                'min': np.min(series.values),
                '25%': np.percentile(series.values, 25),
                '50%': np.percentile(series.values, 50),
                '75%': np.percentile(series.values, 75),
                'max': np.max(series.values)
            }

        return descriptions

    def get_dummies(self):
        dummy_data = {}

        for column, series in self.data.items():
            if series.dtype == 'object':
                unique = set(series.values)

                for value in unique:
                    dummy_column = f'{column}_{value}'
                    dummy_data[dummy_column] = [v == value for v in series.values]
            else:
                dummy_data[column] = series.values

        return DataFrame(data=dummy_data, index=self._index)

    def take(self, indices):
        taken_data = {}

        for column_name, series in self.data.items():
            taken_data[column_name] = series.take(indices)

        return DataFrame(data=taken_data, index=self._index.index(indices))

    def sample(self, n=None, replace=False, random_state=None):
        if n is None:
            n = len(self._index)

        if random_state is not None:
            np.random.seed(random_state)

        sampled_indices = np.random.choice(len(self._index), size=n, replace=replace)
        return self.take(sampled_indices)

    def join(self, other, on):
        if not isinstance(other, DataFrame):
            raise ValueError(f'Parameter "{other}" must be a DataFrame.')

        if on in self.columns and on in other.columns:
            merged_data = {}
            merged_columns = []

            for column in self.columns:
                if column != on:
                    merged_data[column] = self.data[column]
                    merged_columns.append(column)

            for column in other.columns:
                if column != on and column not in merged_columns:
                    merged_data[column] = other.data[column]
                    merged_columns.append(column)

            return DataFrame(data=merged_data, columns=merged_columns)
        else:
            raise ValueError(f'Column "{on}" not found in both DataFrames.')

    def unstack(self, level=-1, fill_value=None):
        unstacked = DataFrame(self.data).unstack(level=level, fill_value=fill_value)

        if isinstance(unstacked, Series):
            return Series(data=unstacked.values, index=unstacked.index)
        else:
            return Series(data=unstacked.values.ravel(), index=unstacked.index)

    def set_index(self, keys, inplace=False):
        if isinstance(keys, str):
            keys = [keys]

        if not all(key in self.columns for key in keys):
            raise KeyError('One or more specified column(s) not found in DataFrame.')

        new_index = Index(self.data[keys[0]].values)
        for key in keys[1:]:
            new_index = new_index + Index(self.data[key].values)

        if inplace:
            self._index = new_index
            return None
        else:
            return DataFrame(data=self.data, index=new_index, columns=self.columns)

    def reset_index(self, inplace=False):
        new_data = {}

        for key, series in self.data.items():
            new_data[key] = series.values

        if inplace:
            self._index = RangeIndex(0, len(self._index), 1)
            return None
        else:
            return DataFrame(data=new_data, index=RangeIndex(0, len(self._index), 1), columns=self.columns)

    def __repr__(self):
        output = ''
        for key, value in self.data.items():
            output += f'{key}: {value}\n'
        return output


# data = DataFrame({'one': [0, 1, 2, 3], 'two': [4, 5, 6, 7], 'three': [8, 9, 10, 11], 'four': [12, 13, 14, 15]},
#                   index=['Ohio', 'Colorado', 'Utah', 'New York'])
# print(data)
# print(data.drop(labels=['Colorado', 'Utah']))
# print(data.drop(columns=['two']))
# print(data.drop('two', axis=1))
# print(data.drop(['two', 'four'], axis='columns'))
#
# df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
#                    index=['Ohio', 'Texas', 'Colorado'])
# df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
#                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])
#
# print(df1)
# print(df2)
# print(df1.add(df2))
#
# df1 = DataFrame({'A': [1, 2]})
# df2 = DataFrame({'B': [3, 4]})
#
# print(df1)
# print(df2)
# print(df1.add(df2))
#
# df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
# df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
#
# print(df1)
# print(df2)
# print(df1.add(df2))
#
# df1.add(df2, fill_value=0)
# print(df1.rdiv(1))

# df1 = DataFrame.read_json('data1.json')
# print(df1)
# df1.to_json('output.json')
# print(DataFrame.read_json('output.json'))

# df2 = DataFrame.read_xml('data2.xml')
# print(df2)

# df1 = DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9]}, index=['a', 'b', 'c'])
# df2 = DataFrame({'A': [5, 4, 3, 2, 1], 'B': [9, 8, 7, 6]}, index=['a', 'b', 'd'])
#
# print(df1 > 2)
# print(df2 < 3.3)
# print(df1 >= 2.2)
# print(df2 <= 5)
#
# print(df1 > df2)
# print(df1 < df2)
# print(df1 >= df2)
# print(df1 <= df2)

# data = {
#     'A': [1, np.nan, 3, 4, 5],
#     'B': [6, 7, 8, np.nan, 10],
#     'C': [np.nan, 12, 13, 14, 15]
# }
# index = Index(['a', 'b', 'c', 'd', 'e'])
# df = DataFrame(data, index=index)

# print(df.dropna())
# print(df.fillna(0))
# print(df.duplicated())
# print(df.map(lambda x: x**2))
# print(df.replace(np.nan, -1))

# print(df.describe())
# print(df.get_dummies())
# print(df.take([0, 2, 4]))
# print(df.sample(n=5, replace=False, random_state=42))

# data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
# df1 = DataFrame(data1)
#
# data2 = {'ID': [1, 2, 4], 'Age': [25, 30, 35]}
# df2 = DataFrame(data2)
#
# joined_df = df1.join(df2, on='ID')
# print(joined_df)
