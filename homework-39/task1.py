import numpy as np


class Index:
    def __init__(self, data=None, name=None, copy=False):
        self.data = np.array(data) if data is not None else np.array([])
        self._name = name
        self.sorted_indices = np.argsort(self.data)

        if copy:
            self.data = self.data.copy()

    @property
    def dtype(self):
        return type(self.data[0]) if len(self.data) > 0 else None

    @property
    def name(self):
        return self._name

    @property
    def values(self):
        return self.data

    def _binary_search(self, value):
        low, high = 0, len(self.data)

        while low < high:
            mid = (low + high) // 2

            if self.data[mid] < value:
                low = mid + 1
            else:
                high = mid

        return low

    def _find_indices(self, values):
        indices = []

        for v in values:
            start_idx = self._binary_search(v)
            idx = start_idx

            while idx < len(self.data) and self.data[idx] == v:
                indices.append(self.sorted_indices[idx])
                idx += 1

            if not indices:
                raise ValueError(f'{v} is not in index')

        return indices

    def index(self, value):
        if isinstance(value, (list, tuple)):
            return self._find_indices(value)
        else:
            start_idx = self._binary_search(value)
            idx = start_idx
            indices = []

            while idx < len(self.data) and self.data[idx] == value:
                indices.append(self.sorted_indices[idx])
                idx += 1

            if not indices:
                raise ValueError(f'{value} is not in index')

            return indices

    def append(self, value):
        return Index(data=list(self.data) + [value], name=self.name)

    def difference(self, other):
        return Index(data=[d for d in self.data if d not in other.data], name=self.name)

    def intersection(self, other):
        return Index(data=[d for d in self.data if d in other.data], name=self.name)

    def union(self, other):
        return Index(data=list(self.data) + [d for d in other.data if d not in self.data], name=self.name)

    def isin(self, data):
        return np.array([d in data for d in self.data])

    def delete(self, loc):
        self.data = [d for idx, d in enumerate(self.data) if idx not in loc]

    def drop(self, labels):
        self.data = [d for d in self.data if d not in labels]

    def insert(self, loc, value):
        self.data = list(self.data[:loc]) + [value] + list(self.data[loc:])

    def unique(self):
        return sorted(set(self.data))

    def map(self, f):
        return Index(data=[f(value) for value in self.data], name=self.name)

    @property
    def is_monotonic(self):
        increasing = all(self.data[i] <= self.data[i + 1] for i in range(len(self.data) - 1))
        decreasing = all(self.data[i] >= self.data[i + 1] for i in range(len(self.data) - 1))

        return increasing or decreasing

    @property
    def is_unique(self):
        return len(set(self.data)) == len(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return f'Index({self.data}, name={self.name})'


class RangeIndex(Index):
    def __init__(self, start=0, stop=0, step=1, copy=False, name=None):
        data = np.arange(start, stop, step)
        super().__init__(data, name, copy)
