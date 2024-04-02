import numpy as np
import random

from task1 import Index, RangeIndex
from ct import Categorical
from mi import MultiIndex


class Series:
    def __init__(self, data=None, index=None, dtype=None, name=None):
        if data is None:
            data = []

        if index is None:
            self._index = RangeIndex(0, 0, 1)
        elif isinstance(index, MultiIndex):
            self._index = index
        else:
            self._index = Index(index)

        if isinstance(data, Categorical):
            self.data = data
        else:
            self.data = np.array(data, dtype=dtype)

        self._dtype = dtype
        self._name = name

    @property
    def index(self):
        return self._index

    @property
    def dtype(self):
        return self._dtype

    @property
    def name(self):
        return self._name

    @property
    def values(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        if isinstance(item, tuple):
            if len(item) == 1:
                level = item[0]
                if level not in self._index:
                    raise KeyError(f'Level "{level}" not found in MultiIndex.')
                level_index = self._index.index(level)
                return Series(data=self.data[self._index[level_index]], index=self._index[level])
            elif len(item) == 2:
                level, sub_item = item
                if level not in self._index:
                    raise KeyError(f'Level "{level}" not found in MultiIndex.')
                level_index = self._index.index(level)
                codes = self._index[level_index]
                return self.data[codes[int(sub_item)]]
            else:
                raise IndexError('Unsupported index type for MultiIndex.')
        elif isinstance(item, str) and item in self._index:
            return self.data[self._index.index(item)]
        else:
            raise IndexError('Unsupported index type for MultiIndex.')

    def __setitem__(self, item, value):
        if isinstance(item, int):
            self.data[item] = value

        if isinstance(item, str):
            self.data[self._index.index(item)] = value

        if isinstance(item, list):
            for k, v in zip(item, value):
                self.data[self._index.index(k)] = v

    def __gt__(self, other):
        return [x > other for x in self.data]

    def __lt__(self, other):
        return [x < other for x in self.data]

    def __ge__(self, other):
        return [x >= other for x in self.data]

    def __le__(self, other):
        return [x <= other for x in self.data]

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self._index

        return item in self.data

    def __add__(self, other):
        if isinstance(other, Series):
            if self._index is None or other.index is None:
                raise ValueError('Both series must have an index for addition.')

            aligned_index = self._index.intersection(other.index)
            aligned_self = self.reindex(aligned_index)
            aligned_other = other.reindex(aligned_index)

            return Series(data=aligned_self.data + aligned_other.values, index=aligned_index, dtype=self.dtype)
        else:
            raise ValueError('Unsupported operand type(s) for +: "Series" and "{}"'.format(type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Series):
            if self._index is None or other.index is None:
                raise ValueError('Both series must have an index for multiplication.')

            aligned_index = self._index.intersection(other.index)
            aligned_self = self.reindex(aligned_index)
            aligned_other = other.reindex(aligned_index)

            return Series(data=aligned_self.data * aligned_other.values, index=aligned_index, dtype=self.dtype)
        else:
            return Series(data=self.data * other, index=self._index, dtype=self._dtype)

    def __rmul__(self, other):
        return self.__mul__(other)

    def isna(self):
        return [True if x is None else False for x in self.data]

    def notna(self):
        return [False if x is None else True for x in self.data]

    def reindex(self, new_index):
        new_data = []

        for idx in new_index:
            if idx in self._index:
                new_data.append(self[idx])
            else:
                new_data.append(None)

        return Series(new_data, new_index)

    def drop(self, labels):
        if isinstance(labels, (str, int)):
            if labels in self._index:
                idx_pos = self._index.index(labels)
                new_data = np.delete(self.data, idx_pos)
                new_index = self._index.drop(labels)
                return Series(data=new_data, index=new_index)
            else:
                raise KeyError(f'Label "{labels}" not found in index.')

        if isinstance(labels, list):
            idx_positions = [self._index.index(label) for label in labels if label in self._index]
            new_data = np.delete(self.data, idx_positions)
            new_index = self._index.drop([label for label in labels if label in self._index])
            return Series(data=new_data, index=new_index)

        raise TypeError('Labels must be either str or array-like.')

    def rank(self, method='average'):
        if method not in ['average', 'min', 'max', 'first', 'dense']:
            raise ValueError(
                f"Invalid method '{method}' for ranking. Available methods: 'average', 'min', 'max', 'first', 'dense'.")

        data_index = list(zip(self.data, self._index))
        sorted_data_index = sorted(data_index, key=lambda x: x[0])
        ranks = [0] * len(self)

        if method == 'average':
            sum = 0
            count = 0
            prev = None

            for i, (val, _) in enumerate(sorted_data_index):
                if val != prev:
                    if count > 0:
                        avg = sum / count

                        for j in range(i - count, i):
                            ranks[j] = avg

                    sum = i + 1
                    count = 1
                else:
                    sum += i + 1
                    count += 1

                prev = val

            if count > 0:
                avg = sum / count

                for j in range(len(sorted_data_index) - count, len(sorted_data_index)):
                    ranks[j] = avg

        elif method == 'min':
            for i, (val, _) in enumerate(sorted_data_index):
                rank = i + 1
                ranks[i] = rank

        elif method == 'max':
            for i, (val, _) in enumerate(sorted_data_index):
                rank = len(sorted_data_index) - i
                ranks[i] = rank

        elif method == 'first':
            for i, (val, _) in enumerate(sorted_data_index):
                rank = i + 1
                ranks[i] = rank

                if i > 0 and val == sorted_data_index[i - 1][0]:
                    ranks[i] = ranks[i - 1]

        elif method == 'dense':
            prev = None
            rank = 1

            for i, (val, _) in enumerate(sorted_data_index):
                if val != prev:
                    rank = i + 1

                ranks[i] = rank
                prev = val

        ranked_series = Series(data=ranks, index=self._index, dtype=int)
        return ranked_series

    def sort_index(self, ascending=True):
        sorted_idx = sorted(self._index, reverse=not ascending)
        sorted_data = [self.data[self._index.index(idx)] for idx in sorted_idx]

        return Series(data=sorted_data, index=sorted_idx, dtype=self._dtype, name=self._name)

    def sort_values(self, ascending=True):
        sorted_data_idx = sorted(zip(self.data, self._index), key=lambda x: x[0], reverse=not ascending)
        sorted_idx = [idx for _, idx in sorted_data_idx]
        sorted_data = [data for data, _ in sorted_data_idx]

        return Series(data=sorted_data, index=sorted_idx, dtype=self._dtype, name=self._name)

    def apply(self, func):
        result_data = [func(x) for x in self.data]
        return Series(data=result_data, index=self._index, dtype=self._dtype, name=self._name)

    def map(self, map_shape, na_action=None):
        if isinstance(map_shape, dict):
            result_data = [map_shape.get(v, np.nan) for v in self.data]
        elif isinstance(map_shape, Series):
            result_data = [map_shape.get(v, np.nan) for v in self.data]
        else:
            result_data = [map_shape(v) for v in self.data]

        if na_action == 'ignore':
            result_data = [v if v is not np.nan else np.nan for v in result_data]

        return Series(data=result_data, index=self._index, dtype=self._dtype, name=self._name)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)

        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else: # odd
            return sorted_data[n // 2]

    def quantile(self, q):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        index = int(n * q)

        return sorted_data[index]

    def pct_change(self):
        pct_changes = [(self.data[i] - self.data[i - 1]) / self.data[i - 1] for i in range(1, len(self.data))]
        pct_changes.insert(0, None)

        return pct_changes

    def var(self):
        mean = sum(self.data) / len(self.data)
        squared_diff = [(x - mean) ** 2 for x in self.data]

        return sum(squared_diff) / (len(self.data) - 1)

    def diff(self, periods=1):
        diff_values = [self.data[i] - self.data[i - periods] for i in range(periods, len(self.data))]

        return [None] * periods + diff_values

    def loc(self, label):
        if isinstance(label, str):
            if label in self._index:
                return self[self._index.index(label)]
            else:
                raise KeyError(f'Label "{label}" not found in index.')

        if isinstance(label, list):
            indices = [self._index.index(x) for x in label]
            return Series(data=self.data[indices], index=label)

        raise TypeError('Label must be either a string or a list of strings.')

    def iloc(self, position):
        if isinstance(position, int):
            return self.data[position]

        if isinstance(position, list):
            return Series(data=self.data[position], index=self._index[position])

        raise TypeError('Position must be an integer or a list of integers.')

    def dropna(self):
        res = ~np.isnan(self.data)
        return Series(data=self.data[res], index=self._index[res])

    def fillna(self, value):
        filled_data = [value if np.isnan(x) else x for x in self.data]
        return Series(data=filled_data, index=self._index)

    def duplicated(self):
        seen = set()
        duplicates = []

        for value in self.data:
            if value in seen:
                duplicates.append(True)
            else:
                duplicates.append(False)
                seen.add(value)

        return duplicates

    def drop_duplicates(self):
        seen = set()
        unique_data = []
        unique_index = []

        for value, index in zip(self.data, self._index):
            if value not in seen:
                unique_data.append(value)
                unique_index.append(index)
                seen.add(value)

        return Series(data=unique_data, index=unique_index)

    def replace(self, y, value):
        replaced_data = [value if x == y else x for x in self.data]
        return Series(data=replaced_data, index=self._index)

    def cut(self, data, bins):
        intervals = []

        for value in data:
            for i in range(len(bins) - 1):
                if bins[i] <= value < bins[i + 1]:
                    intervals.append((bins[i], bins[i + 1]))
                    break
            else:
                if value >= bins[-1]:
                    intervals.append((bins[-1], float('inf')))
                else:
                    intervals.append((float('-inf'), bins[0]))

        return Series(data=intervals, index=self._index)

    def qcut(self, data, q):
        intervals = []
        sorted_data = sorted(data)
        n = len(sorted_data)
        step = n // q

        for i in range(0, n, step):
            if i + step < n:
                intervals.append((sorted_data[i], sorted_data[i + step]))
            else:
                intervals.append((sorted_data[i], sorted_data[-1]))

        return Series(data=intervals, index=self._index)

    def describe(self):
        description = {
            'count': len(self.data),
            'mean': np.mean(self.data),
            'std': np.std(self.data),
            'min': np.min(self.data),
            '25%': np.percentile(self.data, 25),
            '50%': np.percentile(self.data, 50),
            '75%': np.percentile(self.data, 75),
            'max': np.max(self.data)
        }

        return description

    def get_dummies(self):
        unique = set(self.data)
        dummy_data = {}

        for value in unique:
            dummy_data[f'is_{value}'] = [x == value for x in self.data]

        return dummy_data

    def take(self, indices):
        if isinstance(indices, int):
            indices = [indices]
        elif isinstance(indices, list):
            if not all(isinstance(idx, int) for idx in indices):
                raise TypeError('Indices must be integers.')
        else:
            raise TypeError('Indices must be an integer or a list of integers.')

        return Series(data=[self.data[idx] for idx in indices], index=indices)

    def sample(self, n=None, replace=False):
        if n is None:
            n = len(self.data)

        if not isinstance(n, int) or n <= 0:
            raise ValueError(f'{n} must be a positive integer.')

        if not isinstance(replace, bool):
            raise TypeError(f'{replace} must be a boolean.')

        if replace:
            sampled_indices = [random.randint(0, len(self.data) - 1) for _ in range(n)]
        else:
            sampled_indices = random.sample(range(len(self.data)), min(n, len(self.data)))

        return self.take(sampled_indices)

    def astype(self, dtype):
        if dtype == 'category':
            categories = list(set(self.data))
            codes = [categories.index(item) for item in self.data]
            return Categorical(categories=categories, codes=codes)
        else:
            raise ValueError('Unsupported dtype for conversion to Categorical.')

    # def stack(self):
    #     return DataFrame({self._name: self.data}, index=self._index).stack()

    def __repr__(self):
        return f'Series(data={self.data}, index={self._index}, dtype={self.dtype}, name={self._name})'


# obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# print(obj)

# new_obj = obj.drop('c')
# print(new_obj)
# print(obj.drop(['d', 'c']))

# s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
# s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

# print(s1)
# print(s2)
# print(s1 + s2)
# print(s1 * s2)

# obj = Series(np.arange(5), index=['a', 'a', 'b', 'b', 'c'])
# print(obj.index.is_unique)
# print(obj['a'])
# print(obj['c'])

# obj = Series([11, 22, 33, 15], index=['a', 'b', 'c', 'd'])
# print(obj.rank(method='average'))
# print(obj.rank(method='min'))
# print(obj.rank(method='max'))
# print(obj.rank(method='first'))
# print(obj.rank(method='dense'))

# print(obj.sort_index())
# print(obj.sort_index(ascending=True))
# print(obj.sort_values())
# print(obj.sort_values(ascending=False))

# print(obj.apply(lambda x: x * 2))
# print(obj.apply(lambda x: x ** 2))
# print(obj.apply(lambda x: x - 5))

# obj = Series([1, 2, 3, None], index=['a', 'b', 'c', 'd'])
# mapping = {1: 'one', 2: 'two', 3: 'three'}
# print(obj.map(mapping))

# def format_s(s):
#     return f'Series el {s}'

# print(obj.map(format_s))
# print(obj.map(format_s, na_action='ignore'))

# series = Series([1, 2, 3, 4, 5])
# print(series.median())
# print(series.quantile(0.5))
# print(series.pct_change())
# print(series.var())
# print(series.diff())

# obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# print(obj)
# print(obj.loc(['a']))
# print(obj.loc(['a', 'c', 'e']))

# print(obj.iloc([0]))
# print(obj.iloc([0, 2, 4]))

# obj = Series([1, 2, np.nan, 4, np.nan], index=['a', 'b', 'c', 'd', 'e'])
# print(obj)
# obj_dropped = obj.dropna()
# print(obj_dropped)

# obj_filled = obj.fillna(0)
# print(obj_filled)

# obj = Series([1, 2, 2, 3, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# duplicates = obj.duplicated()
# print(duplicates)

# obj_unique = obj.drop_duplicates()
# print(obj_unique)

# obj_replaced = obj.replace(2, 10)
# print(obj_replaced)

# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bins = [18, 25, 35, 60, 100]
# obj = Series(ages)
# print(obj.cut(ages, bins))
# print(obj.qcut(ages, 4))

# obj = Series([1, 2, 3, 4, 5])
# print(obj.describe())
#
# obj = Series(['a', 'b', 'a', 'c', 'b'])
# print(obj.get_dummies())
#
# obj = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(obj.take(2))
# print(obj.take([1, 3, 4]))
# print(obj.sample(3, replace=False))
# print(obj.sample(5, replace=True))

data = Series(np.random.uniform(size=9))
levels = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']
codes = [1, 2, 3, 1, 3, 1, 2, 2, 3]
multi_index = MultiIndex(levels, codes)
series = Series(data=data, index=multi_index)

print(series['a'])
print(series['d'])
